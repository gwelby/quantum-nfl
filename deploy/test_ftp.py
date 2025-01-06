import ftplib
import yaml
from pathlib import Path

def test_ftp():
    # Load config
    config_path = Path(__file__).parent / 'secure_config.yml'
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Get FTP credentials
    host = config['ftp']['host']
    user = config['ftp']['username']
    passwd = config['ftp']['password']
    
    print(f"Connecting to {host}...")
    
    try:
        # Connect to FTP
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=passwd)
        
        print("Connected successfully!")
        
        # Print welcome message
        print(f"\nServer response: {ftp.getwelcome()}")
        
        # List contents of root directory
        print("\nRoot directory contents:")
        ftp.dir()
        
        # Try to navigate to the website directory
        print("\nNavigating to /public_html/quantum-nfl.com...")
        try:
            ftp.cwd('/public_html/quantum-nfl.com')
            print("Directory exists!")
            print("\nWebsite directory contents:")
            ftp.dir()
        except Exception as e:
            print(f"Could not access directory: {str(e)}")
            print("Creating directory...")
            try:
                ftp.mkd('/public_html/quantum-nfl.com')
                print("Directory created successfully!")
            except:
                print("Failed to create directory")
        
        ftp.quit()
        return True
        
    except Exception as e:
        print(f"FTP Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_ftp()
