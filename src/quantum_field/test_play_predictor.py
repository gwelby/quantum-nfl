"""
Test the QuantumPlayPredictor with simulated game situations
"""

from quantum_play_predictor import QuantumPlayPredictor
import logging
import time

logging.basicConfig(level=logging.INFO)

def simulate_game_drive():
    """Simulate a game drive with quantum-human play prediction."""
    predictor = QuantumPlayPredictor()
    
    print("\nSimulating Game Drive with Quantum-Human Fusion")
    print("=" * 50)
    
    # Initial game state
    game_state = {
        'score_differential': -7,
        'time_remaining': 300,  # 5 minutes
        'timeouts_remaining': 2,
        'down': 1,
        'distance': 10,
        'field_position': 25
    }
    
    # Simulate plays
    for play_num in range(1, 9):  # Simulate 8 plays
        print(f"\nPlay {play_num}:")
        print(f"Down: {game_state['down']}, "
              f"Distance: {game_state['distance']}, "
              f"Field Position: {game_state['field_position']}")
        
        # Get play prediction
        prediction = predictor.predict_next_play(game_state)
        
        print(f"\nQuantum-Human Prediction:")
        print(f"Play Type: {prediction.play_type}")
        print(f"Formation: {prediction.formation}")
        print(f"Success Probability: {prediction.success_probability:.3f}")
        print(f"Expected Yards: {prediction.yards_expected:.1f}")
        print(f"Creativity Factor: {prediction.creativity_factor:.3f}")
        print(f"Emotional Boost: {prediction.emotional_boost:.3f}")
        
        # Simulate play result
        yards_gained = prediction.yards_expected * (0.5 + predictor.current_emotional_state.momentum)
        success = yards_gained >= game_state['distance']
        
        # Update emotional momentum
        play_result = {
            'yards_gained': yards_gained,
            'expected_yards': prediction.yards_expected,
            'success': success
        }
        predictor.track_emotional_momentum(play_result)
        
        print(f"\nPlay Result:")
        print(f"Yards Gained: {yards_gained:.1f}")
        print(f"Success: {success}")
        print(f"Team Momentum: {predictor.current_emotional_state.momentum:.3f}")
        print(f"Team Confidence: {predictor.current_emotional_state.confidence:.3f}")
        
        # Update game state
        game_state['field_position'] += yards_gained
        if success:
            game_state['down'] = 1
            game_state['distance'] = 10
        else:
            game_state['down'] += 1
            game_state['distance'] -= yards_gained
        
        game_state['time_remaining'] -= 35  # Average play time
        
        # Check for touchdown
        if game_state['field_position'] >= 100:
            print("\nTOUCHDOWN!")
            print("Perfect quantum-human harmony achieved!")
            break
            
        # Check for turnover on downs
        if game_state['down'] > 4:
            print("\nTurnover on downs.")
            print("Time to realign our quantum-human harmony.")
            break
        
        time.sleep(1)  # Pause for readability

def main():
    try:
        simulate_game_drive()
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    except Exception as e:
        print(f"Error in simulation: {e}")
    finally:
        print("\nQuantum-Human Play Prediction complete!")

if __name__ == "__main__":
    main()
