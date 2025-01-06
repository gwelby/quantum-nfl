"""
Tests for NFL Team Combinations System
"""
import pytest
import numpy as np
from src.quantum.team_combinations import QuantumCombo, NFLCombinations

@pytest.fixture
def combinator():
    return NFLCombinations()

@pytest.fixture
def frozen_tundra():
    return QuantumCombo(
        teams=['PACKERS', 'BILLS', 'VIKINGS'],
        name='Frozen Tundra Alliance',
        power=0.95,
        effects=['❄️ Arctic Blast', '🌨️ Snow Game Mastery', '🥶 Cold Front Defense'],
        synergy=0.93,
        special_plays=['Blizzard Blitz', 'Ice Wall Defense', 'Frost Route']
    )

@pytest.fixture
def coastal_energy():
    return QuantumCombo(
        teams=['49ERS', 'SEAHAWKS', 'DOLPHINS'],
        name='Coastal Energy Nexus',
        power=0.92,
        effects=['🌊 Ocean Power', '🌉 Bridge Energy', '🏖️ Beach Force'],
        synergy=0.91,
        special_plays=['Tide Turn Play', 'Wave Runner', 'Beach Blitz']
    )

def test_combo_creation(frozen_tundra):
    """Test creation of quantum combo object"""
    assert 'PACKERS' in frozen_tundra.teams
    assert 'Frozen Tundra Alliance' == frozen_tundra.name
    assert 0 <= frozen_tundra.power <= 1.0
    assert len(frozen_tundra.effects) > 0
    assert 0 <= frozen_tundra.synergy <= 1.0
    assert len(frozen_tundra.special_plays) > 0

def test_power_calculation(combinator, frozen_tundra):
    """Test power calculation"""
    power = combinator.calculate_power(frozen_tundra)
    assert isinstance(power, float)
    assert 0 <= power <= 1.0
    
    # Power should be enhanced by synergy
    base_power = frozen_tundra.power
    synergy_boost = frozen_tundra.synergy * 0.1  # Example synergy calculation
    assert power >= base_power

def test_team_synergy(combinator, frozen_tundra):
    """Test team synergy effects"""
    base_power = combinator.calculate_power(frozen_tundra)
    
    # Create version with higher synergy
    enhanced_combo = QuantumCombo(
        teams=frozen_tundra.teams,
        name=frozen_tundra.name,
        power=frozen_tundra.power,
        effects=frozen_tundra.effects,
        synergy=min(1.0, frozen_tundra.synergy * 1.1),
        special_plays=frozen_tundra.special_plays
    )
    enhanced_power = combinator.calculate_power(enhanced_combo)
    
    assert enhanced_power > base_power

def test_special_plays(combinator, frozen_tundra):
    """Test special plays impact"""
    base_power = combinator.calculate_power(frozen_tundra)
    
    # Add another special play
    enhanced_combo = QuantumCombo(
        teams=frozen_tundra.teams,
        name=frozen_tundra.name,
        power=frozen_tundra.power,
        effects=frozen_tundra.effects,
        synergy=frozen_tundra.synergy,
        special_plays=frozen_tundra.special_plays + ['Arctic Vortex']
    )
    enhanced_power = combinator.calculate_power(enhanced_combo)
    
    assert enhanced_power >= base_power

def test_team_effects(combinator, frozen_tundra):
    """Test team effects impact"""
    base_power = combinator.calculate_power(frozen_tundra)
    
    # Add another effect
    enhanced_combo = QuantumCombo(
        teams=frozen_tundra.teams,
        name=frozen_tundra.name,
        power=frozen_tundra.power,
        effects=frozen_tundra.effects + ['❄️ Frozen Field Advantage'],
        synergy=frozen_tundra.synergy,
        special_plays=frozen_tundra.special_plays
    )
    enhanced_power = combinator.calculate_power(enhanced_combo)
    
    assert enhanced_power >= base_power

def test_team_composition(combinator, frozen_tundra, coastal_energy):
    """Test team composition impact"""
    tundra_power = combinator.calculate_power(frozen_tundra)
    coastal_power = combinator.calculate_power(coastal_energy)
    
    # Teams with more synergistic effects should have higher power
    tundra_effects = len(frozen_tundra.effects)
    coastal_effects = len(coastal_energy.effects)
    
    if tundra_effects > coastal_effects:
        assert tundra_power >= coastal_power
    elif coastal_effects > tundra_effects:
        assert coastal_power >= tundra_power

def test_combo_interaction(combinator, frozen_tundra, coastal_energy):
    """Test interaction between different combos"""
    # When combos interact, their powers should influence each other
    base_power = combinator.calculate_power(frozen_tundra)
    
    # Create a version with some coastal teams
    mixed_combo = QuantumCombo(
        teams=['PACKERS', 'BILLS', 'DOLPHINS'],  # Replace VIKINGS with DOLPHINS
        name='Mixed Weather Alliance',
        power=frozen_tundra.power,
        effects=['❄️ Arctic Blast', '🌊 Ocean Power'],  # Mix of effects
        synergy=0.85,  # Lower synergy due to mixed weather
        special_plays=frozen_tundra.special_plays
    )
    mixed_power = combinator.calculate_power(mixed_combo)
    
    # Mixed weather teams should have lower synergy
    assert mixed_power < base_power

def test_power_scaling(combinator, frozen_tundra):
    """Test power scaling with number of effects"""
    base_power = combinator.calculate_power(frozen_tundra)
    
    # Create version with more effects but same base power
    scaled_combo = QuantumCombo(
        teams=frozen_tundra.teams,
        name=frozen_tundra.name,
        power=frozen_tundra.power,
        effects=frozen_tundra.effects + ['❄️ Winter Wind', '🌨️ Snow Shield'],
        synergy=frozen_tundra.synergy,
        special_plays=frozen_tundra.special_plays
    )
    scaled_power = combinator.calculate_power(scaled_combo)
    
    # More effects should lead to higher power
    assert scaled_power > base_power
