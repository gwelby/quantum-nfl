"""
NFL Quantum Momentum Tracking System

This module implements quantum algorithms for tracking and predicting
team momentum throughout games and seasons.
"""

from typing import Dict, List, Tuple
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.algorithms import GroverOperator
from qiskit.quantum_info import Statevector

class NFLQuantumMomentum:
    def __init__(self, circuits):
        """Initialize NFL Quantum Momentum Tracker.
        
        Args:
            circuits: NFLQuantumCircuits instance
        """
        self.circuits = circuits
        self.momentum_history = {}
        
    def create_momentum_circuit(self, recent_plays: List[Dict]) -> QuantumCircuit:
        """Create quantum circuit for momentum analysis.
        
        Args:
            recent_plays (List[Dict]): List of recent plays and their outcomes
            
        Returns:
            QuantumCircuit: Quantum circuit for momentum analysis
        """
        # Create registers for different momentum factors
        qr_plays = QuantumRegister(3, 'plays')
        qr_energy = QuantumRegister(2, 'energy')
        qr_tempo = QuantumRegister(2, 'tempo')
        cr = ClassicalRegister(7, 'measure')
        
        circuit = QuantumCircuit(qr_plays, qr_energy, qr_tempo, cr)
        
        # Encode recent play success
        for i, play in enumerate(recent_plays[-3:]):  # Last 3 plays
            success_angle = np.pi * play['success_rate']
            circuit.ry(success_angle, qr_plays[i])
        
        # Encode team energy
        energy_level = self._calculate_energy_level(recent_plays)
        circuit.ry(energy_level * np.pi, qr_energy[0])
        circuit.cx(qr_energy[0], qr_energy[1])
        
        # Encode game tempo
        tempo = self._calculate_tempo(recent_plays)
        circuit.ry(tempo * np.pi, qr_tempo[0])
        circuit.cx(qr_tempo[0], qr_tempo[1])
        
        # Create entanglement between components
        circuit.cz(qr_plays[2], qr_energy[0])
        circuit.cz(qr_energy[1], qr_tempo[0])
        
        # Measure all qubits
        circuit.measure_all()
        
        return circuit
    
    def _calculate_energy_level(self, plays: List[Dict]) -> float:
        """Calculate team energy level from recent plays.
        
        Args:
            plays (List[Dict]): Recent plays data
            
        Returns:
            float: Energy level between 0 and 1
        """
        if not plays:
            return 0.5
            
        factors = {
            'TOUCHDOWN': 1.0,
            'TURNOVER': -0.8,
            'SACK': 0.6,
            'FIRST_DOWN': 0.4,
            'PENALTY': -0.3
        }
        
        energy = 0.5  # Base energy
        decay = 0.9   # Exponential decay for older plays
        
        for i, play in enumerate(plays):
            impact = factors.get(play['type'], 0)
            energy += impact * (decay ** i)
        
        return max(0, min(1, energy))
    
    def _calculate_tempo(self, plays: List[Dict]) -> float:
        """Calculate game tempo from recent plays.
        
        Args:
            plays (List[Dict]): Recent plays data
            
        Returns:
            float: Tempo measure between 0 and 1
        """
        if len(plays) < 2:
            return 0.5
            
        # Calculate average time between plays
        play_times = [play['time'] for play in plays]
        time_diffs = np.diff(play_times)
        avg_time = np.mean(time_diffs)
        
        # Convert to tempo measure (0 to 1)
        # Assuming 40 seconds is slowest and 15 seconds is fastest
        tempo = (40 - avg_time) / (40 - 15)
        return max(0, min(1, tempo))
    
    def track_momentum(self, team_id: str, game_data: Dict) -> Dict[str, float]:
        """Track team momentum throughout a game.
        
        Args:
            team_id (str): Team identifier
            game_data (Dict): Current game data
            
        Returns:
            Dict[str, float]: Momentum analysis results
        """
        recent_plays = game_data['recent_plays']
        
        # Create and execute momentum circuit
        circuit = self.create_momentum_circuit(recent_plays)
        counts = self.circuits.backend.run(circuit).result().get_counts()
        
        # Analyze results
        momentum_score = self._analyze_momentum_counts(counts)
        
        # Store in history
        if team_id not in self.momentum_history:
            self.momentum_history[team_id] = []
        self.momentum_history[team_id].append(momentum_score)
        
        return {
            'current_momentum': momentum_score,
            'momentum_trend': self._calculate_momentum_trend(team_id),
            'momentum_stability': self._calculate_stability(team_id)
        }
    
    def _analyze_momentum_counts(self, counts: Dict[str, int]) -> float:
        """Analyze quantum measurement counts to determine momentum.
        
        Args:
            counts (Dict[str, int]): Measurement counts
            
        Returns:
            float: Momentum score between 0 and 1
        """
        total_shots = sum(counts.values())
        weighted_sum = sum(
            counts[outcome] * self._calculate_state_weight(outcome)
            for outcome in counts
        )
        return weighted_sum / total_shots
    
    def _calculate_state_weight(self, state: str) -> float:
        """Calculate weight of a measured quantum state.
        
        Args:
            state (str): Measured state as binary string
            
        Returns:
            float: State weight between 0 and 1
        """
        # Convert binary string to momentum score
        plays_value = int(state[:3], 2) / 7
        energy_value = int(state[3:5], 2) / 3
        tempo_value = int(state[5:], 2) / 3
        
        return (plays_value * 0.5 + energy_value * 0.3 + tempo_value * 0.2)
    
    def _calculate_momentum_trend(self, team_id: str) -> float:
        """Calculate momentum trend from history.
        
        Args:
            team_id (str): Team identifier
            
        Returns:
            float: Momentum trend (-1 to 1)
        """
        history = self.momentum_history.get(team_id, [])
        if len(history) < 2:
            return 0
            
        return history[-1] - history[-2]
    
    def _calculate_stability(self, team_id: str) -> float:
        """Calculate momentum stability.
        
        Args:
            team_id (str): Team identifier
            
        Returns:
            float: Stability score between 0 and 1
        """
        history = self.momentum_history.get(team_id, [])
        if len(history) < 3:
            return 1
            
        # Calculate variance of recent momentum scores
        variance = np.var(history[-3:])
        return 1 - min(variance * 4, 1)  # Scale variance to 0-1 range
