# NFL Quantum Teams Usage Guide

## Basic Usage

### 1. Running Predictions
```python
from src.quantum.run_predictions import NFLPredictor

predictor = NFLPredictor()
predictions = predictor.predict_game("PACKERS", "BEARS")
print(predictions.win_probability)
```

### 2. Analyzing Rivalries
```python
from src.quantum.rivalry_resonance import NFLRivalries

rivalries = NFLRivalries()
packers_bears = rivalries.analyze_rivalry("PACKERS", "BEARS")
print(packers_bears.intensity)
```

### 3. Playoff Analysis
```python
from src.quantum.playoff_amplification import PlayoffAmplifier

amplifier = PlayoffAmplifier()
playoff_power = amplifier.calculate_power("PACKERS", round="Divisional")
print(playoff_power)
```

## Advanced Features

### 1. Historical Echo Analysis
```python
from src.quantum.historical_echoes import NFLHistory

history = NFLHistory()
echo = history.calculate_echo("PACKERS", years=5)
print(echo.resonance)
```

### 2. Team Combinations
```python
from src.quantum.team_combinations import NFLCombinations

combos = NFLCombinations()
special_combo = combos.find_combination(["PACKERS", "BILLS"])
print(special_combo.power)
```

### 3. Visualization
```python
from src.visualization.team_matchups import MatchupVisualizer

viz = MatchupVisualizer()
viz.plot_matchup("PACKERS", "BEARS")
```

## Command Line Interface

### 1. Run Predictions
```bash
python -m src.quantum.run_predictions --team1 PACKERS --team2 BEARS
```

### 2. Generate Reports
```bash
python -m src.analysis.generate_report --team PACKERS --type full
```

### 3. Update Data
```bash
python -m src.core.update_data --source nfl_api
```

## Configuration

### 1. Environment Variables
```bash
NFL_DATA_DIR=/path/to/data
NFL_ENV=production
NFL_LOG_LEVEL=INFO
```

### 2. Config File
```yaml
# config.yaml
data:
  source: nfl_api
  cache_time: 3600
analysis:
  history_years: 5
  confidence_threshold: 0.8
```

## Error Handling

### 1. Data Errors
```python
try:
    predictions = predictor.predict_game("INVALID", "TEAM")
except TeamNotFoundError as e:
    print(f"Error: {e}")
```

### 2. Analysis Errors
```python
try:
    power = amplifier.calculate_power("PACKERS", "Invalid Round")
except ValueError as e:
    print(f"Invalid input: {e}")
```

## Performance Tips

1. Use caching for frequent calculations
2. Batch process historical data
3. Enable parallel processing for heavy computations
4. Monitor memory usage for large datasets
