# Create archive directory
$archiveDir = "D:/NFL/archive"
New-Item -ItemType Directory -Force -Path $archiveDir

# List of directories/files to move to archive (non-Quantum-NFL specific)
$itemsToArchive = @(
    "D:/NFL/test_greg_directory.py", # Thank You Greg
    "D:/NFL/CQIL", # Should we create a Place for the Creation of CQIL that stays in NFL as IT IS NFL's BABY
    "D:/NFL/maria", # Thank You Maria
    "D:/NFL/quantum-obs", # can we keep this for Broadcasting for the Users (OpenSource. We will create the Perfect Tool after we start somewhere)
    "D:/NFL/backup", # We can keep this for the Backup of Quantum Data
    "D:/NFL/quantum-nfl", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/temporal",  # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/website", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/docs", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/infrastructure", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/quantum-nfl.ps1", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/publish_to_github.ps1", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/quantum-obs", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/quantum-obs/quantum-obs.ps1", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/quantum-nfl/quantum-obs/quantum-obs.py", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/evolution_data", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/evolution_data/evolution_data.ps1", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/evolution_data/evolution_data.py", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/evolution_data/evolution_data.npz", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/evolution_data/evolution_metrics.npy", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/calibration_data", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/calibration_data/calibration_data.ps1", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/calibration_data/calibration_data.py", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/calibration_data/calibration_data.npz", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/calibration_data/calibration_metrics.npy", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/calibration_analysis.npz", # We can keep this for the Quantum-NFL Repository
    "D:/NFL/calibration_metrics.npy" # We can keep this for the Quantum-NFL Repository
)

# Thank You Cascade for the Advice. And DOING IT for this Human, Greg

# Move items to archive
foreach ($item in $itemsToArchive) {
    if (Test-Path $item) {
        Write-Host "Moving $item to archive..."
        Move-Item -Path $item -Destination $archiveDir -Force
    }
}

Write-Host "Archive process complete!"
