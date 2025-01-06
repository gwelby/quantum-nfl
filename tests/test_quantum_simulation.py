"""
Test suite for NFL Quantum Teams simulation
"""

import pytest
import numpy as np
from src.simulation.game_simulator import NFLQuantumSimulator
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class TestGameState:
    """Test game state data"""
    home_team: str
    away_team: str
    quarter: int
    time_remaining: int
    score: Tuple[int, int]
    field_position: int
    possession: str
    momentum: float

class TestQuantumSimulation:
    """Test class for quantum simulation logic"""
    
    @pytest.fixture
    def simulator(self):
        """Create a simulator instance for testing"""
        return NFLQuantumSimulator()
    
    @pytest.fixture
    def test_states(self) -> List[TestGameState]:
        """Generate test game states"""
        return [
            TestGameState(
                home_team="GB",
                away_team="CHI",
                quarter=1,
                time_remaining=900,
                score=(0, 0),
                field_position=20,
                possession="GB",
                momentum=0.5
            ),
            TestGameState(
                home_team="KC",
                away_team="SF",
                quarter=4,
                time_remaining=120,
                score=(28, 24),
                field_position=75,
                possession="SF",
                momentum=0.8
            )
        ]
    
    def test_game_initialization(self, simulator):
        """Test game initialization"""
        game = simulator.initialize_game("GB", "CHI")
        assert game is not None
        assert game.home_team == "GB"
        assert game.away_team == "CHI"
        assert game.quarter == 1
        assert game.time_remaining == 900
        assert game.home_score == 0
        assert game.away_score == 0
        assert game.field_position == 20
        assert game.down == 1
        assert game.yards_to_go == 10
        assert game.possession in ["GB", "CHI"]

    def test_quantum_probability(self, simulator):
        """Test quantum probability calculations"""
        # Initialize game state
        game = simulator.initialize_game("GB", "CHI")
        
        # Test multiple probability calculations
        probabilities = [simulator.calculate_play_outcome(game) for _ in range(100)]
        
        # Verify probabilities are within expected ranges
        for play_type, yards in probabilities:
            assert isinstance(play_type, str)
            assert isinstance(yards, int)
            
            if "Run" in play_type:
                assert -2 <= yards <= 20
            elif "Pass" in play_type:
                assert -5 <= yards <= 50
            elif "Field goal" in play_type:
                assert yards in [0, 3]
            elif "Punt" in play_type:
                assert -60 <= yards <= -20

    def test_momentum_system(self, simulator):
        """Test the quantum momentum system"""
        game = simulator.initialize_game("KC", "SF")
        
        # Test positive momentum after big play
        initial_momentum = game.momentum
        simulator.update_momentum(game, "Pass complete", 25)
        assert game.momentum > initial_momentum
        
        # Test negative momentum after turnover
        simulator.update_momentum(game, "Interception", 0)
        assert game.momentum < initial_momentum

    def test_score_tracking(self, simulator):
        """Test score tracking and updates"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Test touchdown
        simulator.update_score(game, 7)
        assert (game.home_score == 7 and game.away_score == 0) or \
               (game.home_score == 0 and game.away_score == 7)
        
        # Test field goal
        simulator.update_score(game, 3)
        assert (game.home_score == 10 and game.away_score == 0) or \
               (game.home_score == 0 and game.away_score == 10)

    def test_time_management(self, simulator):
        """Test game clock management"""
        game = simulator.initialize_game("GB", "CHI")
        initial_time = game.time_remaining
        
        # Simulate several plays
        for _ in range(5):
            simulator.simulate_play(game)
            assert game.time_remaining < initial_time
            initial_time = game.time_remaining
        
        # Test quarter changes
        game.time_remaining = 1
        simulator.update_time(game, 10)
        assert game.quarter == 2
        assert game.time_remaining == 900

    def test_field_position(self, simulator):
        """Test field position tracking"""
        game = simulator.initialize_game("GB", "CHI")
        
        # Test moving down field
        initial_position = game.field_position
        simulator.update_field_position(game, 15)
        assert game.field_position == initial_position + 15
        
        # Test touchdown detection
        game.field_position = 95
        simulator.update_field_position(game, 10)
        assert game.field_position == 20  # Reset after touchdown
        assert (game.home_score == 7 or game.away_score == 7)

    def test_quantum_entanglement(self, simulator):
        """Test quantum entanglement between teams"""
        game1 = simulator.initialize_game("GB", "CHI")
        game2 = simulator.initialize_game("GB", "MIN")
        
        # Simulate multiple plays and verify entanglement effects
        for _ in range(10):
            result1 = simulator.simulate_play(game1)
            result2 = simulator.simulate_play(game2)
            
            # Test if GB's performance is correlated across games
            assert abs(game1.momentum - game2.momentum) < 0.3

    def test_statistical_analysis(self, simulator):
        """Test statistical analysis of game results"""
        stats = []
        
        # Simulate multiple games
        for _ in range(10):
            game = simulator.initialize_game("GB", "CHI")
            while game.quarter <= 4 and game.time_remaining > 0:
                simulator.simulate_play(game)
            stats.append({
                'home_score': game.home_score,
                'away_score': game.away_score,
                'total_plays': len(game.plays),
                'avg_yards_per_play': sum(p[1] for p in game.plays) / len(game.plays)
            })
        
        # Analyze results
        avg_score_diff = np.mean([s['home_score'] - s['away_score'] for s in stats])
        avg_plays = np.mean([s['total_plays'] for s in stats])
        avg_yards = np.mean([s['avg_yards_per_play'] for s in stats])
        
        # Verify realistic game statistics
        assert 30 < avg_plays < 150  # Reasonable number of plays
        assert -30 < avg_score_diff < 30  # Reasonable score differential
        assert 2 < avg_yards < 10  # Reasonable yards per play

    def test_weather_impact(self, simulator):
        """Test weather effects on game simulation"""
        # Test different weather conditions
        weather_conditions = [
            ('Clear', 1.0),
            ('Rain', 0.8),
            ('Snow', 0.6),
            ('Wind', 0.7)
        ]
        
        results = {}
        for condition, factor in weather_conditions:
            simulator.weather_impact = factor
            game = simulator.initialize_game("GB", "CHI")
            
            # Simulate 10 plays under each condition
            plays = []
            for _ in range(10):
                play_type, yards = simulator.simulate_play(game)
                plays.append(yards)
            
            results[condition] = np.mean(plays)
            
            # Verify weather impacts performance
            if condition != 'Clear':
                assert results[condition] < results['Clear']

    @pytest.mark.parametrize("home,away", [
        ("GB", "CHI"),
        ("KC", "SF"),
        ("TB", "NO"),
        ("LAR", "SEA")
    ])
    def test_rivalry_dynamics(self, simulator, home, away):
        """Test rivalry-specific game dynamics"""
        game = simulator.initialize_game(home, away)
        
        # Simulate full game
        while game.quarter <= 4 and game.time_remaining > 0:
            simulator.simulate_play(game)
        
        # Verify rivalry affects game intensity
        assert len(game.plays) >= 50  # Minimum number of plays
        assert abs(game.home_score - game.away_score) < 30  # Close games for rivals

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
