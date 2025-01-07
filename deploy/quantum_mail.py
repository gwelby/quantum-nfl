import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import yaml
import jinja2
import logging
from datetime import datetime
import asyncio
from aiosmtplib import SMTP
import aioimaplib
from colorama import init, Fore, Style

init()

class QuantumMailManager:
    def __init__(self):
        self.setup_logging()
        self.load_config()
        self.setup_templates()
        
    def setup_logging(self):
        """Configure logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('QuantumMail')
        
    def load_config(self):
        """Load mail configuration"""
        config_path = Path(__file__).parent / 'secure_config.yml'
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
            
        self.email_config = self.config['email']
        self.workflows = self.config['workflows']
        
    def setup_templates(self):
        """Setup Jinja2 templates for emails"""
        template_dir = Path(__file__).parent / 'templates' / 'email'
        template_dir.mkdir(parents=True, exist_ok=True)
        
        # Create default templates if they don't exist
        self.create_default_templates(template_dir)
        
        self.template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(template_dir))
        )
        
    def create_default_templates(self, template_dir):
        """Create default email templates"""
        templates = {
            'support_acknowledgment.html': """
                <h2>Thank you for contacting Quantum NFL Support</h2>
                <p>We have received your message and will get back to you shortly.</p>
                <p>Your message has been categorized as: {{ category }}</p>
                <hr>
                <p>Best regards,<br>Quantum NFL Team</p>
            """,
            'analysis_received.html': """
                <h2>Quantum NFL Analysis Request Received</h2>
                <p>Thank you for your analysis request. Our quantum algorithms are processing your data.</p>
                <p>We will notify you once the analysis is complete.</p>
                <hr>
                <p>Best regards,<br>Quantum NFL Team</p>
            """,
            'support_notification.html': """
                <h2>New Support Request</h2>
                <p><strong>From:</strong> {{ sender }}</p>
                <p><strong>Category:</strong> {{ category }}</p>
                <p><strong>Message:</strong></p>
                {{ message }}
            """,
            'new_analysis_request.html': """
                <h2>New Analysis Request</h2>
                <p><strong>From:</strong> {{ sender }}</p>
                <p><strong>Priority:</strong> {{ priority }}</p>
                <p><strong>Details:</strong></p>
                {{ details }}
            """
        }
        
        for name, content in templates.items():
            template_file = template_dir / name
            if not template_file.exists():
                template_file.write_text(content)
                
    async def send_mail(self, to_email, subject, template_name, context=None):
        """Send an email using template"""
        if context is None:
            context = {}
            
        template = self.template_env.get_template(template_name)
        html_content = template.render(**context)
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = self.email_config['accounts'][0]['email']  # Default sender
        msg['To'] = to_email
        
        msg.attach(MIMEText(html_content, 'html'))
        
        # Connect to SMTP
        smtp = SMTP(
            hostname=self.email_config['smtp']['host'],
            port=self.email_config['smtp']['port'],
            use_tls=self.email_config['smtp']['use_tls']
        )
        
        try:
            await smtp.connect()
            await smtp.send_message(msg)
            print(f"{Fore.GREEN}✓ Email sent to {to_email}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}❌ Failed to send email: {str(e)}{Style.RESET_ALL}")
        finally:
            await smtp.quit()
            
    async def process_incoming_mail(self):
        """Process incoming emails according to workflows"""
        for account in self.email_config['accounts']:
            if account.get('auto_reply'):
                await self.check_mailbox(account)
                
    async def check_mailbox(self, account):
        """Check mailbox for new messages"""
        imap = aioimaplib.IMAP4_SSL(self.email_config['smtp']['host'])
        
        try:
            await imap.login(account['email'], self.config['email']['smtp']['password'])
            await imap.select('INBOX')
            
            # Search for unread messages
            _, message_numbers = await imap.search(None, 'UNSEEN')
            
            for num in message_numbers[0].split():
                _, msg_data = await imap.fetch(num, '(RFC822)')
                email_body = msg_data[0][1]
                
                # Process message according to workflows
                await self.process_message(email.message_from_bytes(email_body), account)
                
        finally:
            await imap.logout()
            
    async def process_message(self, msg, account):
        """Process a single message according to workflows"""
        workflow = self.workflows.get(account['email'].split('@')[0])
        if not workflow:
            return
            
        sender = email.utils.parseaddr(msg['from'])[1]
        subject = msg['subject']
        
        # Extract message content
        content = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    content = part.get_payload(decode=True).decode()
                    break
        else:
            content = msg.get_payload(decode=True).decode()
            
        # Process according to workflow
        for trigger in workflow:
            if trigger['trigger'] == 'new_email':
                for action in trigger['actions']:
                    await self.execute_action(action, {
                        'sender': sender,
                        'subject': subject,
                        'message': content,
                        'category': self.categorize_message(content)
                    })
                    
    def categorize_message(self, content):
        """Simple message categorization"""
        keywords = {
            'question': ['how', 'what', 'when', 'where', 'why', '?'],
            'feedback': ['suggest', 'improve', 'feedback', 'thanks'],
            'issue': ['error', 'problem', 'bug', 'not working', 'failed']
        }
        
        content = content.lower()
        for category, words in keywords.items():
            if any(word in content for word in words):
                return category
                
        return 'general'
        
    async def execute_action(self, action, context):
        """Execute a workflow action"""
        if action['type'] == 'auto_reply':
            await self.send_mail(
                context['sender'],
                f"Re: {context['subject']}",
                f"{action['template']}.html",
                context
            )
        elif action['type'] == 'notify':
            await self.send_mail(
                action['to'],
                f"[Quantum NFL] {action['template'].replace('_', ' ').title()}",
                f"{action['template']}.html",
                context
            )
            
    async def start(self):
        """Start the mail manager"""
        print(f"{Fore.CYAN}🎵 Starting Quantum Mail Manager...{Style.RESET_ALL}")
        
        while True:
            try:
                await self.process_incoming_mail()
                await asyncio.sleep(60)  # Check every minute
            except Exception as e:
                print(f"{Fore.RED}❌ Error in mail processing: {str(e)}{Style.RESET_ALL}")
                await asyncio.sleep(300)  # Wait 5 minutes on error

async def main():
    manager = QuantumMailManager()
    await manager.start()

if __name__ == "__main__":
    asyncio.run(main())
