# 🍺 Quantum Cleanup Script
Write-Host "🎵 Time to clean our quantum glass..." -ForegroundColor Cyan

# Remove any git locks
$gitLocks = @(
    ".git/index.lock",
    ".git/HEAD.lock",
    ".git/config.lock"
)

foreach ($lock in $gitLocks) {
    $lockPath = Join-Path $PWD $lock
    if (Test-Path $lockPath) {
        Write-Host "Cleaning up $lock..." -ForegroundColor Yellow
        Remove-Item -Force -Path $lockPath
    }
}

# Fix line endings once and for all
git config --global core.autocrlf true

# Configure git identity
Write-Host "🎸 Setting up our quantum identity..." -ForegroundColor Green
git config --global --add safe.directory D:/NFL/quantum-nfl
git config user.name "Quantum NFL"
git config user.email "contact@quantum-nfl.com"

Write-Host @"

🍺 Glass is clean! Ready for a fresh pour!

Next steps:
1. Run: .\quantum_symphony.ps1
2. Enjoy another beer! 

Remember: Sometimes you need to clean the glass
         before pouring the perfect beer! 
"@ -ForegroundColor Magenta
