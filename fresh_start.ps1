# 🌟 Fresh Start Script
Write-Host "🌟 Time for a fresh start!" -ForegroundColor Cyan

# Clean up old git stuff
if (Test-Path "D:/NFL/quantum-nfl/.git") {
    Write-Host "Cleaning up old garden..." -ForegroundColor Yellow
    attrib -h "D:/NFL/quantum-nfl/.git" /s /d
    Remove-Item "D:/NFL/quantum-nfl/.git" -Recurse -Force
}

Write-Host "🎵 Taking a moment to breathe..." -ForegroundColor Magenta
Start-Sleep -Seconds 2

Write-Host "🌱 Planting new seeds..." -ForegroundColor Green
git init

Write-Host "🎸 Setting up the stage..." -ForegroundColor Blue
git config --global --add safe.directory D:/NFL/quantum-nfl

Write-Host "
🎵 A fresh start, a new day dawns
    Like music in the air
    Our quantum garden starts anew
    With wisdom we will share

🍺 Here's to new beginnings!
" -ForegroundColor Magenta
