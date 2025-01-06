"""
NFL Historical Echoes System
Advanced analysis of quantum echoes from historic NFL moments
"""

from dataclasses import dataclass
from typing import Dict, List
import numpy as np
from rich.console import Console
from rich.table import Table
from ..visualization.nfl_team_icons import NFLTeamIcons

@dataclass
class HistoricalEcho:
    """NFL historical quantum echo data"""
    
    # Event Data
    year: int
    event: str
    team: str
    impact: float
    
    # Echo Properties
    resonance: float      # Current resonance strength
    frequency: float      # Echo frequency
    amplitude: float      # Echo amplitude
    
    # Time Effects
    decay_rate: float    # Temporal decay
    persistence: float   # Echo persistence
    revival_power: float # Potential for revival

class NFLHistory:
    """NFL historical quantum analysis system"""
    
    def __init__(self):
        self.console = Console()
        self.icons = NFLTeamIcons()
        
        # Initialize historical echoes
        self.echoes = {
            'Ice Bowl': HistoricalEcho(
                year=1967,
                event="Ice Bowl",
                team="PACKERS",
                impact=1.0,
                resonance=0.95,
                frequency=0.92,
                amplitude=0.94,
                decay_rate=0.001,
                persistence=0.96,
                revival_power=0.93
            ),
            'Immaculate Reception': HistoricalEcho(
                year=1972,
                event="Immaculate Reception",
                team="STEELERS",
                impact=0.98,
                resonance=0.94,
                frequency=0.93,
                amplitude=0.92,
                decay_rate=0.002,
                persistence=0.95,
                revival_power=0.91
            ),
            'The Catch': HistoricalEcho(
                year=1982,
                event="The Catch",
                team="49ERS",
                impact=0.97,
                resonance=0.93,
                frequency=0.91,
                amplitude=0.94,
                decay_rate=0.002,
                persistence=0.94,
                revival_power=0.92
            ),
            'Music City Miracle': HistoricalEcho(
                year=2000,
                event="Music City Miracle",
                team="TITANS",
                impact=0.96,
                resonance=0.92,
                frequency=0.90,
                amplitude=0.93,
                decay_rate=0.003,
                persistence=0.93,
                revival_power=0.90
            ),
            'Helmet Catch': HistoricalEcho(
                year=2008,
                event="Helmet Catch",
                team="GIANTS",
                impact=0.97,
                resonance=0.93,
                frequency=0.92,
                amplitude=0.94,
                decay_rate=0.002,
                persistence=0.94,
                revival_power=0.91
            ),
            'Minneapolis Miracle': HistoricalEcho(
                year=2018,
                event="Minneapolis Miracle",
                team="VIKINGS",
                impact=0.95,
                resonance=0.94,
                frequency=0.93,
                amplitude=0.92,
                decay_rate=0.002,
                persistence=0.93,
                revival_power=0.92
            )
        }
        
    def calculate_current_strength(self, echo: HistoricalEcho) -> float:
        """Calculate current echo strength"""
        current_year = 2025
        years_passed = current_year - echo.year
        
        # Calculate temporal decay
        decay = 1 - (years_passed * echo.decay_rate)
        decay = max(decay, echo.persistence)  # Can't decay below persistence
        
        # Calculate current strength
        base_strength = (echo.resonance + echo.frequency + echo.amplitude) / 3
        current_strength = base_strength * decay
        
        # Add revival potential
        revival_boost = echo.revival_power * np.sin(years_passed / 10) * 0.1
        current_strength += revival_boost
        
        return min(current_strength, 1.0)
        
    def analyze_echo(self, event: str) -> Dict:
        """Analyze a historical echo"""
        if event not in self.echoes:
            return None
            
        echo = self.echoes[event]
        current_strength = self.calculate_current_strength(echo)
        
        return {
            'event': event,
            'team': echo.team,
            'year': echo.year,
            'impact': echo.impact,
            'current_strength': current_strength,
            'resonance': echo.resonance,
            'frequency': echo.frequency,
            'amplitude': echo.amplitude,
            'persistence': echo.persistence,
            'revival_power': echo.revival_power
        }
        
    def display_echo(self, event: str):
        """Display historical echo analysis"""
        analysis = self.analyze_echo(event)
        if not analysis:
            self.console.print(f"[red]Echo {event} not found![/red]")
            return
            
        team_icon = self.icons.get_team_icon(analysis['team'])
        table = Table(title=f"{team_icon} {event} ({analysis['year']}) - Historical Echo")
        
        # Add columns
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="yellow")
        table.add_column("Strength", style="magenta")
        
        # Add metrics
        table.add_row(
            "Impact",
            f"{analysis['impact']:.2f}",
            "💥" * int(analysis['impact'] * 5)
        )
        table.add_row(
            "Current Strength",
            f"{analysis['current_strength']:.2f}",
            "⚡" * int(analysis['current_strength'] * 5)
        )
        table.add_row(
            "Resonance",
            f"{analysis['resonance']:.2f}",
            "✨" * int(analysis['resonance'] * 5)
        )
        table.add_row(
            "Frequency",
            f"{analysis['frequency']:.2f}",
            "🌊" * int(analysis['frequency'] * 5)
        )
        table.add_row(
            "Amplitude",
            f"{analysis['amplitude']:.2f}",
            "📊" * int(analysis['amplitude'] * 5)
        )
        table.add_row(
            "Persistence",
            f"{analysis['persistence']:.2f}",
            "🔒" * int(analysis['persistence'] * 5)
        )
        table.add_row(
            "Revival Power",
            f"{analysis['revival_power']:.2f}",
            "🔄" * int(analysis['revival_power'] * 5)
        )
        
        self.console.print(table)
        
        # Special effects based on strength
        if analysis['current_strength'] > 0.9:
            self.console.print("\n[bold green]🌟 LEGENDARY ECHO DETECTED! 🌟[/bold green]")
            self.console.print("This moment's quantum signature remains incredibly powerful!")
        elif analysis['current_strength'] > 0.8:
            self.console.print("\n[bold yellow]✨ Strong Historical Echo! ✨[/bold yellow]")
            self.console.print("This moment continues to resonate through time!")
            
    def display_all_echoes(self):
        """Display all historical echoes"""
        self.console.print("\n🏈 NFL HISTORICAL ECHOES ANALYSIS\n")
        
        for event in self.echoes:
            self.display_echo(event)
            self.console.print("\n" + "="*50 + "\n")
            
    def find_resonating_echoes(self, team: str) -> List[str]:
        """Find strongly resonating echoes for a team"""
        resonating = []
        for event, echo in self.echoes.items():
            if echo.team == team:
                strength = self.calculate_current_strength(echo)
                if strength > 0.8:
                    resonating.append((event, strength))
                    
        return sorted(resonating, key=lambda x: x[1], reverse=True)
        
def main():
    history = NFLHistory()
    
    # Display all echoes
    history.display_all_echoes()
    
    # Find resonating echoes for Packers
    packers_echoes = history.find_resonating_echoes("PACKERS")
    print("\nStrongly Resonating Packers Echoes:")
    for event, strength in packers_echoes:
        print(f"{event}: {strength:.2f}")

if __name__ == "__main__":
    main()
