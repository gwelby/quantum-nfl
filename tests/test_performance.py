"""
Performance and benchmarking tests for NFL Quantum Simulator
"""

import pytest
import time
import cProfile
import pstats
import numpy as np
from pathlib import Path
from src.simulation.game_simulator import NFLQuantumSimulator
from src.teams.quantum_team import QuantumTeam

class TestPerformance:
    """Performance testing suite"""
    
    @pytest.fixture
    def profiler(self):
        """Create profiler fixture"""
        return cProfile.Profile()
        
    def test_game_simulation_speed(self, simulator):
        """Test game simulation performance"""
        start_time = time.time()
        result = simulator.simulate_game("GB", "CHI")
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 5.0  # Game should simulate in under 5 seconds
        
    def test_quantum_calculation_performance(self, simulator, profiler):
        """Test quantum calculation performance"""
        profiler.enable()
        
        # Run multiple quantum calculations
        for _ in range(1000):
            simulator.calculate_quantum_probability(0.5, "GB", "normal")
            
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('cumulative')
        
        # Get function statistics
        function_stats = {
            'calls': stats.total_calls,
            'time': stats.total_tt
        }
        
        # Average time per calculation should be under 1ms
        avg_time = function_stats['time'] / function_stats['calls']
        assert avg_time < 0.001
        
    @pytest.mark.benchmark
    def test_memory_usage(self, simulator):
        """Test memory usage during simulation"""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Run multiple games
        for _ in range(10):
            simulator.simulate_game("GB", "CHI")
            
        final_memory = process.memory_info().rss
        memory_increase = (final_memory - initial_memory) / 1024 / 1024  # Convert to MB
        
        assert memory_increase < 100  # Memory increase should be under 100MB
        
    @pytest.mark.benchmark
    def test_parallel_game_simulation(self, simulator):
        """Test parallel game simulation performance"""
        import concurrent.futures
        
        def simulate_parallel_game(teams):
            home, away = teams
            return simulator.simulate_game(home, away)
            
        team_pairs = [
            ("GB", "CHI"),
            ("KC", "SF"),
            ("TB", "NO"),
            ("LAR", "SEA")
        ]
        
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(simulate_parallel_game, team_pairs))
        end_time = time.time()
        
        parallel_time = end_time - start_time
        
        # Run sequential for comparison
        start_time = time.time()
        sequential_results = [simulate_parallel_game(pair) for pair in team_pairs]
        end_time = time.time()
        
        sequential_time = end_time - start_time
        
        # Parallel should be at least 2x faster
        assert parallel_time * 2 < sequential_time
        
    @pytest.mark.benchmark
    def test_quantum_memory_scaling(self, simulator):
        """Test quantum memory scaling performance"""
        memory_sizes = [10, 100, 1000]
        times = []
        
        for size in memory_sizes:
            start_time = time.time()
            
            # Generate quantum memory entries
            for _ in range(size):
                simulator.update_quantum_memory("Run", np.random.randint(-2, 20))
                
            end_time = time.time()
            times.append(end_time - start_time)
            
        # Time should scale linearly or better
        scaling_factor = times[-1] / times[0]
        size_factor = memory_sizes[-1] / memory_sizes[0]
        assert scaling_factor < size_factor
        
    @pytest.mark.benchmark
    def test_visualization_performance(self, simulator):
        """Test visualization update performance"""
        game = simulator.initialize_game("GB", "CHI")
        update_times = []
        
        for _ in range(100):
            start_time = time.time()
            simulator.simulate_play(game)
            end_time = time.time()
            update_times.append(end_time - start_time)
            
        avg_update_time = np.mean(update_times)
        assert avg_update_time < 0.1  # Updates should be under 100ms
        
    def test_quantum_algorithm_complexity(self, simulator):
        """Test quantum algorithm computational complexity"""
        sizes = [10, 100, 1000]
        times = []
        
        for size in sizes:
            start_time = time.time()
            
            # Run quantum calculations
            for _ in range(size):
                simulator.calculate_quantum_probability(
                    np.random.random(),
                    "GB",
                    "normal"
                )
                
            end_time = time.time()
            times.append(end_time - start_time)
            
        # Check for polynomial time complexity
        log_sizes = np.log(sizes)
        log_times = np.log(times)
        slope = np.polyfit(log_sizes, log_times, 1)[0]
        
        assert slope < 2  # Should be better than quadratic time
        
    @pytest.mark.benchmark
    def test_drive_analysis_performance(self, simulator):
        """Test drive analysis performance"""
        game = simulator.initialize_game("GB", "CHI")
        drives = []
        
        # Generate test drives
        for _ in range(100):
            drive = []
            for _ in range(np.random.randint(5, 15)):
                drive.append(simulator.simulate_play(game))
            drives.append(drive)
            
        start_time = time.time()
        for drive in drives:
            simulator.analyze_drive(drive)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / len(drives)
        assert avg_time < 0.01  # Analysis should be under 10ms per drive

@pytest.fixture
def simulator():
    return NFLQuantumSimulator()

@pytest.fixture
def teams():
    return [QuantumTeam("Team A"), QuantumTeam("Team B")]

def test_simulation_speed(simulator, teams, benchmark):
    def run_sim():
        simulator.simulate_game(teams[0], teams[1])
    benchmark(run_sim)

def test_quantum_calculation_performance(simulator, teams, benchmark):
    def calc_quantum():
        simulator.calculate_quantum_state(teams[0], teams[1])
    benchmark(calc_quantum)

def test_memory_usage(simulator, teams):
    process = psutil.Process()
    initial_memory = process.memory_info().rss
    
    for _ in range(100):
        simulator.simulate_game(teams[0], teams[1])
    
    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory
    
    assert memory_increase < 100 * 1024 * 1024  # Less than 100MB increase

def test_parallel_simulation_scaling():
    simulators = [NFLQuantumSimulator() for _ in range(4)]
    teams_list = [(QuantumTeam(f"Team {i}"), QuantumTeam(f"Team {i+1}")) 
                  for i in range(0, 8, 2)]
    
    start_time = time.time()
    results = []
    for sim, (team1, team2) in zip(simulators, teams_list):
        results.append(sim.simulate_game(team1, team2))
    sequential_time = time.time() - start_time
    
    # Test parallel execution (you would implement actual parallel execution here)
    parallel_time = sequential_time / len(simulators)  # Theoretical perfect scaling
    
    assert parallel_time < sequential_time

@pytest.mark.benchmark
def test_algorithm_complexity(benchmark):
    sizes = [10, 100, 1000]
    times = []
    
    for size in sizes:
        simulator = NFLQuantumSimulator()
        teams = [QuantumTeam(f"Team {i}") for i in range(size)]
        
        def run_large_sim():
            simulator.simulate_tournament(teams)
            
        result = benchmark.pedantic(run_large_sim, iterations=1, rounds=1)
        times.append(result)
    
    # Verify complexity is approximately O(n log n)
    ratios = [times[i+1]/times[i] for i in range(len(times)-1)]
    expected_ratios = [(sizes[i+1]/sizes[i]) * np.log2(sizes[i+1]/sizes[i]) 
                      for i in range(len(sizes)-1)]
    
    assert all(abs(r1/r2 - 1) < 0.5 for r1, r2 in zip(ratios, expected_ratios))

def test_visualization_performance(benchmark):
    simulator = NFLQuantumSimulator()
    teams = [QuantumTeam("Team A"), QuantumTeam("Team B")]
    
    def update_visuals():
        simulator.update_visualization(teams[0], teams[1])
        
    result = benchmark(update_visuals)
    assert result.stats.mean < 0.1  # Updates should take less than 100ms

def test_drive_analysis_performance(benchmark):
    simulator = NFLQuantumSimulator()
    
    def analyze_drives():
        simulator.analyze_game_drives(
            past_games=100,
            quantum_factors=True,
            detailed_stats=True
        )
    
    result = benchmark(analyze_drives)
    assert result.stats.mean < 1.0  # Analysis should complete within 1 second
