import ftplib
from colorama import init, Fore, Style
import yaml
import sys

# Set up UTF-8 encoding for Windows
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

init()  # Initialize colorama

def test_ftp():
    print(f"{Fore.CYAN}Testing FTP connection...{Style.RESET_ALL}")
    
    # Load config
    with open('secure_config.yml', 'r') as f:
        config = yaml.safe_load(f)
    
    try:
        # Connect to FTP
        print(f"{Fore.YELLOW}Connecting to {config['ftp']['host']}...{Style.RESET_ALL}")
        ftp = ftplib.FTP(config['ftp']['host'])
        ftp.login(config['ftp']['username'], config['ftp']['password'])
        
        # List directory contents
        print(f"{Fore.GREEN}Connected successfully!{Style.RESET_ALL}")
        print("\nDirectory contents:")
        files = ftp.nlst()
        for f in files[:10]:  # Show first 10 files
            print(f"  - {f}")
        
        ftp.quit()
        print(f"\n{Fore.GREEN}FTP test completed successfully!{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}FTP connection failed: {str(e)}{Style.RESET_ALL}")
        raise

if __name__ == "__main__":
    test_ftp()
