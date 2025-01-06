"""
NFL Quantum State Analyzer using IBM Quantum

This module provides tools for analyzing quantum states of NFL teams
and games using IBM Quantum computers.
"""

from typing import Dict, List, Tuple
import numpy as np
from qiskit import QuantumCircuit, execute
from qiskit.quantum_info import state_fidelity, Statevector
from qiskit.visualization import plot_state_city

class NFLQuantumAnalyzer:
    def __init__(self, circuits):
        """Initialize NFL Quantum Analyzer.
        
        Args:
            circuits: NFLQuantumCircuits instance
        """
        self.circuits = circuits
        
    def analyze_team_state(self, team_metrics: Dict[str, float]) -> Dict[str, float]:
        """Analyze a team's quantum state.
        
        Args:
            team_metrics (Dict[str, float]): Team performance metrics
            
        Returns:
            Dict[str, float]: Quantum state analysis results
        """
        # Create and execute circuit
        circuit = self.circuits.create_team_state_circuit(team_metrics)
        statevector = Statevector.from_instruction(circuit)
        
        # Analyze quantum properties
        entanglement = self._calculate_entanglement(statevector)
        coherence = self._calculate_coherence(statevector)
        
        return {
            'entanglement': entanglement,
            'coherence': coherence,
            'quantum_advantage': (entanglement + coherence) / 2
        }
    
    def _calculate_entanglement(self, statevector) -> float:
        """Calculate the entanglement measure of the quantum state.
        
        Args:
            statevector: Quantum state vector
            
        Returns:
            float: Entanglement measure between 0 and 1
        """
        # Calculate reduced density matrix
        dims = [2, 2, 2, 2, 2]  # 5 qubits
        reduced = statevector.partial_trace([0, 1])
        
        # Calculate von Neumann entropy
        eigenvals = np.real(np.linalg.eigvals(reduced.data))
        eigenvals = eigenvals[eigenvals > 1e-10]
        entropy = -np.sum(eigenvals * np.log2(eigenvals))
        
        return min(entropy, 1.0)
    
    def _calculate_coherence(self, statevector) -> float:
        """Calculate the quantum coherence of the state.
        
        Args:
            statevector: Quantum state vector
            
        Returns:
            float: Coherence measure between 0 and 1
        """
        # Calculate l1-norm coherence
        rho = statevector.to_operator().data
        coherence = np.sum(np.abs(rho)) - np.trace(np.abs(rho))
        
        return min(coherence, 1.0)
    
    def analyze_matchup(self, home_metrics: Dict[str, float], 
                       away_metrics: Dict[str, float]) -> Dict[str, float]:
        """Analyze quantum properties of a team matchup.
        
        Args:
            home_metrics (Dict[str, float]): Home team metrics
            away_metrics (Dict[str, float]): Away team metrics
            
        Returns:
            Dict[str, float]: Matchup analysis results
        """
        # Get win probabilities
        game_results = self.circuits.simulate_game(home_metrics, away_metrics)
        
        # Analyze quantum interference
        home_state = Statevector.from_instruction(
            self.circuits.create_team_state_circuit(home_metrics)
        )
        away_state = Statevector.from_instruction(
            self.circuits.create_team_state_circuit(away_metrics)
        )
        
        # Calculate state fidelity
        fidelity = state_fidelity(home_state, away_state)
        
        return {
            'win_probability': game_results['home_win_prob'],
            'quantum_interference': fidelity,
            'matchup_entanglement': self._calculate_matchup_entanglement(
                home_state, away_state
            )
        }
    
    def _calculate_matchup_entanglement(self, state1, state2) -> float:
        """Calculate entanglement between two team states.
        
        Args:
            state1: First team's quantum state
            state2: Second team's quantum state
            
        Returns:
            float: Entanglement measure between the teams
        """
        # Calculate composite system entropy
        composite = state1.tensor(state2)
        entropy = self._calculate_entanglement(composite)
        
        return entropy
    
    def visualize_team_state(self, team_metrics: Dict[str, float]) -> None:
        """Visualize a team's quantum state.
        
        Args:
            team_metrics (Dict[str, float]): Team performance metrics
        """
        circuit = self.circuits.create_team_state_circuit(team_metrics)
        state = Statevector.from_instruction(circuit)
        
        # Create city plot visualization
        fig = plot_state_city(state)
        return fig
