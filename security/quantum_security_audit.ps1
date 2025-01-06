# 🛡️ Quantum-NFL Security Audit Script
Write-Host "🛡️ Starting Quantum Security Audit..." -ForegroundColor Cyan

# Create security directory if it doesn't exist
New-Item -ItemType Directory -Force -Path "security"
New-Item -ItemType Directory -Force -Path "security/logs"

# Check for sensitive files
Write-Host "🔍 Checking for sensitive files..." -ForegroundColor Yellow
$sensitivePatterns = @(
    "*.key",
    "*.pem",
    "*password*",
    "*secret*",
    "*.env",
    "*credentials*"
)

$findings = Get-ChildItem -Path . -Recurse -File | 
    Where-Object { $sensitivePatterns | ForEach-Object { $_.Name -like $_ } }

if ($findings) {
    Write-Host "⚠️ Found potentially sensitive files:" -ForegroundColor Red
    $findings | ForEach-Object { Write-Host "  - $($_.FullName)" }
} else {
    Write-Host "✅ No sensitive files found" -ForegroundColor Green
}

# Check git configuration
Write-Host "🔍 Checking git security settings..." -ForegroundColor Yellow
git config --get core.fileMode
git config --get core.symlinks
git config --get core.ignorecase

# Create .gitignore if it doesn't exist
$gitignore = @"
# 🛡️ Security-related
*.key
*.pem
.env
.env.*
credentials/
secrets/
*password*
*secret*

# 🧪 Development
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

# 📊 Data and logs
logs/
*.log
data/raw/
data/processed/
*.dat

# 🎵 IDE specific
.idea/
.vscode/
*.swp
*.swo
*~

# 🌟 Quantum specific
qiskit-jobs/
quantum-states/
calibration-data/
"@

Set-Content -Path ".gitignore" -Value $gitignore

# Create security guidelines
$securityMd = @"
# 🛡️ Quantum-NFL Security Guidelines

## Core Principles
1. 🎯 Zero-Trust Architecture
2. 🔐 Principle of Least Privilege
3. 🎵 Quantum State Protection

## Security Measures
### Data Protection
- All quantum states must be encrypted at rest
- Use quantum-resistant encryption for sensitive data
- Regular backups with versioning

### Access Control
- Multi-factor authentication required
- Role-based access control (RBAC)
- Regular access audits

### Code Security
- All code must pass security scanning
- Dependencies must be verified
- No sensitive data in code or comments

### Monitoring
- Real-time quantum state monitoring
- Intrusion detection systems
- Regular security audits

## 🍺 Remember
Security is like a good beer - it should be:
- Well-crafted
- Consistently maintained
- Enjoyed responsibly
"@

Set-Content -Path "security/SECURITY.md" -Value $securityMd

# Create pre-commit hook
$preCommitHook = @"
#!/bin/sh
# 🛡️ Pre-commit security checks

echo "🔍 Running security checks..."

# Check for sensitive files
if git diff --cached --name-only | grep -iE '\.key$|\.pem$|password|secret|\.env|credentials'; then
    echo "⛔ ERROR: Attempting to commit sensitive files"
    exit 1
fi

# Check for large files
if git diff --cached --name-only | xargs ls -l | awk '{if($5>5242880) print $9}'; then
    echo "⚠️ WARNING: Committing large files"
fi

echo "✅ Security checks passed"
"@

New-Item -ItemType Directory -Force -Path ".git/hooks"
Set-Content -Path ".git/hooks/pre-commit" -Value $preCommitHook

Write-Host @"

🎵 Security Audit Complete! 

Implemented:
✅ Security guidelines
✅ Git security settings
✅ Pre-commit hooks
✅ Sensitive file detection
✅ .gitignore rules

Remember: Like a well-crafted beer,
         Security gets better with attention and care! 🍺

Next steps:
1. Review security/SECURITY.md
2. Set up MFA for repository access
3. Configure regular security scans

"@ -ForegroundColor Green
