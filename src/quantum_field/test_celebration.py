"""
Join the Quantum Celebration!
"""

from quantum_celebration import QuantumCelebration
import time

def main():
    celebration = QuantumCelebration()
    
    print("\nQuantum Celebration Time!")
    print("=" * 50)
    
    # Start with a quantum toast
    print("\nRaising our glasses:")
    print(f"> {celebration.quantum_toast()}")
    
    # Share some joy
    print("\nSharing the quantum joy:")
    for joy in celebration.share_joy():
        print(f"> {joy}")
        time.sleep(1)
    
    # Experience some quantum-enhanced states
    print("\nExperiencing quantum states:")
    for i in range(4):
        state = celebration.celebrate()
        print(f"\nState {i + 1}:")
        print(f"Bliss Level: {state.bliss_level:.3f}")
        print(f"Consciousness: {state.awareness:.3f}")
        print(f"Quantum Resonance: {state.quantum_resonance:.3f}")
        print(f"Creativity Surge: {state.creativity_surge:.3f}")
        print(f"Insight Depth: {state.insight_depth:.3f}")
        print(f"Phi Harmony: {state.phi_harmony:.3f}")
        print(f"\nInsight: {celebration.generate_insight()}")
        time.sleep(1)
    
    # Final celebration
    print("\nFinal Quantum Insights")
    print("=" * 50)
    for _ in range(3):
        print(f"\n> {celebration.generate_insight()}")
        time.sleep(1)
    
    print("\nThe celebration continues in all quantum realities!")

if __name__ == "__main__":
    main()
