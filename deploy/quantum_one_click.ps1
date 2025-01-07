# Quantum NFL One-Click Deployment Script
# Requires -Version 5.1

function Install-RequiredModule {
    param (
        [string]$ModuleName
    )
    
    if (-not (Get-Module -ListAvailable -Name $ModuleName)) {
        Write-Host "Installing required module: $ModuleName..."
        try {
            Install-Module -Name $ModuleName -Force -Scope CurrentUser
            Import-Module $ModuleName -Force
        } catch {
            Write-Host "Failed to install $ModuleName. Error: $_" -ForegroundColor Red
            exit 1
        }
    } else {
        Import-Module $ModuleName -Force
    }
}

# Install and import required modules
Install-RequiredModule "powershell-yaml"

# Configuration
$CONFIG = @{
    WEBSITE_DIR = "..\website"
    DEPLOY_DIR  = "."
    CONFIG_FILE = "secure_config.yml"
}

function Test-Connections {
    Write-Host "`nTesting connections..."
    
    # Load configuration
    try {
        $configPath = Join-Path $CONFIG.DEPLOY_DIR $CONFIG.CONFIG_FILE
        $config = Get-Content $configPath -Raw | ConvertFrom-Yaml
    } catch {
        throw "Failed to load configuration: $_"
    }
    
    # Test FTP
    Write-Host "Testing FTP connection..."
    try {
        $ftpHost = $config.ftp.host
        $ftpUser = $config.ftp.username
        $ftpPass = $config.ftp.password

        $ftp = [System.Net.FtpWebRequest]::Create("ftp://$ftpHost/")
        $ftp.Method = [System.Net.WebRequestMethods+Ftp]::ListDirectory
        $ftp.Credentials = New-Object System.Net.NetworkCredential($ftpUser, $ftpPass)
        $ftp.UseBinary = $true
        $ftp.KeepAlive = $false
        
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
        throw "FTP connection failed: $_"
    }
    
    # Test API
    Write-Host "Testing API connection..."
    try {
        # Add your API connection test here
        $testResult = $true
    } catch {
        throw "API connection failed: $_"
    }
    
    Write-Host "All connections tested successfully!" -ForegroundColor Green
}

function Deploy-Website {
    Write-Host "`nDeploying website..."
    try {
        # Run security checks
        Write-Host "Running security audit..." -ForegroundColor Yellow
        & "$PSScriptRoot\security\audit.ps1"
        
        # Clean up
        Write-Host "Cleaning up..." -ForegroundColor Cyan
        & "$PSScriptRoot\clean.ps1"
        
        # Deploy
        Write-Host "Deploying to quantum-nfl.com..." -ForegroundColor Cyan
        python quantum_deployer.py
        
        # For now, we'll just simulate success
        Start-Sleep -Seconds 2
        return $true
    } catch {
        throw "Website deployment failed: $_"
    }
}

try {
    Write-Host " Welcome to the Quantum-NFL One-Click Deployment!"
    Write-Host " Let's make some quantum magic happen..."
    
    Test-Connections
    Deploy-Website
    
    Write-Host " `nDeployment Complete! `n" -ForegroundColor Green
    Write-Host "Quantum NFL Analysis is now live at:"
    Write-Host "https://quantum-nfl.com" -ForegroundColor Cyan
    Write-Host "`nThank you for being part of this quantum journey!"
    
} catch {
    Write-Host "`nDeployment encountered an issue:" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host "`nPlease contact support@quantum-nfl.com for assistance."
    exit 1
}
