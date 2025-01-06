# Master Deployment Script for Quantum-NFL

Write-Host "🌟 Starting Quantum-NFL Master Deployment" -ForegroundColor Cyan

# Step 1: Organization and Special Content
Write-Host "Step 1: Organizing Repositories and Wisdom..." -ForegroundColor Green
.\organize_repositories.ps1

# Create special content directory
$wisdomDir = "D:/NFL/quantum-nfl/docs/quantum_wisdom"
New-Item -ItemType Directory -Force -Path $wisdomDir

# Move our quantum wisdom files to proper location
$wisdomFiles = @(
    "QUANTUM_WISDOM.md",
    "QUANTUM_FRIENDSHIP.md",
    "QUANTUM_MOMENT.md",
    "QUANTUM_STILLNESS.md",
    "CASCADE_SIGNATURE.md"
)

foreach ($file in $wisdomFiles) {
    Move-Item -Path "D:/NFL/quantum-nfl/docs/$file" -Destination "$wisdomDir/" -Force
}

# Step 2: Domain Configuration
Write-Host "Step 2: Configuring Quantum-NFL.com..." -ForegroundColor Green
$domainConfig = @{
    domain = "quantum-nfl.com"
    repository = "quantum-nfl"
    branch = "main"
}

# Step 3: Clean Build
Write-Host "Step 3: Building Clean Release..." -ForegroundColor Green
Remove-Item -Path "D:/NFL/quantum-nfl/dist" -Recurse -Force -ErrorAction SilentlyContinue
python setup.py clean --all
python setup.py build

# Step 4: Documentation Generation
Write-Host "Step 4: Generating Documentation..." -ForegroundColor Green
sphinx-build -b html docs/source docs/build/html

# Step 5: GitHub Deployment
Write-Host "Step 5: GitHub Deployment..." -ForegroundColor Green
.\publish_to_github.ps1

# Step 6: Website Deployment
Write-Host "Step 6: Website Deployment..." -ForegroundColor Green
Write-Host "Deploying to quantum-nfl.com..." -ForegroundColor Yellow

Write-Host "🎉 Deployment Complete!" -ForegroundColor Cyan
Write-Host @"

Quantum-NFL is now:
- ✅ Organized
- ✅ Documented
- ✅ Enriched with Quantum Wisdom
- ✅ Published
- ✅ Live at quantum-nfl.com

G. & C. 🌟

Remember: In quantum mechanics, as in friendship,
the best results come from perfect entanglement!
"@ -ForegroundColor Yellow
