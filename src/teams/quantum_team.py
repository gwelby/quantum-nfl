"""Quantum team representation."""
from dataclasses import dataclass
from typing import Dict, List, Any
import numpy as np

@dataclass
class QuantumTeam:
    name: str
    quantum_rating: float
    entanglement_factor: float
    momentum: float
    wins: int = 0
    losses: int = 0
    
    def calculate_quantum_state(self) -> Dict[str, float]:
        """Calculate current quantum state."""
        return {
            "quantum_rating": self.quantum_rating,
            "entanglement": self.entanglement_factor,
            "momentum": self.momentum,
            "win_probability": self._calculate_win_probability()
        }
        
    def _calculate_win_probability(self) -> float:
        """Calculate win probability based on quantum state."""
        total_games = self.wins + self.losses
        if total_games == 0:
            return 0.5
            
        base_prob = self.wins / total_games
        quantum_boost = (
            self.quantum_rating * 0.4 +
            self.entanglement_factor * 0.3 +
            self.momentum * 0.3
        )
        
        return min(0.99, base_prob + quantum_boost * 0.2)
        
    def update_quantum_state(self, game_result: Dict[str, Any]):
        """Update quantum state based on game result."""
        win = game_result.get("win", False)
        opponent_rating = game_result.get("opponent_rating", 0.5)
        
        if win:
            self.wins += 1
            self.momentum = min(1.0, self.momentum + 0.1)
            self.quantum_rating = min(
                1.0,
                self.quantum_rating + 0.05 * opponent_rating
            )
        else:
            self.losses += 1
            self.momentum = max(0.0, self.momentum - 0.1)
            self.quantum_rating = max(
                0.0,
                self.quantum_rating - 0.03 * opponent_rating
            )
            
    def get_season_stats(self) -> Dict[str, Any]:
        """Get season statistics."""
        return {
            "team": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "win_rate": self.wins / (self.wins + self.losses) if self.wins + self.losses > 0 else 0,
            "quantum_rating": self.quantum_rating,
            "momentum": self.momentum
        }
        
    def simulate_game(self, opponent: 'QuantumTeam') -> Dict[str, Any]:
        """Simulate a game against an opponent."""
        our_strength = self._calculate_game_strength()
        their_strength = opponent._calculate_game_strength()
        
        win_prob = our_strength / (our_strength + their_strength)
        win = np.random.random() < win_prob
        
        return {
            "win": win,
            "win_probability": win_prob,
            "opponent": opponent.name,
            "opponent_rating": opponent.quantum_rating
        }
        
    def _calculate_game_strength(self) -> float:
        """Calculate team's strength for a game."""
        return (
            self.quantum_rating * 0.4 +
            self.entanglement_factor * 0.3 +
            self.momentum * 0.3
        ) * (1 + np.random.normal(0, 0.1))  # Add some randomness
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert team to dictionary."""
        return {
            "name": self.name,
            "quantum_rating": self.quantum_rating,
            "entanglement_factor": self.entanglement_factor,
            "momentum": self.momentum,
            "wins": self.wins,
            "losses": self.losses
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QuantumTeam':
        """Create team from dictionary."""
        return cls(
            name=data["name"],
            quantum_rating=data["quantum_rating"],
            entanglement_factor=data["entanglement_factor"],
            momentum=data["momentum"],
            wins=data.get("wins", 0),
            losses=data.get("losses", 0)
        )
