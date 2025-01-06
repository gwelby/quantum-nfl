"""
NFL Playoff Quantum Amplification System
Advanced quantum analysis of playoff energy and amplification
"""

from dataclasses import dataclass
from typing import Dict, List
import numpy as np
from rich.console import Console
from rich.table import Table
from ..visualization.nfl_team_icons import NFLTeamIcons

@dataclass
class PlayoffAmplification:
    """Playoff quantum amplification metrics"""
    
    # Core Amplification
    base_power: float      # Team's base quantum power
    playoff_boost: float   # Playoff energy multiplier
    momentum: float        # Current momentum factor
    
    # Special Factors
    home_field: float     # Home field amplification
    experience: float     # Playoff experience bonus
    pressure: float       # Pressure handling factor
    
    # Historical Power
    legacy_factor: float  # Historical playoff success
    clutch_rating: float  # Critical moment performance
    dynasty_power: float  # Dynasty potential

class NFLPlayoffs:
    """NFL playoff quantum analysis system"""
    
    def __init__(self):
        self.console = Console()
        self.icons = NFLTeamIcons()
        
    def calculate_amplification(self, metrics: PlayoffAmplification) -> float:
        """Calculate total playoff amplification"""
        core_amp = (metrics.base_power * 
                   metrics.playoff_boost * 
                   metrics.momentum)
                   
        special_amp = (metrics.home_field +
                      metrics.experience +
                      metrics.pressure) / 3
                      
        history_amp = (metrics.legacy_factor +
                      metrics.clutch_rating +
                      metrics.dynasty_power) / 3
                      
        return (core_amp * 0.4 + 
                special_amp * 0.3 + 
                history_amp * 0.3)
                
    def display_amplification(self, team: str, metrics: PlayoffAmplification):
        """Display team's playoff amplification"""
        table = Table(title=f"{self.icons.get_team_icon(team)} {team} Playoff Quantum Amplification")
        
        # Add columns
        table.add_column("Category", style="cyan")
        table.add_column("Metric", style="yellow")
        table.add_column("Value", style="green")
        table.add_column("Amplification", style="magenta")
        
        # Core metrics
        table.add_row(
            "Core",
            "Base Power",
            f"{metrics.base_power:.2f}",
            "⚡" * int(metrics.base_power * 5)
        )
        table.add_row(
            "",
            "Playoff Boost",
            f"{metrics.playoff_boost:.2f}",
            "🔋" * int(metrics.playoff_boost * 5)
        )
        table.add_row(
            "",
            "Momentum",
            f"{metrics.momentum:.2f}",
            "🌊" * int(metrics.momentum * 5)
        )
        
        # Special factors
        table.add_row(
            "Special",
            "Home Field",
            f"{metrics.home_field:.2f}",
            "🏟️" * int(metrics.home_field * 5)
        )
        table.add_row(
            "",
            "Experience",
            f"{metrics.experience:.2f}",
            "📚" * int(metrics.experience * 5)
        )
        table.add_row(
            "",
            "Pressure",
            f"{metrics.pressure:.2f}",
            "💎" * int(metrics.pressure * 5)
        )
        
        # Historical power
        table.add_row(
            "Historical",
            "Legacy",
            f"{metrics.legacy_factor:.2f}",
            "🏆" * int(metrics.legacy_factor * 5)
        )
        table.add_row(
            "",
            "Clutch",
            f"{metrics.clutch_rating:.2f}",
            "✨" * int(metrics.clutch_rating * 5)
        )
        table.add_row(
            "",
            "Dynasty",
            f"{metrics.dynasty_power:.2f}",
            "👑" * int(metrics.dynasty_power * 5)
        )
        
        # Calculate total amplification
        total_amp = self.calculate_amplification(metrics)
        
        table.add_row(
            "TOTAL",
            "Amplification",
            f"{total_amp:.2f}",
            "⭐" * int(total_amp * 5)
        )
        
        self.console.print(table)
        
        # Special effects based on amplification
        if total_amp > 0.9:
            self.console.print("\n[bold green]🌟 SUPREME PLAYOFF POWER! 🌟[/bold green]")
            self.console.print("Quantum amplification at championship levels!")
            self.console.print(f"Expected Power Increase: {(total_amp - 1) * 100:.1f}%")
        elif total_amp > 0.8:
            self.console.print("\n[bold yellow]⚡ Strong Playoff Energy! ⚡[/bold yellow]")
            self.console.print("Significant quantum amplification detected!")
            
    def simulate_playoff_run(self, team: str, metrics: PlayoffAmplification):
        """Simulate team's playoff quantum trajectory"""
        base_amp = self.calculate_amplification(metrics)
        rounds = ['Wild Card', 'Divisional', 'Conference', 'Super Bowl']
        
        self.console.print(f"\n[cyan]Playoff Quantum Trajectory - {team}[/cyan]")
        
        current_power = base_amp
        for round_name in rounds:
            # Increase power with each round
            round_boost = np.random.uniform(0.05, 0.15)
            current_power *= (1 + round_boost)
            
            self.console.print(f"\n{round_name} Round:")
            self.console.print(f"Power Level: {'⚡' * int(current_power * 5)} ({current_power:.2f})")
            self.console.print(f"Quantum Boost: +{round_boost*100:.1f}%")
            
            # Special events
            if current_power > 1.5:
                self.console.print("[bold red]!!! QUANTUM SURGE DETECTED !!![/bold red]")
            elif current_power > 1.2:
                self.console.print("[bold yellow]>> High Energy State <<[/bold yellow]")
                
def main():
    playoffs = NFLPlayoffs()
    
    # Example: Packers playoff metrics
    packers_metrics = PlayoffAmplification(
        base_power=0.92,
        playoff_boost=0.95,
        momentum=0.93,
        home_field=0.96,
        experience=0.94,
        pressure=0.91,
        legacy_factor=0.97,
        clutch_rating=0.93,
        dynasty_power=0.94
    )
    
    # Display amplification
    playoffs.display_amplification("PACKERS", packers_metrics)
    
    # Simulate playoff run
    playoffs.simulate_playoff_run("PACKERS", packers_metrics)

if __name__ == "__main__":
    main()
