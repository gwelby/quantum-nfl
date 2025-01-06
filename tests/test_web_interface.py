"""
Test suite for web interface functionality
"""

import pytest
from pathlib import Path
import json
from bs4 import BeautifulSoup
import re

class TestWebInterface:
    """Test class for web interface functionality"""
    
    @pytest.fixture
    def html_content(self):
        """Load HTML content"""
        html_path = Path("website/simulator.html")
        return html_path.read_text(encoding='utf-8')
        
    @pytest.fixture
    def js_content(self):
        """Load JavaScript content"""
        js_path = Path("website/simulator.js")
        return js_path.read_text(encoding='utf-8')
        
    @pytest.fixture
    def teams_data(self):
        """Load teams data"""
        teams_path = Path("website/teams.js")
        content = teams_path.read_text(encoding='utf-8')
        # Extract JSON data from JavaScript
        json_str = re.search(r'const NFL_TEAMS = ({.*?});', content, re.DOTALL).group(1)
        return json.loads(json_str)
        
    def test_html_structure(self, html_content):
        """Test HTML structure and required elements"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Check for required sections
        assert soup.find(id="game-setup")
        assert soup.find(id="game-simulation")
        assert soup.find(id="game-stats")
        
        # Check for team selectors
        assert soup.find(id="home-team")
        assert soup.find(id="away-team")
        
        # Check for visualization elements
        assert soup.find(id="field-position-marker")
        assert soup.find(id="momentum-bar")
        assert soup.find(id="stats-chart")
        
    def test_teams_data_structure(self, teams_data):
        """Test teams data structure"""
        required_fields = ['name', 'icon', 'colors', 'quantumRating']
        
        for team_code, team_data in teams_data.items():
            # Check team code format
            assert len(team_code) in [2, 3]
            assert team_code.isupper()
            
            # Check required fields
            for field in required_fields:
                assert field in team_data
                
            # Check colors
            assert 'primary' in team_data['colors']
            assert 'secondary' in team_data['colors']
            
            # Check quantum rating
            assert 0 <= team_data['quantumRating'] <= 1
            
    def test_javascript_classes(self, js_content):
        """Test JavaScript class structure"""
        # Check for required classes and methods
        assert 'class GameSimulator' in js_content
        
        required_methods = [
            'initializeGame',
            'calculateQuantumProbability',
            'simulatePlay',
            'updateMomentum',
            'updateChart'
        ]
        
        for method in required_methods:
            assert f'def {method}' in js_content or f'{method}(' in js_content
            
    def test_visualization_components(self, html_content):
        """Test visualization components"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Check for chart.js integration
        scripts = soup.find_all('script')
        assert any('chart.js' in str(script) for script in scripts)
        
        # Check for statistics bars
        stat_bars = [
            'total-yards-bar',
            'passing-yards-bar',
            'rushing-yards-bar',
            'sacks-bar',
            'interceptions-bar',
            'fumbles-bar',
            'field-goals-bar',
            'punts-bar',
            'return-yards-bar'
        ]
        
        for bar_id in stat_bars:
            assert soup.find(id=bar_id)
            
    def test_dark_mode_support(self, html_content):
        """Test dark mode implementation"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Check for theme toggle
        assert soup.find(id="theme-toggle")
        
        # Check for dark mode classes
        dark_classes = ['dark:bg-gray-900', 'dark:text-gray-200', 'dark:bg-gray-800']
        for class_name in dark_classes:
            elements = soup.find_all(class_=re.compile(class_name))
            assert len(elements) > 0
            
    def test_responsive_design(self, html_content):
        """Test responsive design implementation"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Check for responsive grid classes
        grid_classes = ['grid-cols-1', 'md:grid-cols-2', 'md:grid-cols-3']
        for class_name in grid_classes:
            elements = soup.find_all(class_=re.compile(class_name))
            assert len(elements) > 0
            
        # Check for responsive padding/margin
        responsive_classes = ['p-4', 'px-4', 'py-8', 'mt-6', 'mb-6']
        for class_name in responsive_classes:
            elements = soup.find_all(class_=re.compile(class_name))
            assert len(elements) > 0
            
    def test_game_simulation_updates(self, js_content):
        """Test game simulation update functions"""
        update_functions = [
            'updateDisplay',
            'updateGameState',
            'updateMomentum',
            'updateChart',
            'updateStats'
        ]
        
        for func in update_functions:
            assert f'def {func}' in js_content or f'{func}(' in js_content
            
    def test_quantum_visualization(self, html_content, js_content):
        """Test quantum state visualization"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Check for quantum visualization elements
        assert soup.find(id="quantum-momentum")
        assert soup.find(id="momentum-bar")
        
        # Check for quantum update functions in JS
        quantum_functions = [
            'calculateQuantumProbability',
            'updateQuantumMemory',
            'detectInterferencePatterns'
        ]
        
        for func in quantum_functions:
            assert f'def {func}' in js_content or f'{func}(' in js_content
            
    def test_error_handling(self, js_content):
        """Test error handling in JavaScript"""
        error_patterns = [
            'try {',
            'catch',
            'if (!',
            'return null',
            'console.error'
        ]
        
        for pattern in error_patterns:
            assert pattern in js_content
            
    def test_performance_optimization(self, js_content):
        """Test performance optimizations"""
        optimizations = [
            'requestAnimationFrame',
            'clearInterval',
            'setTimeout',
            'chart.update()'
        ]
        
        for opt in optimizations:
            assert opt in js_content
