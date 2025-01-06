"""
Tests for NFL Playoff Predictions System
"""
import pytest
import numpy as np
from datetime import datetime
from src.quantum.playoff_predictions import PlayoffTeam, NFLPlayoffPredictor

@pytest.fixture
def predictor():
    return NFLPlayoffPredictor()

@pytest.fixture
def packers_team():
    return PlayoffTeam(
        name="PACKERS",
        seed=2,
        momentum=0.88,
        quantum_power=0.85,
        playoff_experience=0.92,
        clutch_factor=0.87,
        home_advantage=0.94,
        injury_resistance=0.91
    )

@pytest.fixture
def chiefs_team():
    return PlayoffTeam(
        name="CHIEFS",
        seed=1,
        momentum=0.90,
        quantum_power=0.87,
        playoff_experience=0.94,
        clutch_factor=0.89,
        home_advantage=0.92,
        injury_resistance=0.93
    )

def test_playoff_team_creation(packers_team):
    """Test creation of playoff team object"""
    assert packers_team.name == "PACKERS"
    assert 1 <= packers_team.seed <= 7  # Valid playoff seed
    assert 0 <= packers_team.momentum <= 1.0
    assert 0 <= packers_team.quantum_power <= 1.0
    assert 0 <= packers_team.playoff_experience <= 1.0
    assert 0 <= packers_team.clutch_factor <= 1.0
    assert 0 <= packers_team.home_advantage <= 1.0
    assert 0 <= packers_team.injury_resistance <= 1.0

def test_win_probability_calculation(predictor, packers_team, chiefs_team):
    """Test win probability calculation"""
    prob, details = predictor.calculate_win_probability(packers_team, chiefs_team, "Divisional Round")
    assert isinstance(prob, float)
    assert isinstance(details, dict)
    assert 0 <= prob <= 1.0

def test_momentum_impact(predictor, packers_team, chiefs_team):
    """Test momentum impact"""
    base_prob, _ = predictor.calculate_win_probability(packers_team, chiefs_team, "Divisional Round")
    
    # Increase momentum
    enhanced_team = PlayoffTeam(
        name=packers_team.name,
        seed=packers_team.seed,
        momentum=min(1.0, packers_team.momentum * 1.1),
        quantum_power=packers_team.quantum_power,
        playoff_experience=packers_team.playoff_experience,
        clutch_factor=packers_team.clutch_factor,
        home_advantage=packers_team.home_advantage,
        injury_resistance=packers_team.injury_resistance
    )
    enhanced_prob, _ = predictor.calculate_win_probability(enhanced_team, chiefs_team, "Divisional Round")
    
    assert enhanced_prob > base_prob

def test_home_advantage(predictor, packers_team, chiefs_team):
    """Test home field advantage impact"""
    base_prob, _ = predictor.calculate_win_probability(packers_team, chiefs_team, "Divisional Round")
    
    # Increase home advantage
    home_team = PlayoffTeam(
        name=packers_team.name,
        seed=packers_team.seed,
        momentum=packers_team.momentum,
        quantum_power=packers_team.quantum_power,
        playoff_experience=packers_team.playoff_experience,
        clutch_factor=packers_team.clutch_factor,
        home_advantage=min(1.0, packers_team.home_advantage * 1.1),
        injury_resistance=packers_team.injury_resistance
    )
    home_prob, _ = predictor.calculate_win_probability(home_team, chiefs_team, "Divisional Round")
    
    assert home_prob > base_prob

def test_playoff_experience(predictor, packers_team, chiefs_team):
    """Test playoff experience impact"""
    base_prob, _ = predictor.calculate_win_probability(packers_team, chiefs_team, "Divisional Round")
    
    # Increase playoff experience
    experienced_team = PlayoffTeam(
        name=packers_team.name,
        seed=packers_team.seed,
        momentum=packers_team.momentum,
        quantum_power=packers_team.quantum_power,
        playoff_experience=min(1.0, packers_team.playoff_experience * 1.1),
        clutch_factor=packers_team.clutch_factor,
        home_advantage=packers_team.home_advantage,
        injury_resistance=packers_team.injury_resistance
    )
    exp_prob, _ = predictor.calculate_win_probability(experienced_team, chiefs_team, "Divisional Round")
    
    assert exp_prob > base_prob

def test_clutch_performance(predictor, packers_team, chiefs_team):
    """Test clutch factor in playoffs"""
    base_prob, _ = predictor.calculate_win_probability(packers_team, chiefs_team, "Super Bowl")
    
    # Increase clutch factor
    clutch_team = PlayoffTeam(
        name=packers_team.name,
        seed=packers_team.seed,
        momentum=packers_team.momentum,
        quantum_power=packers_team.quantum_power,
        playoff_experience=packers_team.playoff_experience,
        clutch_factor=min(1.0, packers_team.clutch_factor * 1.1),
        home_advantage=packers_team.home_advantage,
        injury_resistance=packers_team.injury_resistance
    )
    clutch_prob, _ = predictor.calculate_win_probability(clutch_team, chiefs_team, "Super Bowl")
    
    assert clutch_prob > base_prob

def test_injury_impact(predictor, packers_team, chiefs_team):
    """Test injury impact"""
    base_prob, _ = predictor.calculate_win_probability(packers_team, chiefs_team, "Divisional Round")
    
    # Decrease injury resistance
    injured_team = PlayoffTeam(
        name=packers_team.name,
        seed=packers_team.seed,
        momentum=packers_team.momentum,
        quantum_power=packers_team.quantum_power,
        playoff_experience=packers_team.playoff_experience,
        clutch_factor=packers_team.clutch_factor,
        home_advantage=packers_team.home_advantage,
        injury_resistance=packers_team.injury_resistance * 0.8
    )
    injured_prob, _ = predictor.calculate_win_probability(injured_team, chiefs_team, "Divisional Round")
    
    assert injured_prob < base_prob

def test_seed_advantage(predictor, packers_team, chiefs_team):
    """Test playoff seeding impact"""
    # Higher seed should have slight advantage
    high_seed_prob, _ = predictor.calculate_win_probability(chiefs_team, packers_team, "Divisional Round")
    low_seed_prob, _ = predictor.calculate_win_probability(packers_team, chiefs_team, "Divisional Round")
    
    assert high_seed_prob > low_seed_prob
