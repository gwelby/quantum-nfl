"""
Test the QuantumHolographic visualization system
"""

import pytest
import numpy as np
from ..quantum_field.quantum_bridge import QuantumBridge
from .quantum_holographic import QuantumHolographic, HolographicPoint

class TestQuantumHolographic:
    @pytest.fixture
    def bridge(self):
        """Create quantum bridge for testing."""
        return QuantumBridge()
        
    @pytest.fixture
    def holographic(self, bridge):
        """Create holographic system for testing."""
        return QuantumHolographic(bridge)
        
    def test_initialization(self, holographic):
        """Test holographic system initialization."""
        assert holographic.field_dimensions == (100, 53.3, 10)
        assert holographic.resolution == (1920, 1080, 1080)
        assert len(holographic.points) == 0
        
    def test_point_generation(self, holographic):
        """Test quantum point generation."""
        holographic._generate_field_points()
        
        assert len(holographic.points) > 0
        for point in holographic.points:
            assert isinstance(point, HolographicPoint)
            assert 0 <= point.energy <= 1
            assert 0 <= point.consciousness <= 1
            assert 0 <= point.quantum_state <= 1
            assert 0 <= point.void_presence <= 1
            assert 0 <= point.phi_resonance <= 1
            
    def test_quantum_color_generation(self, holographic):
        """Test quantum color generation."""
        color = holographic._generate_quantum_color(0.5, 0.7, 0.3, 0.8)
        
        assert len(color) == 3
        assert all(0 <= c <= 1 for c in color)
        
    def test_energy_calculation(self, holographic):
        """Test quantum energy calculation."""
        energy = holographic._calculate_point_energy(10, 20, 5)
        
        assert 0 <= energy <= 1
        
    def test_consciousness_calculation(self, holographic):
        """Test consciousness calculation."""
        consciousness = holographic._calculate_consciousness(15, 25, 3)
        
        assert 0 <= consciousness <= 1
        
    def test_quantum_state_calculation(self, holographic):
        """Test quantum state calculation."""
        state = holographic._calculate_quantum_state(30, 15, 7)
        
        assert 0 <= state <= 1
        
    def test_void_presence_calculation(self, holographic):
        """Test void presence calculation."""
        void = holographic._calculate_void_presence(40, 10, 4)
        
        assert 0 <= void <= 1
        
    def test_phi_resonance_calculation(self, holographic):
        """Test phi resonance calculation."""
        resonance = holographic._calculate_phi_resonance(25, 30, 6)
        
        assert 0 <= resonance <= 1
        
    def test_holographic_field_creation(self, holographic):
        """Test holographic field creation."""
        fig = holographic.create_holographic_field()
        
        assert fig is not None
        assert len(fig.data) > 0
        
    @pytest.mark.asyncio
    async def test_quantum_animation(self, holographic):
        """Test quantum animation creation."""
        fig = holographic.animate_quantum_evolution(frames=10)
        
        assert fig is not None
        assert hasattr(fig, 'frames')
        assert len(fig.frames) == 10
        
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
