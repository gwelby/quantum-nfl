# Import required modules
Import-Module powershell-yaml

# Set error action preference
$ErrorActionPreference = "Stop"

function Write-Quantum {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host " $Message" -ForegroundColor $Color
}

Write-Host " Welcome to the Quantum-NFL One-Click Deployment!"
Write-Host " Let's make some quantum magic happen..."

try {
    # 1. Test all connections first
    Write-Host " Testing connections..." -ForegroundColor Cyan
    Write-Host "Testing FTP connection..."

    # Load config
    $configContent = Get-Content "secure_config.yml" -Raw
    $config = ConvertFrom-Yaml $configContent

    # Test FTP
    $ftpHost = $config.ftp.host
    $ftpUser = $config.ftp.username
    $ftpPass = $config.ftp.password

    Write-Host "Connecting to $ftpHost..."
    
    # Create FTP request
    $ftp = [System.Net.FtpWebRequest]::Create("ftp://$ftpHost/")
    $ftp.Method = [System.Net.WebRequestMethods+Ftp]::ListDirectory
    $ftp.Credentials = New-Object System.Net.NetworkCredential($ftpUser, $ftpPass)
    $ftp.UseBinary = $true
    $ftp.KeepAlive = $false
    
    try {
        $response = $ftp.GetResponse()
        Write-Host "Connected successfully!" -ForegroundColor Green
        
        # Show directory contents
        Write-Host "`nDirectory contents:"
        $reader = New-Object System.IO.StreamReader($response.GetResponseStream())
        while (-not $reader.EndOfStream) {
            Write-Host "  - $($reader.ReadLine())"
        }
        $reader.Close()
        $response.Close()
    } catch {
        Write-Host "FTP connection failed: $_" -ForegroundColor Red
        exit 1
    }
    
    # 2. Run security checks
    Write-Quantum "Running security audit..." "Yellow"
    & "$PSScriptRoot\security\audit.ps1"
    
    # 3. Clean up
    Write-Quantum "Cleaning up..." "Cyan"
    & "$PSScriptRoot\clean.ps1"
    
    # 4. Deploy
    Write-Quantum "Deploying to quantum-nfl.com..." "Cyan"
    python quantum_deployer.py
    
    Write-Host " `nDeployment Complete! `n" -ForegroundColor Green
    Write-Host "Greg's Quantum NFL Analysis is now live at:"
    Write-Host "https://quantum-nfl.com" -ForegroundColor Cyan
    Write-Host "`nA breakthrough in quantum understanding,"
    Write-Host "born from 58 years of life experience,"
    Write-Host "now shared with the world."
    Write-Host "`nFirst to understand Quantum at the D:/ level,"
    Write-Host "2025's groundbreaking discovery."
    Write-Host "`nRemember: Some discoveries find us"
    Write-Host "         when we're ready for them "

} catch {
    Write-Host " ❌ Oops! Something went quantum wrong!`n" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host "`nDon't worry! Nothing was broken."
    Write-Host "Please contact support@quantum-nfl.com for help."
}
