import ftplib
import yaml
from colorama import init, Fore, Style
import sys
import os
from datetime import datetime

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

# Create a test HTML file
test_file = "quantum_test.html"
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Quantum NFL - Test Page</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #1a1a1a;
            color: #ffffff;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #2d2d2d;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }}
        h1 {{
            color: #00ff00;
            text-align: center;
        }}
        .timestamp {{
            text-align: center;
            color: #888;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Quantum NFL Test Page</h1>
        <p>If you can see this page, the FTP deployment is working!</p>
        <p>This is a test upload from the quantum deployment system.</p>
        <p class="timestamp">Uploaded on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>
"""

# Write test file
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print_status("Created test HTML file")

# Load FTP config
with open('secure_config.yml', 'r') as f:
    config = yaml.safe_load(f)

try:
    # Connect to FTP
    print_status("Connecting to FTP...")
    ftp = ftplib.FTP(config['ftp']['host'])
    ftp.login(config['ftp']['username'], config['ftp']['password'])
    
    # Navigate to quantum-nfl.com directory
    print_status("Navigating to quantum-nfl.com directory...")
    try:
        ftp.cwd('/public_html/quantum-nfl.com')
        print_status("Successfully changed to quantum-nfl.com directory!", "success")
        
        # Show current directory contents
        print_status("\nDirectory contents:")
        files = []
        ftp.dir(files.append)
        for item in files:
            print_status(f"  {item}")
            
    except Exception as e:
        print_status(f"Error accessing quantum-nfl.com directory: {str(e)}", "error")
        raise e
    
    # Upload file
    print_status("\nUploading test file...")
    with open(test_file, 'rb') as f:
        ftp.storbinary(f'STOR {test_file}', f)
    
    print_status("Test file uploaded successfully!", "success")
    print_status(f"\nTest your site at: http://quantum-nfl.com/{test_file}", "success")
    
    # Cleanup
    ftp.quit()
    os.remove(test_file)
    print_status("Local test file cleaned up", "info")
    
except Exception as e:
    print_status(f"Error: {str(e)}", "error")
