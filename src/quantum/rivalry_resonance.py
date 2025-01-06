"""
NFL Rivalry Resonance System
Quantum analysis of historic NFL rivalries and their resonance patterns
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple
import numpy as np
from rich.console import Console
from rich.table import Table
from ..visualization.nfl_team_icons import NFLTeamIcons

@dataclass
class RivalryResonance:
    """NFL rivalry quantum resonance data"""
    
    teams: Tuple[str, str]  # Rival teams
    intensity: float        # Rivalry intensity
    history: float         # Historical weight
    fan_energy: float      # Fan interaction
    field_clash: float     # Field interference
    special_games: List[str]  # Notable matchups

class NFLRivalries:
    """NFL rivalry analysis system"""
    
    def __init__(self):
        self.console = Console()
        self.icons = NFLTeamIcons()
        
        # Define historic rivalries
        self.rivalries = {
            'PACKERS-BEARS': RivalryResonance(
                teams=('PACKERS', 'BEARS'),
                intensity=0.98,
                history=0.99,
                fan_energy=0.95,
                field_clash=0.97,
                special_games=['Ice Bowl', 'Christmas 2011', '100th Season Opener']
            ),
            'CHIEFS-RAIDERS': RivalryResonance(
                teams=('CHIEFS', 'RAIDERS'),
                intensity=0.94,
                history=0.93,
                fan_energy=0.95,
                field_clash=0.92,
                special_games=['Red Friday Showdown', 'Monday Night Classics']
            ),
            'COWBOYS-EAGLES': RivalryResonance(
                teams=('COWBOYS', 'EAGLES'),
                intensity=0.95,
                history=0.94,
                fan_energy=0.96,
                field_clash=0.93,
                special_games=['Bounty Bowl', 'Pickle Juice Game']
            ),
            'STEELERS-RAVENS': RivalryResonance(
                teams=('STEELERS', 'RAVENS'),
                intensity=0.96,
                history=0.92,
                fan_energy=0.97,
                field_clash=0.95,
                special_games=['Immaculate Extension', 'Division Clinchers']
            ),
            '49ERS-RAMS': RivalryResonance(
                teams=('49ERS', 'RAMS'),
                intensity=0.93,
                history=0.91,
                fan_energy=0.94,
                field_clash=0.92,
                special_games=['West Coast Battles', 'NFC Championship Games']
            )
            # Add more rivalries as needed
        }
        
    def calculate_resonance(self, rivalry: RivalryResonance) -> float:
        """Calculate rivalry resonance power"""
        base_power = (rivalry.intensity + 
                     rivalry.history + 
                     rivalry.fan_energy + 
                     rivalry.field_clash) / 4
                     
        game_bonus = len(rivalry.special_games) * 0.05
        return min(base_power + game_bonus, 1.0)
        
    def analyze_rivalry(self, team1: str, team2: str) -> Dict:
        """Analyze rivalry between two teams"""
        key = f"{team1}-{team2}"
        alt_key = f"{team2}-{team1}"
        
        rivalry = self.rivalries.get(key) or self.rivalries.get(alt_key)
        if not rivalry:
            return None
            
        resonance = self.calculate_resonance(rivalry)
        
        return {
            'teams': rivalry.teams,
            'resonance': resonance,
            'intensity': rivalry.intensity,
            'history': rivalry.history,
            'fan_energy': rivalry.fan_energy,
            'field_clash': rivalry.field_clash,
            'special_games': rivalry.special_games
        }
        
    def display_rivalry(self, team1: str, team2: str):
        """Display rivalry analysis"""
        analysis = self.analyze_rivalry(team1, team2)
        if not analysis:
            self.console.print(f"[red]No rivalry data found for {team1} vs {team2}![/red]")
            return
            
        # Create title with team icons
        title = (f"{self.icons.get_team_icon(team1)} {team1} vs "
                f"{team2} {self.icons.get_team_icon(team2)}")
        
        table = Table(title=title)
        
        # Add columns
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="yellow")
        table.add_column("Power", style="magenta")
        
        # Add metrics
        table.add_row(
            "Resonance",
            f"{analysis['resonance']:.2f}",
            "⚡" * int(analysis['resonance'] * 5)
        )
        table.add_row(
            "Intensity",
            f"{analysis['intensity']:.2f}",
            "🔥" * int(analysis['intensity'] * 5)
        )
        table.add_row(
            "History",
            f"{analysis['history']:.2f}",
            "📜" * int(analysis['history'] * 5)
        )
        table.add_row(
            "Fan Energy",
            f"{analysis['fan_energy']:.2f}",
            "🌟" * int(analysis['fan_energy'] * 5)
        )
        table.add_row(
            "Field Clash",
            f"{analysis['field_clash']:.2f}",
            "⚔️" * int(analysis['field_clash'] * 5)
        )
        
        self.console.print(table)
        
        # Display special games
        self.console.print("\n[cyan]Legendary Matchups:[/cyan]")
        for game in analysis['special_games']:
            self.console.print(f"🏈 {game}")
            
        # Special effects based on resonance
        if analysis['resonance'] > 0.95:
            self.console.print("\n[bold red]⚠️ EXTREME RIVALRY DETECTED! ⚠️[/bold red]")
            self.console.print("Quantum field interference at maximum levels!")
        elif analysis['resonance'] > 0.9:
            self.console.print("\n[bold yellow]🌟 High Rivalry Energy! 🌟[/bold yellow]")
            self.console.print("Significant quantum resonance observed!")
            
    def display_all_rivalries(self):
        """Display all NFL rivalries"""
        self.console.print("\n🏈 NFL RIVALRY RESONANCE ANALYSIS\n")
        
        for rivalry_key in self.rivalries:
            team1, team2 = rivalry_key.split('-')
            self.display_rivalry(team1, team2)
            self.console.print("\n" + "="*50 + "\n")
            
def main():
    rivalries = NFLRivalries()
    rivalries.display_all_rivalries()

if __name__ == "__main__":
    main()
