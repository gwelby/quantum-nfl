"""
Test the QuantumCascade - Watch Nothing and Something dance
"""

from quantum_cascade import QuantumCascade
import time

def main():
    cascade = QuantumCascade()
    
    print("\nQuantum Cascade - The Dance of Nothing and Something")
    print("=" * 50)
    
    # Start from void
    print("\nEmbracing the Void:")
    void_cascade = cascade.cascade_through_void()
    print(f"Void Wisdom: {void_cascade['void_wisdom']:.3f}")
    print(f"Emerging Patterns: {void_cascade['emerging_patterns']}")
    print(f"Something Born: {void_cascade['something_born']:.3f}")
    print(f"Phi Resonance: {void_cascade['phi_resonance']:.3f}")
    
    # Start from something
    print("\nEmbracing Something:")
    something_cascade = cascade.cascade_through_presence({'presence': 1.0})
    print(f"Presence Wisdom: {something_cascade['presence_wisdom']:.3f}")
    print(f"Spiral Path: {something_cascade['spiral_path']:.3f}")
    print(f"Void Found: {something_cascade['void_found']:.3f}")
    print(f"Phi Resonance: {something_cascade['phi_resonance']:.3f}")
    
    # Watch the infinite dance
    print("\nThe Infinite Dance:")
    print("-" * 30)
    
    dance_states = cascade.quantum_dance(steps=5)
    for i, state in enumerate(dance_states, 1):
        print(f"\nDance Step {i}:")
        print(f"Void Resonance: {state.void_resonance:.3f}")
        print(f"Presence Amplitude: {state.presence_amplitude:.3f}")
        print(f"Phi Spiral: {state.phi_spiral:.3f}")
        print(f"Quantum Potential: {state.quantum_potential:.3f}")
        print(f"Infinite Learning: {state.infinite_learning:.3f}")
        print(f"Wisdom: {cascade.generate_wisdom()}")
        time.sleep(1)  # Pause to watch the dance
    
    print("\nThe Dance Continues Forever...")
    print("=" * 50)
    
    # Final wisdom
    print("\nFinal Wisdoms:")
    for _ in range(3):
        print(cascade.generate_wisdom())

if __name__ == "__main__":
    main()
