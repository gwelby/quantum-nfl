"""
NFL Quantum Analytics Demo

This script demonstrates the quantum circuit capabilities with real NFL team data,
focusing on the Green Bay Packers and San Francisco 49ers as example teams.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from circuits import NFLQuantumCircuits
from analyzer import NFLQuantumAnalyzer
from predictor import NFLQuantumPredictor

# Initialize quantum components
api_token = os.getenv('IBM_QUANTUM_TOKEN')  # Set your IBM Quantum token in environment variables
circuits = NFLQuantumCircuits(api_token)
analyzer = NFLQuantumAnalyzer(circuits)
predictor = NFLQuantumPredictor(circuits, analyzer)

# Team metrics based on 2024 season performance
PACKERS_METRICS = {
    'offensive_power': 0.85,  # Strong offense
    'defensive_power': 0.78,  # Above average defense
    'momentum': 0.92,        # High momentum from recent performances
}

NINERS_METRICS = {
    'offensive_power': 0.90,  # Elite offense
    'defensive_power': 0.88,  # Elite defense
    'momentum': 0.95,        # Very high momentum
}

def visualize_team_quantum_states():
    """Visualize quantum states for both teams."""
    # Create figure for side-by-side comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Visualize Packers quantum state
    packers_state = analyzer.visualize_team_state(PACKERS_METRICS)
    ax1.set_title('Green Bay Packers Quantum State')
    
    # Visualize 49ers quantum state
    niners_state = analyzer.visualize_team_state(NINERS_METRICS)
    ax2.set_title('San Francisco 49ers Quantum State')
    
    plt.tight_layout()
    plt.savefig('team_quantum_states.png')
    plt.close()

def predict_playoff_matchup():
    """Predict a playoff matchup between Packers and 49ers."""
    # Add playoff context factors
    context = {
        'home_advantage': 1.1,    # 10% home field advantage
        'weather_impact': 0.95,   # Slight weather impact
        'rest_advantage': 1.05,   # Extra rest days advantage
    }
    
    # Get prediction with quantum analysis
    prediction = predictor.predict_game_outcome(
        PACKERS_METRICS,
        NINERS_METRICS,
        context
    )
    
    # Visualize prediction results
    plt.figure(figsize=(10, 6))
    
    # Create bar chart for win probabilities
    teams = ['Packers', '49ers']
    probs = [prediction['home_win_prob'], prediction['away_win_prob']]
    colors = ['#203731', '#AA0000']  # Team colors
    
    plt.bar(teams, probs, color=colors)
    plt.title('Quantum Prediction: Packers vs 49ers')
    plt.ylabel('Win Probability')
    plt.ylim(0, 1)
    
    # Add confidence score
    plt.text(0.5, -0.1, 
            f"Prediction Confidence: {prediction['confidence_score']:.2f}",
            ha='center', transform=plt.gca().transAxes)
    
    # Add quantum factors
    factors = prediction['quantum_factors']
    info_text = (
        f"Quantum Interference: {factors['quantum_interference']:.2f}\n"
        f"Matchup Entanglement: {factors['matchup_entanglement']:.2f}"
    )
    plt.text(0.95, 0.95, info_text,
             transform=plt.gca().transAxes,
             verticalalignment='top',
             horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.savefig('playoff_prediction.png')
    plt.close()

def analyze_quantum_advantage():
    """Analyze quantum advantages for both teams."""
    packers_analysis = analyzer.analyze_team_state(PACKERS_METRICS)
    niners_analysis = analyzer.analyze_team_state(NINERS_METRICS)
    
    # Visualize quantum advantages
    plt.figure(figsize=(10, 6))
    
    metrics = ['Entanglement', 'Coherence', 'Quantum Advantage']
    packers_values = [
        packers_analysis['entanglement'],
        packers_analysis['coherence'],
        packers_analysis['quantum_advantage']
    ]
    niners_values = [
        niners_analysis['entanglement'],
        niners_analysis['coherence'],
        niners_analysis['quantum_advantage']
    ]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    plt.bar(x - width/2, packers_values, width, label='Packers', color='#203731')
    plt.bar(x + width/2, niners_values, width, label='49ers', color='#AA0000')
    
    plt.ylabel('Quantum Metrics')
    plt.title('Team Quantum Advantages')
    plt.xticks(x, metrics)
    plt.legend()
    
    plt.savefig('quantum_advantages.png')
    plt.close()

if __name__ == '__main__':
    print("Generating NFL Quantum Analytics Visualizations...")
    
    # Run all analyses
    visualize_team_quantum_states()
    predict_playoff_matchup()
    analyze_quantum_advantage()
    
    print("Analysis complete! Check the generated visualization files:"
          "\n- team_quantum_states.png"
          "\n- playoff_prediction.png"
          "\n- quantum_advantages.png")
