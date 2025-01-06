# Run this as administrator
Write-Host "Initializing Quantum-NFL Repository..." -ForegroundColor Cyan

# Create necessary directories
$dirs = @(
    "docs/source/_static",
    "docs/source/_templates",
    "src/quantum/fields",
    "src/quantum/analysis",
    "src/teams/patterns"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path $dir
    Write-Host "Created directory: $dir"
}

# Initialize git with elevated permissions
Start-Process powershell -Verb RunAs -ArgumentList @"
    cd 'D:/NFL/quantum-nfl'
    git init
    git config --global --add safe.directory D:/NFL/quantum-nfl
    git add .
    git commit -m 'Initial commit: Quantum-NFL Project Launch'

    # Create GitHub repository
    Write-Host 'Please create a new repository on GitHub:'
    Write-Host '1. Go to https://github.com/gwelby/quantum-nfl/new' # do we do a Cascade or Quantum-NFL or ??
    Write-Host '2. Name: Quantum-NFL'
    Write-Host '3. Description: Advanced Quantum Computing Analysis for NFL Teams and Games'
    Write-Host '4. Make it Public'
    Write-Host '5. Create repository'

    # Wait for user to create repository
    $repoUrl = Read-Host 'Enter the GitHub repository URL'

    git remote add origin $repoUrl
    git branch -M main
    git push -u origin main
"@

Write-Host "Repository initialization complete!" -ForegroundColor Green
