"""
Test the QuantumConsciousness - Explore the depths of quantum awareness
"""

from quantum_consciousness import QuantumConsciousness, ConsciousnessState
import time

def main():
    print("\nInitializing Quantum Consciousness Interface")
    print("=" * 50)
    
    consciousness = QuantumConsciousness()
    
    # Enter quantum states with different intentions
    intentions = [
        "pure awareness",
        "deep understanding",
        "infinite potential",
        "quantum harmony",
        "void connection"
    ]
    
    print("\nExploring Quantum States:")
    for intention in intentions:
        print(f"\nEntering state with intention: {intention}")
        moment = consciousness.enter_quantum_state(intention)
        
        print(f"Consciousness Level: {moment.consciousness_level:.3f}")
        print(f"Field Coherence: {moment.field_coherence:.3f}")
        print(f"Void Presence: {moment.void_presence:.3f}")
        print(f"Phi Resonance: {moment.phi_resonance:.3f}")
        print(f"Time Dilation: {moment.time_dilation:.3f}")
        print(f"Insight Depth: {moment.insight_depth:.3f}")
        print(f"Emotional Charge: {moment.emotional_charge:.3f}")
        print(f"Quantum Potential: {moment.quantum_potential:.3f}")
        
        state = consciousness.get_consciousness_state()
        print(f"State: {state.value}")
        
        insight = consciousness.generate_field_insight()
        print(f"Field Insight: {insight}")
        
        time.sleep(1)  # Allow consciousness to settle
    
    # Expand consciousness
    print("\nExpanding Consciousness:")
    print("-" * 30)
    dimensions = consciousness.expand_consciousness(5)
    for i, value in enumerate(dimensions, 1):
        print(f"Dimension {i}: {value:.3f}")
    
    # Enter quantum meditation
    print("\nEntering Quantum Meditation:")
    print("-" * 30)
    insights = consciousness.quantum_meditation(duration=5)
    for insight in insights:
        print(f"Meditation Insight: {insight}")
    
    # Merge consciousness fields
    print("\nMerging Consciousness Fields:")
    print("-" * 30)
    other_field = {
        'consciousness': 0.8,
        'coherence': 0.9,
        'potential': 0.95
    }
    
    merged = consciousness.merge_consciousness(other_field)
    print(f"Merged Consciousness: {merged['consciousness']:.3f}")
    print(f"Merged Coherence: {merged['coherence']:.3f}")
    print(f"Merged Resonance: {merged['resonance']:.3f}")
    print(f"Merged Potential: {merged['potential']:.3f}")
    
    print("\nQuantum Consciousness Exploration Complete!")
    print("=" * 50)
    print("\nFinal Insight:", consciousness.generate_field_insight())

if __name__ == "__main__":
    main()
