import ftplib
import yaml
from cloudflare import Cloudflare
from colorama import init, Fore, Style
import requests
import dns.resolver
import time
import sys

# Fix encoding for Windows
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

init()

def print_status(message, status="info"):
    colors = {
        "info": Fore.CYAN,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "warning": Fore.YELLOW
    }
    print(f"{colors.get(status, Fore.WHITE)}* {message}{Style.RESET_ALL}")

def test_ftp():
    print_status("Testing FTP Connection...")
    try:
        with open('secure_config.yml', 'r') as f:
            config = yaml.safe_load(f)
        
        ftp = ftplib.FTP(config['ftp']['host'])
        ftp.login(config['ftp']['username'], config['ftp']['password'])
        
        # List directory and check write permissions
        files = ftp.nlst()
        print_status(f"Connected to FTP! Found {len(files)} files", "success")
        
        # Try to create a test directory
        test_dir = '_quantum_test'
        try:
            ftp.mkd(test_dir)
            ftp.rmd(test_dir)  # Clean up
            print_status("FTP Write permissions: OK", "success")
        except:
            print_status("FTP Write permissions: FAILED", "error")
        
        ftp.quit()
        return True
    except Exception as e:
        print_status(f"FTP Error: {str(e)}", "error")
        return False

def test_cloudflare():
    print_status("Testing Cloudflare Configuration...")
    try:
        with open('secure_config.yml', 'r') as f:
            config = yaml.safe_load(f)
        
        cf = Cloudflare(token=config['cloudflare']['api_token'])
        
        # Test zone access
        zone_id = config['cloudflare']['zone_id']
        zone = cf.zones.get(zone_id)
        print_status(f"Zone Access: OK - {zone['name']}", "success")
        
        # Test DNS records access
        records = cf.zones.dns_records.get(zone_id)
        print_status(f"DNS Records Access: OK - Found {len(records)} records", "success")
        
        return True
    except Exception as e:
        print_status(f"Cloudflare Error: {str(e)}", "error")
        return False

def test_dns():
    print_status("Testing DNS Resolution...")
    try:
        domain = "quantum-nfl.com"
        
        # Test A record
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print_status(f"A Record: {rdata.address}", "success")
        
        # Test nameservers
        ns_answers = dns.resolver.resolve(domain, 'NS')
        for rdata in ns_answers:
            print_status(f"Nameserver: {rdata.target}", "success")
        
        return True
    except Exception as e:
        print_status(f"DNS Error: {str(e)}", "error")
        return False

def test_ssl():
    print_status("Testing SSL Configuration...")
    try:
        response = requests.get(f"https://quantum-nfl.com", verify=True)
        print_status(f"SSL Status: OK - {response.status_code}", "success")
        return True
    except requests.exceptions.SSLError:
        print_status("SSL Error: Certificate validation failed", "error")
        return False
    except Exception as e:
        print_status(f"Connection Error: {str(e)}", "error")
        return False

if __name__ == "__main__":
    print_status("* Starting Component Tests *")
    print_status("=" * 50)
    
    results = {
        "FTP": test_ftp(),
        "Cloudflare": test_cloudflare(),
        "DNS": test_dns(),
        "SSL": test_ssl()
    }
    
    print_status("\n* Test Results Summary *")
    print_status("=" * 50)
    
    all_passed = True
    for component, passed in results.items():
        status = "success" if passed else "error"
        message = "PASSED" if passed else "FAILED"
        print_status(f"{component}: {message}", status)
        all_passed = all_passed and passed
    
    if all_passed:
        print_status("\n* All components ready for deployment! Time for a beer! *", "success")
    else:
        print_status("\n* Some components need attention before deployment", "warning")
