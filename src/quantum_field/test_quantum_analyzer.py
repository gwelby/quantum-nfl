"""
Test module for QuantumFieldAnalyzer
"""

import numpy as np
from quantum_field_analyzer import QuantumFieldAnalyzer, FieldDimension

def create_sample_game_data():
    """Create sample game data for testing."""
    return {
        'offense_stats': np.random.random(10),
        'defense_stats': np.random.random(10),
        'special_teams_stats': np.random.random(10),
        'quarter_scores': [7, 10, 3, 14],
        'drive_times': np.random.random(8) * 180,  # Drive times in seconds
        'play_durations': np.random.random(50) * 40,  # Play durations in seconds
        'play_types': np.random.choice(['run', 'pass', 'special'], 50),
        'formations': np.random.choice(['spread', 'i-form', 'shotgun'], 50),
        'personnel_groupings': np.random.choice(['11', '12', '21'], 50),
        'efficiency_stats': np.random.random(10),
        'success_rates': np.random.random(10),
        'epa_values': np.random.normal(0, 1, 50)
    }

def main():
    # Create analyzer
    analyzer = QuantumFieldAnalyzer()
    
    # Generate sample data
    game_data = create_sample_game_data()
    
    # Analyze patterns
    patterns = analyzer.analyze_field_patterns(game_data)
    
    # Print results
    print("\nQuantum Field Analysis Results:")
    print("=" * 50)
    
    for dim, pattern in patterns.items():
        print(f"\nDimension: {dim}")
        print(f"Intensity: {pattern.intensity:.3f}")
        print(f"Phase: {pattern.phase:.3f}")
        print(f"Coherence: {pattern.coherence:.3f}")
        print(f"Phi Resonance: {pattern.phi_resonance:.3f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
