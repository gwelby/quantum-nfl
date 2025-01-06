import asyncio
import logging
from pathlib import Path
from cloudflare import Cloudflare
from cryptography.fernet import Fernet
import yaml
import os
from datetime import datetime
from tqdm import tqdm
import ftplib
import requests
from colorama import init, Fore, Style
import sys

# Fix Windows encoding
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

init()

class QuantumDeployer:
    def __init__(self):
        self.setup_logging()
        self.load_config()
        self.setup_apis()
        
    def setup_logging(self):
        """Configure logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('QuantumDeployer')
        
    def load_config(self):
        """Load and decrypt configuration"""
        config_path = Path(__file__).parent / 'secure_config.yml'
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
            
        # Create secrets directory if not exists
        secrets_dir = Path(__file__).parent / 'secrets'
        secrets_dir.mkdir(exist_ok=True)
            
        # Generate encryption key if not exists
        key_path = secrets_dir / '.key'
        if not key_path.exists():
            key = Fernet.generate_key()
            key_path.write_bytes(key)
        
        self.fernet = Fernet(key_path.read_bytes())
        
    def setup_apis(self):
        """Initialize APIs"""
        try:
            # Initialize Cloudflare
            self.configure_cloudflare()
            
        except Exception as e:
            print(f"{Fore.RED}* API Setup Error: {str(e)}{Style.RESET_ALL}")
            raise
            
    async def configure_cloudflare(self):
        """Configure Cloudflare settings"""
        print(f"{Fore.CYAN}* Configuring Cloudflare...{Style.RESET_ALL}")
        
        try:
            # Initialize Cloudflare with API token
            cf = Cloudflare(token=self.config['cloudflare']['api_token'])
            
            # Get zone ID if not set
            if not self.config['cloudflare']['zone_id']:
                zones = cf.zones.get(params={'name': self.config['cloudflare']['domain']})
                if zones:
                    self.config['cloudflare']['zone_id'] = zones[0]['id']
                    
            zone_id = self.config['cloudflare']['zone_id']
            
            # Configure DNS
            print("* Setting up DNS records...")
            dns_records = [
                {
                    'name': '@',
                    'type': 'A',
                    'content': '198.54.115.144',
                    'proxied': True
                },
                {
                    'name': 'www',
                    'type': 'CNAME',
                    'content': 'quantum-nfl.com',
                    'proxied': True
                },
                {
                    'name': 'mail',
                    'type': 'CNAME',
                    'content': 'mx.zoho.com',
                    'proxied': False
                }
            ]
            
            # MX records for email
            mx_records = [
                {'name': '@', 'type': 'MX', 'priority': 10, 'content': 'mx.zoho.com'},
                {'name': '@', 'type': 'MX', 'priority': 20, 'content': 'mx2.zoho.com'}
            ]
            
            # TXT records for email verification
            txt_records = [
                {'name': '@', 'type': 'TXT', 'content': 'v=spf1 include:zoho.com ~all'}
            ]
            
            # Add/update all records
            existing_records = cf.zones.dns_records.get(zone_id)
            for record in dns_records + mx_records + txt_records:
                record_exists = False
                for existing in existing_records:
                    if existing['type'] == record['type'] and existing['name'] == record['name']:
                        cf.zones.dns_records.put(zone_id, existing['id'], data=record)
                        record_exists = True
                        break
                if not record_exists:
                    cf.zones.dns_records.post(zone_id, data=record)
            
            # Configure SSL
            print("* Configuring SSL...")
            cf.zones.settings.ssl.patch(zone_id, value='full')
            
            # Enable HTTPS
            print("* Enabling HTTPS...")
            cf.zones.settings.always_use_https.patch(zone_id, value='on')
            
            # Configure caching
            print("* Optimizing caching...")
            cf.zones.settings.cache_level.patch(zone_id, value='aggressive')
            cf.zones.settings.browser_cache_ttl.patch(zone_id, value=14400)
            
            # Enable minification
            print("* Enabling minification...")
            cf.zones.settings.minify.patch(zone_id, value={
                'css': 'on',
                'html': 'on',
                'js': 'on'
            })
            
            # Enable Brotli compression
            print("* Enabling Brotli compression...")
            cf.zones.settings.brotli.patch(zone_id, value='on')
            
            # Configure security settings
            print("* Configuring security settings...")
            cf.zones.settings.security_level.patch(zone_id, value='medium')
            cf.zones.settings.browser_check.patch(zone_id, value='on')
            cf.zones.settings.email_obfuscation.patch(zone_id, value='on')
            
            print(f"{Fore.GREEN}* Cloudflare configured successfully!{Style.RESET_ALL}")
            
        except Exception as e:
            print(f"{Fore.RED}* Cloudflare configuration error: {str(e)}{Style.RESET_ALL}")
            raise
            
    async def deploy_website(self):
        """Deploy the website"""
        try:
            print(f"{Fore.CYAN}* Starting Quantum-NFL deployment...{Style.RESET_ALL}")
            
            # 1. Create backup if needed
            if self.config.get('backup', {}).get('enabled', False):
                self.create_backup()
            
            # 2. Upload via FTP
            self.deploy_via_ftp()
            
            # 3. Update DNS settings
            await self.update_dns()
            
            print(f"{Fore.GREEN}* Deployment completed successfully!{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}* Deployment failed: {str(e)}{Style.RESET_ALL}")
            self.logger.error(f"Deployment failed: {str(e)}")
            return False
            
    def create_backup(self):
        """Create backup of current deployment"""
        print(f"{Fore.CYAN}* Creating backup...{Style.RESET_ALL}")
        # Backup implementation here
        
    def deploy_via_ftp(self):
        """Deploy files via FTP"""
        try:
            print(f"{Fore.CYAN}* Connecting to FTP...{Style.RESET_ALL}")
            ftp = ftplib.FTP(self.config['ftp']['host'])
            ftp.login(self.config['ftp']['username'], self.config['ftp']['password'])
            
            # Navigate to quantum-nfl.com directory
            print(f"{Fore.CYAN}* Navigating to site directory...{Style.RESET_ALL}")
            ftp.cwd('/public_html/quantum-nfl.com')
            
            # Upload files
            local_root = Path(self.config['deployment']['local_root'])
            for root, dirs, files in os.walk(local_root):
                for file in tqdm(files, desc="Uploading files"):
                    local_path = Path(root) / file
                    
                    # Skip certain files/directories
                    if any(skip in str(local_path) for skip in ['.git', '__pycache__', 'deploy']):
                        continue
                        
                    # Calculate relative path from local_root
                    rel_path = local_path.relative_to(local_root)
                    remote_path = str(rel_path).replace('\\', '/')
                    
                    # Create remote directories if needed
                    remote_dirs = str(rel_path.parent).split(os.sep)
                    current_dir = ''
                    for d in remote_dirs:
                        if d:
                            current_dir += f'/{d}'
                            try:
                                ftp.mkd(current_dir)
                            except:
                                pass  # Directory might already exist
                    
                    # Upload file
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f'STOR {remote_path}', f)
            
            print(f"{Fore.GREEN}* Files uploaded successfully!{Style.RESET_ALL}")
            ftp.quit()
            return True
            
        except Exception as e:
            print(f"{Fore.RED}* FTP Error: {str(e)}{Style.RESET_ALL}")
            return False
            
    async def update_dns(self):
        """Update DNS records"""
        print(f"{Fore.CYAN}* DNS updates will be configured later...{Style.RESET_ALL}")
        pass

async def main():
    deployer = QuantumDeployer()
    await deployer.deploy_website()

if __name__ == "__main__":
    asyncio.run(main())
