"""
Test suite for Quantum Teams analysis
"""

import pytest
import numpy as np
from pathlib import Path
from hypothesis import given, strategies as st
import cirq
import pennylane as qml
from src.simulation.game_simulator import NFLQuantumSimulator, GameState

class TestQuantumTeams:
    """Test class for quantum team interactions"""
    
    @pytest.fixture
    def quantum_circuit(self):
        """Create a quantum circuit for team entanglement"""
        n_qubits = 4  # One for each major aspect: offense, defense, special teams, momentum
        circuit = cirq.Circuit()
        qubits = cirq.LineQubit.range(n_qubits)
        
        # Create superposition
        circuit.append(cirq.H.on_each(qubits))
        
        # Add entanglement
        for i in range(n_qubits-1):
            circuit.append(cirq.CNOT(qubits[i], qubits[i+1]))
            
        return circuit, qubits
        
    @pytest.fixture
    def quantum_device(self):
        """Initialize quantum device for simulation"""
        dev = qml.device('default.qubit', wires=4)
        
        @qml.qnode(dev)
        def quantum_circuit(params):
            # Encode team parameters
            for i in range(4):
                qml.RY(params[i], wires=i)
                
            # Create entanglement
            for i in range(3):
                qml.CNOT(wires=[i, i+1])
                
            # Measure quantum states
            return [qml.expval(qml.PauliZ(i)) for i in range(4)]
            
        return quantum_circuit
        
    def test_team_initialization(self, simulator):
        """Test quantum team initialization"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Check quantum states
        assert 0 <= simulator.quantum_states["GB"] <= 1
        assert 0 <= simulator.quantum_states["CHI"] <= 1
        assert abs(simulator.quantum_states["GB"] + simulator.quantum_states["CHI"] - 1) < 1e-10
        
    def test_quantum_entanglement(self, simulator, quantum_device):
        """Test quantum entanglement between teams"""
        # Initialize two games with same team
        game1 = simulator.initialize_game("GB", "CHI")
        game2 = simulator.initialize_game("GB", "MIN")
        
        # Get quantum parameters for GB in both games
        params1 = [simulator.quantum_states["GB"], game1.momentum, 0.5, 0.5]
        params2 = [simulator.quantum_states["GB"], game2.momentum, 0.5, 0.5]
        
        # Measure quantum states
        result1 = quantum_device(params1)
        result2 = quantum_device(params2)
        
        # Check for quantum correlation
        correlation = np.corrcoef(result1, result2)[0,1]
        assert abs(correlation) > 0.5  # Strong quantum correlation expected
        
    @given(st.lists(st.floats(min_value=0, max_value=1), min_size=4, max_size=4))
    def test_quantum_probability_properties(self, simulator, params):
        """Test properties of quantum probability calculations"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Test multiple situations
        situations = ['normal', 'redzone', 'thirddown', 'fourthdown']
        
        for situation, param in zip(situations, params):
            prob = simulator.calculate_quantum_probability(param, "GB", situation)
            assert 0 <= prob <= 1  # Probability bounds
            
    def test_momentum_quantum_effects(self, simulator):
        """Test quantum effects on momentum"""
        game = simulator.initialize_game("GB", "CHI")
        initial_momentum = game.momentum
        
        # Simulate quantum momentum changes
        big_play_momentum = simulator.calculate_quantum_probability(0.8, "GB", "normal")
        simulator.update_momentum(game, "Touchdown", 80)
        
        assert game.momentum > initial_momentum  # Positive momentum shift
        assert game.momentum <= 1.0  # Upper bound
        
        # Test negative momentum
        simulator.update_momentum(game, "Interception", 0)
        assert game.momentum < big_play_momentum  # Negative momentum shift
        assert game.momentum >= 0.0  # Lower bound
        
    def test_quantum_memory_effects(self, simulator):
        """Test quantum memory and history effects"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Simulate series of plays
        plays = [
            ("Run", 5),
            ("Pass complete", 15),
            ("Incomplete pass", 0),
            ("Field goal", 3)
        ]
        
        for play_type, yards in plays:
            simulator.update_quantum_memory(play_type, yards)
            
        assert len(simulator.quantum_memory) == len(plays)
        assert all(isinstance(m['success'], float) for m in simulator.quantum_memory)
        
    def test_interference_patterns(self, simulator):
        """Test quantum interference patterns"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Simulate full game
        result = simulator.simulate_game("GB", "CHI")
        
        # Analyze quantum patterns
        patterns = simulator.detect_interference_patterns(result['stats']['plays'])
        
        assert 'yards_autocorrelation' in patterns
        assert 'momentum_periodicity' in patterns
        assert 'quantum_coherence' in patterns
        
        # Test for non-random patterns
        coherence = patterns['quantum_coherence']
        assert 0 <= coherence <= 1  # Normalized coherence
        
    def test_quantum_stability(self, simulator):
        """Test quantum stability over time"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Track quantum states over time
        states = []
        for _ in range(10):
            simulator.simulate_play(game)
            states.append(game.quantum_state.copy())
            
        # Calculate stability metrics
        stability = np.mean([s['superposition'] for s in states])
        variance = np.var([s['entanglement'] for s in states])
        
        assert 0 <= stability <= 1
        assert variance < 0.5  # Expect some variance but not too much
        
    @pytest.mark.parametrize("home,away", [
        ("GB", "CHI"),
        ("KC", "SF"),
        ("TB", "NO"),
        ("LAR", "SEA")
    ])
    def test_rivalry_quantum_effects(self, simulator, home, away):
        """Test quantum effects in rivalry games"""
        game = simulator.initialize_game(home, away)
        
        # Simulate first quarter
        for _ in range(15):  # Approximately one quarter
            simulator.simulate_play(game)
            
        # Check for rivalry-specific quantum effects
        assert game.quantum_state['interference'] > 0.4  # Higher interference in rivalry games
        assert abs(game.momentum - 0.5) < 0.3  # Close games expected
        
    def test_quantum_drive_analysis(self, simulator):
        """Test quantum analysis of drives"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Simulate a drive
        drive = []
        for _ in range(8):  # Typical drive length
            play = simulator.simulate_play(game)
            drive.append(play)
            
        # Analyze drive
        analysis = simulator.analyze_drive(drive)
        
        assert 'success_rate' in analysis
        assert 'plays' in analysis
        assert 'yards' in analysis
        assert isinstance(analysis['success_rate'], float)
        
    def test_quantum_game_analysis(self, simulator):
        """Test full game quantum analysis"""
        result = simulator.simulate_game("GB", "CHI")
        
        # Check quantum analysis results
        analysis = result['quantum_analysis']
        
        assert 'momentum_volatility' in analysis
        assert 'quantum_stability' in analysis
        assert 'entanglement_strength' in analysis
        assert 'interference_patterns' in analysis
        
        # Verify reasonable values
        assert 0 <= analysis['quantum_stability'] <= 1
        assert -1 <= analysis['entanglement_strength'] <= 1
