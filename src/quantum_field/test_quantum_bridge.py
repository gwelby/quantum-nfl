"""
Test the QuantumBridge - Prove the quantum-consciousness connection
"""

import pytest
import asyncio
import numpy as np
from quantum_bridge import QuantumBridge, NFLQuantumState, QuantumState

class TestQuantumBridge:
    @pytest.fixture
    def bridge(self):
        """Create a quantum bridge for testing."""
        return QuantumBridge()
        
    @pytest.mark.asyncio
    async def test_initialization(self, bridge):
        """Test quantum bridge initialization."""
        await bridge.initialize_quantum_system()
        
        # Verify field dimensions
        assert bridge.field_matrix.shape == (32, 32, 32)
        assert len(bridge.consciousness_field) > 0
        assert len(bridge.void_states) == 32
        
    def test_quantum_states(self, bridge):
        """Test quantum state calculations."""
        # Test team data
        team_data = {
            'momentum': 0.8,
            'vector': [1, 0, 1],
            'energy': 0.9
        }
        
        # Calculate quantum state
        quantum_state = bridge._calculate_quantum_state(team_data)
        
        # Verify quantum properties
        assert 0 <= quantum_state['potential'] <= 1
        assert 0 <= quantum_state['field_strength'] <= 1
        assert 0 <= quantum_state['coherence'] <= 1
        
    def test_consciousness_integration(self, bridge):
        """Test consciousness state calculations."""
        team_data = {
            'awareness': 0.7,
            'focus': 0.8,
            'presence': 0.9
        }
        
        # Calculate consciousness state
        consciousness = bridge._calculate_consciousness_state(team_data)
        
        # Verify consciousness properties
        assert 0 <= consciousness['level'] <= 1
        assert 0 <= consciousness['awareness'] <= bridge.phi
        assert 0 <= consciousness['connection'] <= 1
        
    def test_void_presence(self, bridge):
        """Test void state calculations."""
        team_id = "team_1"
        
        # Initialize void states
        bridge._initialize_void_states()
        
        # Calculate void presence
        void_presence = bridge._calculate_void_presence(team_id)
        
        # Verify void properties
        assert 0 <= void_presence <= 1
        
    def test_phi_resonance(self, bridge):
        """Test golden ratio resonance."""
        team_id = "team_1"
        
        # Calculate phi resonance
        resonance = bridge._calculate_phi_resonance(team_id)
        
        # Verify phi properties
        assert 0 <= resonance <= 1
        assert abs(resonance - (bridge.phi % 1)) <= 1
        
    def test_play_prediction(self, bridge):
        """Test quantum play prediction."""
        # Create test game state
        game_state = {
            'offense': 'team_1',
            'defense': 'team_2',
            'down': 1,
            'distance': 10,
            'field_position': 30
        }
        
        # Create test quantum states
        bridge.teams['team_1'] = NFLQuantumState(
            team_id='team_1',
            quantum_potential=0.8,
            consciousness_level=0.7,
            emotional_charge=0.6,
            momentum_vector=np.array([1, 0, 1]),
            field_strength=0.9,
            entanglement_pairs=['team_3'],
            void_presence=0.3,
            phi_resonance=0.618
        )
        
        bridge.teams['team_2'] = NFLQuantumState(
            team_id='team_2',
            quantum_potential=0.7,
            consciousness_level=0.8,
            emotional_charge=0.5,
            momentum_vector=np.array([0, 1, 1]),
            field_strength=0.85,
            entanglement_pairs=['team_4'],
            void_presence=0.4,
            phi_resonance=0.618
        )
        
        # Get prediction
        prediction = bridge.predict_play(game_state)
        
        # Verify prediction structure
        assert 'prediction' in prediction
        assert 'factors' in prediction
        assert 'play_type' in prediction['prediction']
        assert 'confidence' in prediction['prediction']
        assert 'consciousness_alignment' in prediction['prediction']
        assert 'quantum_potential' in prediction['prediction']
        
        # Verify prediction values
        assert 0 <= prediction['prediction']['confidence'] <= 1
        assert 0 <= prediction['prediction']['consciousness_alignment'] <= 1
        assert 0 <= prediction['prediction']['quantum_potential'] <= 1
        
    @pytest.mark.asyncio
    async def test_nfl_data_processing(self, bridge):
        """Test NFL data processing."""
        # Initialize system
        await bridge.initialize_quantum_system()
        
        # Test data
        test_data = {
            'game_id': 'game_1',
            'play_type': 'run',
            'teams': {
                'team_1': {
                    'momentum': 0.8,
                    'vector': [1, 0, 1],
                    'energy': 0.9
                },
                'team_2': {
                    'momentum': 0.6,
                    'vector': [0, 1, 1],
                    'energy': 0.85
                }
            }
        }
        
        # Process data
        await bridge._process_nfl_data(test_data)
        
        # Verify team states
        assert 'team_1' in bridge.teams
        assert 'team_2' in bridge.teams
        assert isinstance(bridge.teams['team_1'], NFLQuantumState)
        assert isinstance(bridge.teams['team_2'], NFLQuantumState)
        
    def test_quantum_consciousness_harmony(self, bridge):
        """Test quantum-consciousness harmony."""
        # Get consciousness insights
        team1 = NFLQuantumState(
            team_id='team_1',
            quantum_potential=0.8,
            consciousness_level=0.7,
            emotional_charge=0.6,
            momentum_vector=np.array([1, 0, 1]),
            field_strength=0.9,
            entanglement_pairs=['team_3'],
            void_presence=0.3,
            phi_resonance=0.618
        )
        
        team2 = NFLQuantumState(
            team_id='team_2',
            quantum_potential=0.7,
            consciousness_level=0.8,
            emotional_charge=0.5,
            momentum_vector=np.array([0, 1, 1]),
            field_strength=0.85,
            entanglement_pairs=['team_4'],
            void_presence=0.4,
            phi_resonance=0.618
        )
        
        insights = bridge._get_consciousness_insights(team1, team2)
        
        # Verify insights
        assert 'momentum' in insights
        assert 'awareness' in insights
        assert 'potential' in insights
        assert -1 <= insights['momentum'] <= 1
        assert 0 <= insights['awareness'] <= 1
        assert 0 <= insights['potential'] <= 1

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
