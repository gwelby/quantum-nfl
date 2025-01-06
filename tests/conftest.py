"""
Shared pytest fixtures for Quantum NFL tests
"""
import pytest
import numpy as np
from datetime import datetime
from src.quantum.historical_echoes import NFLHistory
from src.visualization.team_matchups import TeamMatchups

@pytest.fixture(scope="session")
def current_season():
    return 2025

@pytest.fixture(scope="session")
def quantum_constants():
    return {
        'planck_constant': 6.62607015e-34,
        'base_resonance': 0.95,
        'quantum_decay_rate': 0.001,
        'interference_threshold': 0.5
    }

@pytest.fixture(scope="session")
def nfl_teams():
    return [
        "PACKERS", "BEARS", "VIKINGS", "LIONS",  # NFC North
        "CHIEFS", "RAIDERS", "BRONCOS", "CHARGERS",  # AFC West
        # Add more as needed
    ]

@pytest.fixture(scope="function")
def mock_quantum_state():
    def _quantum_state(offense=0.8, defense=0.8, momentum=0.8):
        return {
            'offense_power': offense,
            'defense_power': defense,
            'momentum': momentum,
            'wave_function': np.random.rand(100, 100)
        }
    return _quantum_state

@pytest.fixture(scope="session")
def test_data_directory(tmp_path_factory):
    """Create and return a temporary directory for test data"""
    return tmp_path_factory.mktemp("quantum_test_data")
