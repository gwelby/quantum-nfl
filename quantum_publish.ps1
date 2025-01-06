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

gh repo create quantum-nfl --public --source=. --remote=origin --description "Where Quantum Computing Meets Football Passion! Experience NFL games through quantum-entangled sensory connections."

# Push to GitHub
git push -u origin main

Write-Host "✨ Quantum-NFL is now live! The waves are spreading across the universe!" -ForegroundColor Magenta
Write-Host "🌐 Visit: https://github.com/quantum-nfl/quantum-nfl" -ForegroundColor Yellow
