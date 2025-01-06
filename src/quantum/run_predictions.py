"""
Runner script for NFL Quantum Predictions with Unicode support
"""
import sys
import os
import codecs

# Force UTF-8 encoding for stdout
if sys.platform == 'win32':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    os.system('chcp 65001')

from playoff_predictions import NFLPlayoffPredictor, PlayoffTeam

def main():
    predictor = NFLPlayoffPredictor()
    
    # Example playoff teams
    playoff_teams = [
        PlayoffTeam("PACKERS", 1, 0.95, 0.92, 0.94, 0.93, 0.96, 0.91),
        PlayoffTeam("49ERS", 2, 0.93, 0.94, 0.92, 0.91, 0.95, 0.93),
        PlayoffTeam("EAGLES", 3, 0.92, 0.91, 0.90, 0.94, 0.93, 0.92),
        PlayoffTeam("COWBOYS", 4, 0.91, 0.93, 0.91, 0.92, 0.94, 0.90),
        PlayoffTeam("CHIEFS", 1, 0.94, 0.95, 0.93, 0.95, 0.96, 0.92),
        PlayoffTeam("BILLS", 2, 0.93, 0.92, 0.91, 0.93, 0.94, 0.91),
        PlayoffTeam("RAVENS", 3, 0.92, 0.90, 0.89, 0.91, 0.93, 0.94),
        PlayoffTeam("BENGALS", 4, 0.91, 0.89, 0.90, 0.92, 0.91, 0.93)
    ]
    
    # Simulate playoffs
    predictor.simulate_playoff_bracket(playoff_teams)

if __name__ == "__main__":
    main()
