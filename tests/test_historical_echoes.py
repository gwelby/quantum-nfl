"""
Tests for NFL Historical Echoes System
"""
import pytest
import numpy as np
from datetime import datetime
from src.quantum.historical_echoes import HistoricalEcho, NFLHistory

@pytest.fixture
def nfl_history():
    return NFLHistory()

@pytest.fixture
def ice_bowl_echo():
    return HistoricalEcho(
        year=1967,
        event="Ice Bowl",
        team="PACKERS",
        impact=1.0,
        resonance=0.95,
        frequency=0.92,
        amplitude=0.94,
        decay_rate=0.001,
        persistence=0.96,
        revival_power=0.85
    )

@pytest.fixture
def super_bowl_I_echo():
    return HistoricalEcho(
        year=1967,
        event="Super Bowl I",
        team="PACKERS",
        impact=1.0,
        resonance=0.97,
        frequency=0.95,
        amplitude=0.96,
        decay_rate=0.001,
        persistence=0.98,
        revival_power=0.90
    )

def test_historical_echo_creation(ice_bowl_echo):
    """Test creation of historical echo object"""
    assert ice_bowl_echo.year == 1967
    assert ice_bowl_echo.event == "Ice Bowl"
    assert ice_bowl_echo.team == "PACKERS"
    assert 0 <= ice_bowl_echo.resonance <= 1.0
    assert 0 <= ice_bowl_echo.frequency <= 1.0
    assert 0 <= ice_bowl_echo.amplitude <= 1.0

def test_nfl_history_initialization(nfl_history):
    """Test NFL History system initialization"""
    assert nfl_history.console is not None
    assert nfl_history.icons is not None
    assert isinstance(nfl_history.echoes, dict)
    assert "Ice Bowl" in nfl_history.echoes

def test_echo_decay_calculation(nfl_history, ice_bowl_echo):
    """Test temporal decay calculations"""
    current_year = 2025
    years_passed = current_year - ice_bowl_echo.year
    
    # Calculate decay
    decay_factor = np.exp(-ice_bowl_echo.decay_rate * years_passed)
    current_resonance = ice_bowl_echo.resonance * decay_factor
    
    assert 0 <= current_resonance <= ice_bowl_echo.resonance
    assert decay_factor < 1.0  # Should have decayed over time

def test_echo_resonance_validity(ice_bowl_echo):
    """Test echo resonance properties"""
    assert 0 <= ice_bowl_echo.resonance <= 1.0
    assert 0 <= ice_bowl_echo.persistence <= 1.0
    assert 0 <= ice_bowl_echo.revival_power <= 1.0

def test_quantum_interference(ice_bowl_echo, super_bowl_I_echo):
    """Test quantum interference between historic events"""
    # Calculate interference between two historic events
    interference = (ice_bowl_echo.resonance * super_bowl_I_echo.resonance * 
                   np.sqrt(ice_bowl_echo.amplitude * super_bowl_I_echo.amplitude))
    
    assert 0 <= interference <= 1.0
    # Events from same year should have strong interference
    assert interference > 0.8

def test_echo_persistence(ice_bowl_echo):
    """Test echo persistence over time"""
    current_year = 2025
    years_passed = current_year - ice_bowl_echo.year
    
    # Calculate persistence effect
    persistence_factor = ice_bowl_echo.persistence ** (years_passed / 50)  # Normalized by half-century
    assert 0 <= persistence_factor <= 1.0
    
    # Even after many years, significant events should retain some echo
    assert persistence_factor > 0.3

def test_revival_power_calculation(ice_bowl_echo):
    """Test revival power calculations"""
    base_power = ice_bowl_echo.revival_power
    resonance_boost = ice_bowl_echo.resonance * 0.2
    
    # Calculate total revival potential
    revival_potential = base_power + (1 - base_power) * resonance_boost
    assert 0 <= revival_potential <= 1.0
    assert revival_potential >= base_power  # Resonance should enhance revival power

def test_multiple_echo_combination(nfl_history, ice_bowl_echo, super_bowl_I_echo):
    """Test combination of multiple historical echoes"""
    # Combined echo effect should consider:
    # 1. Temporal proximity
    # 2. Team relationship
    # 3. Event significance
    
    combined_power = np.mean([
        ice_bowl_echo.impact * ice_bowl_echo.resonance,
        super_bowl_I_echo.impact * super_bowl_I_echo.resonance
    ])
    
    assert 0 <= combined_power <= 1.0
    # Both are significant events, so combined power should be high
    assert combined_power > 0.8
