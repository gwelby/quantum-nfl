"""
Packers Legends Analysis System
Quantum analysis of Packers legendary players and moments
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, List
from rich.console import Console
from rich.table import Table
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.visualization.nfl_team_icons import NFLTeamIcons

@dataclass
class LegendaryMoment:
    """Represents a legendary Packers moment"""
    player: str
    year: int
    game: str
    impact: float  # 0-1 historical impact
    energy: float  # 0-1 quantum energy
    resonance: float  # 0-1 current resonance
    description: str

class PackersLegends:
    """Packers legends analysis system"""
    
    def __init__(self):
        self.console = Console()
        self.icons = NFLTeamIcons()
        
        # Initialize legendary moments
        self.moments = [
            LegendaryMoment(
                "Bart Starr",
                1967,
                "Ice Bowl",
                1.0,  # Maximum impact
                0.95,  # High energy
                0.98,  # High resonance
                "QB sneak to win NFL Championship"
            ),
            LegendaryMoment(
                "Brett Favre",
                1996,
                "Super Bowl XXXI",
                0.95,
                0.93,
                0.94,
                "Super Bowl victory over Patriots"
            ),
            LegendaryMoment(
                "Aaron Rodgers",
                2010,
                "Super Bowl XLV",
                0.93,
                0.92,
                0.96,
                "Super Bowl MVP performance"
            ),
            # Add more legendary moments
        ]
        
        # Initialize legendary players
        self.legends = {
            "Bart Starr": {
                "position": "QB",
                "years": "1956-1971",
                "championships": 5,
                "quantum_legacy": 0.98,
                "field_impact": 0.99
            },
            "Brett Favre": {
                "position": "QB",
                "years": "1992-2007",
                "championships": 1,
                "quantum_legacy": 0.96,
                "field_impact": 0.97
            },
            "Aaron Rodgers": {
                "position": "QB",
                "years": "2005-2022",
                "championships": 1,
                "quantum_legacy": 0.95,
                "field_impact": 0.96
            },
            "Don Hutson": {
                "position": "WR/DB",
                "years": "1935-1945",
                "championships": 3,
                "quantum_legacy": 0.97,
                "field_impact": 0.98
            },
            "Ray Nitschke": {
                "position": "LB",
                "years": "1958-1972",
                "championships": 5,
                "quantum_legacy": 0.94,
                "field_impact": 0.95
            }
        }
        
    def analyze_legend(self, name: str) -> Dict:
        """Analyze a Packers legend's quantum impact"""
        if name not in self.legends:
            return None
            
        legend = self.legends[name]
        
        # Calculate quantum metrics
        legacy_power = legend['quantum_legacy'] * legend['field_impact']
        championship_factor = legend['championships'] * 0.1
        years_active = int(legend['years'].split('-')[1]) - int(legend['years'].split('-')[0])
        longevity_factor = min(years_active * 0.02, 0.5)
        
        return {
            'name': name,
            'position': legend['position'],
            'legacy_power': legacy_power,
            'championship_impact': championship_factor,
            'longevity_impact': longevity_factor,
            'total_impact': (legacy_power + championship_factor + longevity_factor) / 3
        }
        
    def display_legend_analysis(self, name: str):
        """Display analysis of a Packers legend"""
        analysis = self.analyze_legend(name)
        if not analysis:
            self.console.print(f"[red]Legend {name} not found![/red]")
            return
            
        table = Table(title=f"{self.icons.get_team_icon('PACKERS')} {name} Legend Analysis")
        
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_column("Impact", style="green")
        
        table.add_row(
            "Legacy Power",
            f"{analysis['legacy_power']:.2f}",
            "🌟" * int(analysis['legacy_power'] * 5)
        )
        table.add_row(
            "Championship Impact",
            f"{analysis['championship_impact']:.2f}",
            "🏆" * int(analysis['championship_impact'] * 10)
        )
        table.add_row(
            "Longevity Impact",
            f"{analysis['longevity_impact']:.2f}",
            "📈" * int(analysis['longevity_impact'] * 10)
        )
        table.add_row(
            "Total Impact",
            f"{analysis['total_impact']:.2f}",
            "⭐" * int(analysis['total_impact'] * 5)
        )
        
        self.console.print(table)
        
    def analyze_legendary_moment(self, moment: LegendaryMoment) -> Dict:
        """Analyze a legendary moment's quantum resonance"""
        current_year = 2025
        time_factor = 1 - (current_year - moment.year) / 100  # Time decay
        
        resonance = moment.resonance * time_factor
        energy = moment.energy * time_factor
        impact = moment.impact * (resonance + energy) / 2
        
        return {
            'moment': f"{moment.player} - {moment.game}",
            'year': moment.year,
            'resonance': resonance,
            'energy': energy,
            'impact': impact,
            'description': moment.description
        }
        
    def display_legendary_moments(self):
        """Display analysis of legendary Packers moments"""
        table = Table(title=f"{self.icons.get_team_icon('PACKERS')} Legendary Moments")
        
        table.add_column("Moment", style="cyan")
        table.add_column("Year", style="yellow")
        table.add_column("Resonance", style="magenta")
        table.add_column("Energy", style="green")
        table.add_column("Impact", style="red")
        
        for moment in self.moments:
            analysis = self.analyze_legendary_moment(moment)
            table.add_row(
                analysis['moment'],
                str(analysis['year']),
                "✨" * int(analysis['resonance'] * 5),
                "⚡" * int(analysis['energy'] * 5),
                "🌟" * int(analysis['impact'] * 5)
            )
            
        self.console.print(table)
        
    def get_legacy_power(self) -> float:
        """Calculate total Packers legacy power"""
        total_power = 0.0
        for legend in self.legends.values():
            total_power += legend['quantum_legacy'] * legend['field_impact']
        return total_power / len(self.legends)

    def get_championship_resonance(self) -> float:
        """Calculate championship resonance"""
        total_championships = sum(legend['championships'] for legend in self.legends.values())
        return min(total_championships * 0.1, 1.0)

    def calculate_team_quantum_state(self) -> Dict:
        """Calculate overall team quantum state"""
        legacy_power = self.get_legacy_power()
        championship_resonance = self.get_championship_resonance()
        moment_impact = sum(moment.impact for moment in self.moments) / len(self.moments)
        
        return {
            'legacy_power': legacy_power,
            'championship_resonance': championship_resonance,
            'moment_impact': moment_impact,
            'total_quantum_state': (legacy_power + championship_resonance + moment_impact) / 3
        }

    def display_team_quantum_state(self):
        """Display team quantum state analysis"""
        state = self.calculate_team_quantum_state()
        
        table = Table(title=f"{self.icons.get_team_icon('PACKERS')} Team Quantum State")
        
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_column("Visualization", style="green")
        
        table.add_row(
            "Legacy Power",
            f"{state['legacy_power']:.2f}",
            "🏈" * int(state['legacy_power'] * 10)
        )
        table.add_row(
            "Championship Resonance",
            f"{state['championship_resonance']:.2f}",
            "🏆" * int(state['championship_resonance'] * 10)
        )
        table.add_row(
            "Moment Impact",
            f"{state['moment_impact']:.2f}",
            "✨" * int(state['moment_impact'] * 10)
        )
        table.add_row(
            "Total Quantum State",
            f"{state['total_quantum_state']:.2f}",
            "⭐" * int(state['total_quantum_state'] * 10)
        )
        
        self.console.print(table)

def main():
    """Main function to demonstrate Packers legends analysis"""
    legends = PackersLegends()
    
    # Display individual legend analysis
    legends.display_legend_analysis("Bart Starr")
    legends.display_legend_analysis("Brett Favre")
    legends.display_legend_analysis("Aaron Rodgers")
    
    # Display legendary moments
    legends.display_legendary_moments()
    
    # Display team quantum state
    legends.display_team_quantum_state()

if __name__ == "__main__":
    main()
