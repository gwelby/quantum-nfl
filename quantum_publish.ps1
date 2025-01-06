Write-Host "🌟 Publishing Quantum-NFL to the world!" -ForegroundColor Cyan

# Check for GitHub CLI and install if needed
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "Installing GitHub CLI..." -ForegroundColor Yellow
    winget install --id GitHub.cli
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Set up Git configuration
git config --global user.name "Quantum NFL"
git config --global user.email "quantum@nfl.com"

# Create .gitignore if it doesn't exist
if (-not (Test-Path .gitignore)) {
    @"
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.idea/
.vscode/
secure_credentials.yml
"@ | Out-File .gitignore -Encoding utf8
}

# Initialize and stage files
git init
git add .
git commit -m "🌟 Initial release of Quantum-NFL - Where Quantum Computing Meets Football Passion!"

# Ensure we're on main branch
git branch -M main

# Create GitHub repository using GitHub CLI (gh)
Write-Host "🚀 Creating GitHub repository..." -ForegroundColor Green
gh auth status 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Please authenticate with GitHub..." -ForegroundColor Yellow
    gh auth login
}

# Get GitHub username
$githubUser = gh api user --jq '.login'
Write-Host "Publishing as $githubUser..." -ForegroundColor Cyan

# Try to create repo, if it fails, just set the remote
gh repo create "$githubUser/quantum-nfl" --public --source=. --remote=origin --description "Where Quantum Computing Meets Football Passion! Experience NFL games through quantum-entangled sensory connections." 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Repository exists, setting remote..." -ForegroundColor Yellow
    git remote remove origin 2>&1 | Out-Null
    git remote add origin "https://github.com/$githubUser/quantum-nfl.git"
}

# Push to GitHub
git push -u origin main --force

Write-Host "✨ Quantum-NFL is now live! The waves are spreading across the universe!" -ForegroundColor Magenta
Write-Host "🌐 Visit: https://github.com/$githubUser/quantum-nfl" -ForegroundColor Yellow
