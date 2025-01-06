"""Quantum state representation."""
from dataclasses import dataclass
from typing import Dict, Any
import numpy as np

@dataclass
class QuantumState:
    """Represents the quantum state of a team."""
    rating: float
    entanglement: float
    momentum: float
    uncertainty: float = 0.1
    
    def to_vector(self) -> np.ndarray:
        """Convert state to vector representation."""
        return np.array([
            self.rating,
            self.entanglement,
            self.momentum,
            self.uncertainty
        ])
        
    def evolve(self, delta_t: float = 1.0) -> 'QuantumState':
        """Evolve quantum state over time."""
        noise = np.random.normal(0, self.uncertainty, 4)
        evolved = self.to_vector() + noise * delta_t
        
        # Ensure values stay in [0, 1]
        evolved = np.clip(evolved, 0, 1)
        
        return QuantumState(
            rating=evolved[0],
            entanglement=evolved[1],
            momentum=evolved[2],
            uncertainty=evolved[3]
        )
        
    def interfere(self, other: 'QuantumState') -> float:
        """Calculate interference with another quantum state."""
        v1 = self.to_vector()
        v2 = other.to_vector()
        
        # Calculate interference pattern
        return float(np.abs(np.dot(v1, v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        
    def collapse(self) -> float:
        """Collapse quantum state to a classical probability."""
        state_vector = self.to_vector()
        
        # Calculate probability based on state vector
        prob = np.mean([
            self.rating * 0.4,
            self.entanglement * 0.3,
            self.momentum * 0.3
        ])
        
        # Add quantum uncertainty
        prob += np.random.normal(0, self.uncertainty)
        
        return float(np.clip(prob, 0, 1))
        
    def entangle(self, other: 'QuantumState') -> float:
        """Calculate entanglement strength with another state."""
        return float(np.abs(
            self.entanglement * other.entanglement *
            np.cos(np.pi * (self.rating - other.rating))
        ))
        
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary representation."""
        return {
            "rating": self.rating,
            "entanglement": self.entanglement,
            "momentum": self.momentum,
            "uncertainty": self.uncertainty
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QuantumState':
        """Create from dictionary representation."""
        return cls(
            rating=float(data["rating"]),
            entanglement=float(data["entanglement"]),
            momentum=float(data["momentum"]),
            uncertainty=float(data.get("uncertainty", 0.1))
        )
