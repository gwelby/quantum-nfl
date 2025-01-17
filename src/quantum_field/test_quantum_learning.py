"""
Test the QuantumHumanLearner with simulated NFL play data
"""

import pandas as pd
import numpy as np
from quantum_human_learner import QuantumHumanLearner
import logging

logging.basicConfig(level=logging.INFO)

def generate_sample_plays(n_plays: int = 1000) -> pd.DataFrame:
    """Generate sample NFL play data for testing."""
    plays = []
    
    for _ in range(n_plays):
        play = {
            'down': np.random.randint(1, 5),
            'distance': np.random.randint(1, 11),
            'field_position': np.random.randint(1, 100),
            'score_differential': np.random.randint(-21, 22),
            'time_remaining': np.random.randint(0, 3600),
            'timeouts_remaining': np.random.randint(0, 4),
            'formation': np.random.choice(['spread', 'i-form', 'shotgun', 'pistol']),
            'play_type': np.random.choice(['run', 'pass', 'option', 'screen']),
            'yards_gained': np.random.normal(4, 3),  # Mean 4 yards, std 3
            'expected_yards': 4.0,  # League average
            'success': np.random.random() > 0.5,  # Random success
            'emotional_momentum': np.random.random()  # Random emotional state
        }
        plays.append(play)
    
    return pd.DataFrame(plays)

def main():
    print("\nQuantum-Human Learning Analysis")
    print("=" * 50)
    
    # Create learner
    learner = QuantumHumanLearner()
    
    # Generate sample data
    print("\nGenerating sample NFL play data...")
    plays_df = generate_sample_plays()
    print(f"Generated {len(plays_df)} plays")
    
    # Train models
    print("\nTraining quantum-human models...")
    learner.learn_from_historical_data(plays_df)
    
    # Analyze some interesting plays
    print("\nAnalyzing specific play situations:")
    
    # Critical 4th down
    critical_play = {
        'down': 4,
        'distance': 2,
        'field_position': 45,
        'score_differential': -4,
        'time_remaining': 120,
        'timeouts_remaining': 2,
        'formation': 'shotgun',
        'play_type': 'option',
        'yards_gained': 5,
        'expected_yards': 2
    }
    
    print("\n1. Critical 4th Down Analysis:")
    analysis = learner.analyze_play_effectiveness(critical_play)
    print(f"Creativity Score: {analysis['creativity_score']:.3f}")
    print(f"Quantum Score: {analysis['quantum_score']:.3f}")
    print(f"Human Score: {analysis['human_score']:.3f}")
    print(f"Overall Harmony: {analysis['harmony_score']:.3f}")
    print("\nInsights:")
    for insight in analysis['insights']:
        print(f"- {insight}")
    
    # Unexpected big play
    big_play = {
        'down': 2,
        'distance': 8,
        'field_position': 25,
        'score_differential': 0,
        'time_remaining': 1800,
        'timeouts_remaining': 3,
        'formation': 'spread',
        'play_type': 'pass',
        'yards_gained': 75,
        'expected_yards': 6
    }
    
    print("\n2. Unexpected Big Play Analysis:")
    analysis = learner.analyze_play_effectiveness(big_play)
    print(f"Creativity Score: {analysis['creativity_score']:.3f}")
    print(f"Quantum Score: {analysis['quantum_score']:.3f}")
    print(f"Human Score: {analysis['human_score']:.3f}")
    print(f"Overall Harmony: {analysis['harmony_score']:.3f}")
    print("\nInsights:")
    for insight in analysis['insights']:
        print(f"- {insight}")
    
    # Save models
    print("\nSaving trained models...")
    learner.save_models()
    
    print("\nQuantum-Human Learning complete!")
    print("Models are now ready for real-time analysis of NFL plays.")
    print("\nNext steps:")
    print("1. Connect to real NFL play data feed")
    print("2. Implement real-time learning updates")
    print("3. Develop visualization of quantum-human patterns")
    print("4. Create predictive play-calling system")

if __name__ == "__main__":
    main()
