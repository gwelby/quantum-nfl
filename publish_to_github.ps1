# PowerShell script to publish Quantum-NFL to GitHub
Write-Host "Publishing Quantum-NFL to GitHub..." -ForegroundColor Green

# Set repository details
$REPO_NAME = "Quantum-NFL"
$GITHUB_USERNAME = "GWelby"
$REPO_DESCRIPTION = "Advanced Quantum Computing Analysis for NFL Teams and Games"

# Initialize git repository
Write-Host "Initializing git repository..." -ForegroundColor Yellow
git init

# Configure git
Write-Host "Configuring git..." -ForegroundColor Yellow
git config user.name $GITHUB_USERNAME
git config user.email "your.email@example.com"  # Replace with your email

# Add all files
Write-Host "Adding files..." -ForegroundColor Yellow
git add .

# Initial commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Quantum-NFL Project Launch

Key Features:
- Team Quantum Fields
- Neural Evolution System
- Reality Manipulation
- Quantum Harmonics
- Advanced NFL Analysis"

# Create .gitignore if it doesn't exist
if (-not (Test-Path .gitignore)) {
    Write-Host "Creating .gitignore..." -ForegroundColor Yellow
    Copy-Item templates/.gitignore .gitignore
}

# Create GitHub repository
Write-Host "To create repository on GitHub:" -ForegroundColor Cyan
Write-Host "1. Go to https://github.com/new" -ForegroundColor White
Write-Host "2. Repository name: $REPO_NAME" -ForegroundColor White
Write-Host "3. Description: $REPO_DESCRIPTION" -ForegroundColor White
Write-Host "4. Choose 'Public'" -ForegroundColor White
Write-Host "5. Click 'Create repository'" -ForegroundColor White
Write-Host "6. Copy the repository URL" -ForegroundColor White

# Prompt for repository URL
$REPO_URL = Read-Host "Enter the GitHub repository URL"

# Add remote and push
Write-Host "Adding remote and pushing code..." -ForegroundColor Yellow
git remote add origin $REPO_URL
git branch -M main
git push -u origin main

Write-Host "Done! Your code is now published to GitHub!" -ForegroundColor Green
Write-Host "Repository URL: $REPO_URL" -ForegroundColor Cyan

# Next steps
Write-Host "`nNext steps:" -ForegroundColor Magenta
Write-Host "1. Set up branch protection rules in GitHub repository settings" -ForegroundColor White
Write-Host "2. Enable GitHub Pages in repository settings" -ForegroundColor White
Write-Host "3. Configure GitHub Actions in repository settings" -ForegroundColor White
Write-Host "4. Add repository topics: quantum-computing, nfl, sports-analytics, python" -ForegroundColor White
Write-Host "5. Set up project boards for feature tracking" -ForegroundColor White

# Open browser to repository
Write-Host "`nOpening repository in browser..." -ForegroundColor Yellow
Start-Process $REPO_URL
