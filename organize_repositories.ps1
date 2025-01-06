# Create main directory structure
$baseDir = "D:/NFL"
$dirs = @(
    "quantum-nfl",
    "CQIL",
    "quantum-obs",
    "backup/quantum-states",
    "backup/evolution-data",
    "backup/calibration-data",
    "infrastructure"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path "$baseDir/$dir"
    Write-Host "Created directory: $dir"
}

# Move CQIL related files
Write-Host "Organizing CQIL..."
Move-Item -Path "$baseDir/CQIL/*" -Destination "$baseDir/CQIL/research/" -Force

# Organize quantum-obs
Write-Host "Organizing quantum-obs..."
Move-Item -Path "$baseDir/quantum-obs/*" -Destination "$baseDir/quantum-obs/broadcast/" -Force

# Organize backup data
Write-Host "Organizing backup data..."
Move-Item -Path "$baseDir/evolution_data/*" -Destination "$baseDir/backup/evolution-data/" -Force
Move-Item -Path "$baseDir/calibration_data/*" -Destination "$baseDir/backup/calibration-data/" -Force

# Clean up quantum-nfl for release
Write-Host "Cleaning quantum-nfl for release..."
$cleanupPaths = @(
    "temporal",
    "test_greg_directory.py",
    ".pytest_cache",
    "__pycache__",
    "*.pyc"
)

foreach ($path in $cleanupPaths) {
    Remove-Item -Path "$baseDir/quantum-nfl/$path" -Recurse -Force
}

Write-Host "Organization complete! Ready for:"
Write-Host "1. GitHub push"
Write-Host "2. Repository setup"
Write-Host "3. 🍺 Celebration"
