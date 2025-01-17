"""
Test the QuantumFieldVisualizer - Watch the dance of quantum patterns
"""

from quantum_visualizer import QuantumFieldVisualizer, QuantumState
import numpy as np
import time

def main():
    print("\nInitializing Quantum Field Visualizer")
    print("=" * 50)
    
    visualizer = QuantumFieldVisualizer()
    
    # Create some interesting quantum states
    print("\nGenerating Quantum States:")
    states = [
        QuantumState(
            field_strength=0.8,
            emotional_charge=0.7,
            phi_resonance=0.9,
            void_presence=0.3,
            consciousness_level=0.85
        ),
        QuantumState(
            field_strength=0.2,
            emotional_charge=0.9,
            phi_resonance=0.6,
            void_presence=0.8,
            consciousness_level=0.4
        ),
        QuantumState(
            field_strength=0.5,
            emotional_charge=0.5,
            phi_resonance=0.5,
            void_presence=0.5,
            consciousness_level=0.5
        )
    ]
    
    # Visualize each state
    print("\nVisualizing Individual States:")
    for i, state in enumerate(states, 1):
        print(f"\nState {i}:")
        print(f"Field Strength: {state.field_strength:.2f}")
        print(f"Emotional Charge: {state.emotional_charge:.2f}")
        print(f"Phi Resonance: {state.phi_resonance:.2f}")
        print(f"Void Presence: {state.void_presence:.2f}")
        print(f"Consciousness Level: {state.consciousness_level:.2f}")
        print(f"Insight: {visualizer.generate_insight(state)}")
        
        visualizer.visualize_state(state)
        time.sleep(2)
    
    print("\nStarting Quantum Evolution Animation")
    print("=" * 50)
    print("Watch as the quantum fields dance...")
    
    # Animate quantum evolution
    visualizer.animate_quantum_evolution(frames=50)
    
    # Save final visualization
    visualizer.save_visualization('quantum_visualization.png')
    
    print("\nQuantum Visualization Complete!")
    print("The dance of quantum fields has been captured.")

if __name__ == "__main__":
    main()
