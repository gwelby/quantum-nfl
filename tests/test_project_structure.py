"""
Tests to verify NFL Quantum Teams project structure
"""
import os
import pytest

def test_root_directory_structure():
    """Test that all required root directories exist"""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    required_dirs = [
        'src',
        'tests',
        'docs'
    ]
    
    required_files = [
        'README.md',
        'requirements.txt',
        'pytest.ini'
    ]
    
    # Check directories
    for dir_name in required_dirs:
        dir_path = os.path.join(root_dir, dir_name)
        assert os.path.isdir(dir_path), f"Required directory '{dir_name}' is missing"
        
    # Check files
    for file_name in required_files:
        file_path = os.path.join(root_dir, file_name)
        assert os.path.isfile(file_path), f"Required file '{file_name}' is missing"

def test_src_directory_structure():
    """Test that all required source directories exist"""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(root_dir, 'src')
    
    required_dirs = [
        'quantum',
        'visualization',
        'analysis',
        'core',
        'dashboards',
        'monitoring'
    ]
    
    # Check src directories
    for dir_name in required_dirs:
        dir_path = os.path.join(src_dir, dir_name)
        assert os.path.isdir(dir_path), f"Required src directory '{dir_name}' is missing"

def test_quantum_module_files():
    """Test that all required quantum module files exist"""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    quantum_dir = os.path.join(root_dir, 'src', 'quantum')
    
    required_files = [
        '__init__.py',
        'historical_echoes.py',
        'playoff_amplification.py',
        'playoff_predictions.py',
        'rivalry_resonance.py',
        'run_predictions.py',
        'team_combinations.py',
        'team_fields.py'
    ]
    
    # Check quantum module files
    for file_name in required_files:
        file_path = os.path.join(quantum_dir, file_name)
        assert os.path.isfile(file_path), f"Required quantum module file '{file_name}' is missing"

def test_visualization_module_files():
    """Test that all required visualization module files exist"""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    viz_dir = os.path.join(root_dir, 'src', 'visualization')
    
    required_files = [
        '__init__.py',
        'enhanced_icons.py',
        'holographic.py',
        'lambeau_field.py',
        'nfl_icons.py',
        'nfl_team_icons.py',
        'team_matchups.py'
    ]
    
    # Check visualization module files
    for file_name in required_files:
        file_path = os.path.join(viz_dir, file_name)
        assert os.path.isfile(file_path), f"Required visualization file '{file_name}' is missing"

def test_test_files():
    """Test that all required test files exist"""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tests_dir = os.path.join(root_dir, 'tests')
    
    required_files = [
        '__init__.py',
        'test_historical_echoes.py',
        'test_playoff_amplification.py',
        'test_playoff_predictions.py',
        'test_rivalry_resonance.py',
        'test_team_combinations.py',
        'test_team_matchups.py',
        'test_project_structure.py'  # This file
    ]
    
    # Check test files
    for file_name in required_files:
        file_path = os.path.join(tests_dir, file_name)
        assert os.path.isfile(file_path), f"Required test file '{file_name}' is missing"

def test_documentation():
    """Test that required documentation exists"""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(root_dir, 'docs')
    
    required_files = [
        'architecture.md',
        'quantum_algorithms.md',
        'setup.md',
        'team_analysis.md',
        'usage.md'
    ]
    
    # Check documentation files
    for file_name in required_files:
        file_path = os.path.join(docs_dir, file_name)
        assert os.path.isfile(file_path), f"Required documentation file '{file_name}' is missing"
