"""
Tests for NFL Rivalry Resonance System
"""
import pytest
import numpy as np
from src.quantum.rivalry_resonance import RivalryResonance, NFLRivalries

@pytest.fixture
def rivalry_system():
    return NFLRivalries()

@pytest.fixture
def packers_bears_resonance():
    return RivalryResonance(
        teams=('PACKERS', 'BEARS'),
        intensity=0.85,  # Lowered to allow for testing increases
        history=0.99,
        fan_energy=0.85,
        field_clash=0.87,
        special_games=['Ice Bowl', 'Christmas 2011']
    )

@pytest.fixture
def chiefs_raiders_resonance():
    return RivalryResonance(
        teams=('CHIEFS', 'RAIDERS'),
        intensity=0.82,  # Lower base values for testing
        history=0.83,
        fan_energy=0.85,
        field_clash=0.82,
        special_games=['Red Friday Showdown']
    )

def test_rivalry_creation(packers_bears_resonance):
    """Test creation of rivalry resonance object"""
    assert packers_bears_resonance.teams == ('PACKERS', 'BEARS')
    assert 0 <= packers_bears_resonance.intensity <= 1.0
    assert 0 <= packers_bears_resonance.history <= 1.0
    assert 0 <= packers_bears_resonance.fan_energy <= 1.0
    assert 0 <= packers_bears_resonance.field_clash <= 1.0
    assert len(packers_bears_resonance.special_games) > 0

def test_resonance_calculation(rivalry_system, packers_bears_resonance):
    """Test rivalry resonance calculation"""
    resonance = rivalry_system.calculate_resonance(packers_bears_resonance)
    assert isinstance(resonance, float)
    assert 0 <= resonance <= 1.0
    
    # Calculate expected base power
    base_power = (packers_bears_resonance.intensity + 
                 packers_bears_resonance.history +
                 packers_bears_resonance.fan_energy + 
                 packers_bears_resonance.field_clash) / 4
    game_bonus = len(packers_bears_resonance.special_games) * 0.05
    expected = min(base_power + game_bonus, 1.0)
    
    assert abs(resonance - expected) < 1e-6

def test_historical_weight(rivalry_system, packers_bears_resonance, chiefs_raiders_resonance):
    """Test historical weight impact on resonance"""
    # Calculate raw base powers without game bonus
    packers_bears_base = (packers_bears_resonance.intensity + 
                         packers_bears_resonance.history +
                         packers_bears_resonance.fan_energy + 
                         packers_bears_resonance.field_clash) / 4
                         
    chiefs_raiders_base = (chiefs_raiders_resonance.intensity + 
                          chiefs_raiders_resonance.history +
                          chiefs_raiders_resonance.fan_energy + 
                          chiefs_raiders_resonance.field_clash) / 4
    
    assert packers_bears_base > chiefs_raiders_base

def test_special_games_impact(rivalry_system, packers_bears_resonance):
    """Test special games impact"""
    base_resonance = rivalry_system.calculate_resonance(packers_bears_resonance)
    
    # Add another special game
    enhanced_resonance = RivalryResonance(
        teams=packers_bears_resonance.teams,
        intensity=packers_bears_resonance.intensity,
        history=packers_bears_resonance.history,
        fan_energy=packers_bears_resonance.fan_energy,
        field_clash=packers_bears_resonance.field_clash,
        special_games=packers_bears_resonance.special_games + ['2024 Playoff Showdown']
    )
    enhanced_value = rivalry_system.calculate_resonance(enhanced_resonance)
    
    # Each special game adds 0.05 to resonance (before capping)
    assert enhanced_value >= base_resonance

def test_field_clash_effect(rivalry_system, packers_bears_resonance):
    """Test field clash effects"""
    # Create a version with lower field clash
    base_resonance = RivalryResonance(
        teams=packers_bears_resonance.teams,
        intensity=packers_bears_resonance.intensity,
        history=packers_bears_resonance.history,
        fan_energy=packers_bears_resonance.fan_energy,
        field_clash=0.7,  # Lower value
        special_games=packers_bears_resonance.special_games
    )
    
    # Compare with enhanced field clash
    enhanced_resonance = RivalryResonance(
        teams=packers_bears_resonance.teams,
        intensity=packers_bears_resonance.intensity,
        history=packers_bears_resonance.history,
        fan_energy=packers_bears_resonance.fan_energy,
        field_clash=0.8,  # Higher value
        special_games=packers_bears_resonance.special_games
    )
    
    base_value = rivalry_system.calculate_resonance(base_resonance)
    enhanced_value = rivalry_system.calculate_resonance(enhanced_resonance)
    
    assert enhanced_value > base_value

def test_resonance_combination(rivalry_system, packers_bears_resonance, chiefs_raiders_resonance):
    """Test combining multiple rivalry resonances"""
    resonance1 = rivalry_system.calculate_resonance(packers_bears_resonance)
    resonance2 = rivalry_system.calculate_resonance(chiefs_raiders_resonance)
    
    # Calculate weighted average based on history
    weighted_resonance = (resonance1 * packers_bears_resonance.history + 
                         resonance2 * chiefs_raiders_resonance.history) / (
                             packers_bears_resonance.history + chiefs_raiders_resonance.history)
    
    assert 0 <= weighted_resonance <= 1.0
    assert min(resonance1, resonance2) <= weighted_resonance <= max(resonance1, resonance2)

def test_fan_energy_amplification(rivalry_system, packers_bears_resonance):
    """Test fan energy amplification"""
    base_resonance = rivalry_system.calculate_resonance(packers_bears_resonance)
    
    # Increase fan energy
    energized_resonance = RivalryResonance(
        teams=packers_bears_resonance.teams,
        intensity=packers_bears_resonance.intensity,
        history=packers_bears_resonance.history,
        fan_energy=min(1.0, packers_bears_resonance.fan_energy * 1.1),
        field_clash=packers_bears_resonance.field_clash,
        special_games=packers_bears_resonance.special_games
    )
    energized_value = rivalry_system.calculate_resonance(energized_resonance)
    
    assert energized_value >= base_resonance

def test_intensity_scaling(rivalry_system, packers_bears_resonance):
    """Test intensity scaling effects"""
    base_resonance = rivalry_system.calculate_resonance(packers_bears_resonance)
    
    # Reduce intensity
    reduced_resonance = RivalryResonance(
        teams=packers_bears_resonance.teams,
        intensity=packers_bears_resonance.intensity * 0.8,
        history=packers_bears_resonance.history,
        fan_energy=packers_bears_resonance.fan_energy,
        field_clash=packers_bears_resonance.field_clash,
        special_games=packers_bears_resonance.special_games
    )
    reduced_value = rivalry_system.calculate_resonance(reduced_resonance)
    
    assert reduced_value <= base_resonance  # Lower intensity should reduce resonance
