"""
Test module for QuantumStrategicAdvisor
"""

import numpy as np
from quantum_strategic_advisor import QuantumStrategicAdvisor

def create_sample_game_state():
    """Create sample game state for testing."""
    return {
        'offense_stats': np.random.random(10) * 100,  # Yards gained etc.
        'defense_stats': np.random.random(10) * 100,
        'special_teams_stats': np.random.random(10) * 50,
        'quarter_scores': [7, 10, 3, 14],
        'drive_times': np.random.random(8) * 180,  # Drive times in seconds
        'play_durations': np.random.random(50) * 40,  # Play durations in seconds
        'play_types': np.random.choice(['run', 'pass', 'special'], 50),
        'formations': np.random.choice(['spread', 'i-form', 'shotgun'], 50),
        'personnel_groupings': np.random.choice(['11', '12', '21'], 50),
        'efficiency_stats': np.random.random(10),
        'success_rates': np.random.random(10),
        'epa_values': np.random.normal(0, 1, 50),
        'game_clock': 1800,  # 30 minutes remaining
        'score_differential': -7,  # Down by 7
        'field_position': 65,  # Own 35 yard line
        'down': 2,
        'distance': 8,
        'timeouts_remaining': 2
    }

def main():
    # Create advisor
    advisor = QuantumStrategicAdvisor()
    
    # Generate sample game state
    game_state = create_sample_game_state()
    
    # Get recommendations
    recommendations = advisor.analyze_game_state(game_state)
    
    # Print results
    print("\nQuantum Strategic Recommendations:")
    print("=" * 50)
    
    for i, rec in enumerate(recommendations, 1):
        print(f"\nRecommendation {i}:")
        print(f"Confidence: {rec.confidence:.3f}")
        print(f"Phi Alignment: {rec.phi_alignment:.3f}")
        print(f"Play Type: {rec.play_type}")
        print(f"Formation: {rec.formation}")
        print(f"Personnel: {rec.personnel}")
        print(f"Optimal Timing: {rec.timing:.1f} seconds")
        print(f"Expected Success Rate: {rec.expected_success_rate:.3f}")
        print(f"Quantum Resonance: {rec.quantum_resonance:.3f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
