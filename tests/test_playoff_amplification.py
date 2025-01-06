"""
Tests for NFL Playoff Quantum Amplification System
"""
import pytest
import numpy as np
from src.quantum.playoff_amplification import PlayoffAmplification, NFLPlayoffs

@pytest.fixture
def playoffs():
    return NFLPlayoffs()

@pytest.fixture
def packers_metrics():
    return PlayoffAmplification(
        base_power=0.88,
        playoff_boost=1.15,
        momentum=0.92,
        home_field=0.85,
        experience=0.90,
        pressure=0.87,
        legacy_factor=0.95,
        clutch_rating=0.89,
        dynasty_power=0.92
    )

@pytest.fixture
def chiefs_metrics():
    return PlayoffAmplification(
        base_power=0.90,
        playoff_boost=1.18,
        momentum=0.95,
        home_field=0.88,
        experience=0.92,
        pressure=0.90,
        legacy_factor=0.88,
        clutch_rating=0.91,
        dynasty_power=0.89
    )

def test_playoff_amplification_creation(packers_metrics):
    """Test creation of playoff amplification metrics"""
    assert 0 <= packers_metrics.base_power <= 1.0
    assert packers_metrics.playoff_boost >= 1.0  # Boost should be multiplicative
    assert 0 <= packers_metrics.momentum <= 1.0
    assert 0 <= packers_metrics.home_field <= 1.0
    assert 0 <= packers_metrics.experience <= 1.0
    assert 0 <= packers_metrics.pressure <= 1.0
    assert 0 <= packers_metrics.legacy_factor <= 1.0
    assert 0 <= packers_metrics.clutch_rating <= 1.0
    assert 0 <= packers_metrics.dynasty_power <= 1.0

def test_amplification_calculation(playoffs, packers_metrics):
    """Test playoff amplification calculation"""
    amp = playoffs.calculate_amplification(packers_metrics)
    assert isinstance(amp, float)
    assert amp > packers_metrics.base_power  # Amplification should increase power

def test_playoff_boost_effect(playoffs, packers_metrics):
    """Test playoff boost effect on team power"""
    base_amp = playoffs.calculate_amplification(packers_metrics)
    
    # Increase playoff boost
    enhanced_metrics = PlayoffAmplification(
        **{**packers_metrics.__dict__, 'playoff_boost': packers_metrics.playoff_boost * 1.1}
    )
    boosted_amp = playoffs.calculate_amplification(enhanced_metrics)
    
    assert boosted_amp > base_amp

def test_home_field_advantage(playoffs, packers_metrics):
    """Test home field advantage impact"""
    base_amp = playoffs.calculate_amplification(packers_metrics)
    
    # Increase home field advantage
    enhanced_metrics = PlayoffAmplification(
        **{**packers_metrics.__dict__, 'home_field': min(1.0, packers_metrics.home_field * 1.1)}
    )
    home_amp = playoffs.calculate_amplification(enhanced_metrics)
    
    assert home_amp > base_amp

def test_legacy_impact(playoffs, packers_metrics):
    """Test historical legacy impact"""
    base_amp = playoffs.calculate_amplification(packers_metrics)
    
    # Increase legacy factor
    enhanced_metrics = PlayoffAmplification(
        **{**packers_metrics.__dict__, 'legacy_factor': min(1.0, packers_metrics.legacy_factor * 1.1)}
    )
    legacy_amp = playoffs.calculate_amplification(enhanced_metrics)
    
    assert legacy_amp > base_amp

def test_pressure_handling(playoffs, packers_metrics):
    """Test pressure handling in playoffs"""
    base_amp = playoffs.calculate_amplification(packers_metrics)
    
    # Decrease pressure handling (simulating high-pressure situation)
    stressed_metrics = PlayoffAmplification(
        **{**packers_metrics.__dict__, 'pressure': packers_metrics.pressure * 0.8}
    )
    pressure_amp = playoffs.calculate_amplification(stressed_metrics)
    
    assert pressure_amp < base_amp  # Lower pressure handling should reduce amplification

def test_team_comparison(playoffs, packers_metrics, chiefs_metrics):
    """Test comparison between two teams"""
    packers_amp = playoffs.calculate_amplification(packers_metrics)
    chiefs_amp = playoffs.calculate_amplification(chiefs_metrics)
    
    # Both should be valid amplifications
    assert isinstance(packers_amp, float)
    assert isinstance(chiefs_amp, float)
    assert packers_amp > 0
    assert chiefs_amp > 0
