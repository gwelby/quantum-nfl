"""
NFL Team Quantum Combinations
Special quantum interactions between teams, players, and environments
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple
import numpy as np
from rich.console import Console
from rich.table import Table
from ..visualization.nfl_team_icons import NFLTeamIcons

@dataclass
class QuantumCombo:
    """Special team quantum combination"""
    teams: List[str]
    name: str
    power: float
    effects: List[str]
    synergy: float
    special_plays: List[str]

class NFLCombinations:
    """NFL quantum combination system"""
    
    def __init__(self):
        self.console = Console()
        self.icons = NFLTeamIcons()
        
        # Define special combinations
        self.combos = {
            'Frozen Tundra Alliance': QuantumCombo(
                teams=['PACKERS', 'BILLS', 'VIKINGS'],
                name='Frozen Tundra Alliance',
                power=0.95,
                effects=['❄️ Arctic Blast', '🌨️ Snow Game Mastery', '🥶 Cold Front Defense'],
                synergy=0.93,
                special_plays=['Blizzard Blitz', 'Ice Wall Defense', 'Frost Route']
            ),
            'Coastal Energy Nexus': QuantumCombo(
                teams=['49ERS', 'SEAHAWKS', 'DOLPHINS'],
                name='Coastal Energy Nexus',
                power=0.92,
                effects=['🌊 Ocean Power', '🌉 Bridge Energy', '🏖️ Beach Force'],
                synergy=0.91,
                special_plays=['Tide Turn Play', 'Wave Runner', 'Beach Blitz']
            ),
            'Storm Front Coalition': QuantumCombo(
                teams=['BUCCANEERS', 'SAINTS', 'DOLPHINS'],
                name='Storm Front Coalition',
                power=0.94,
                effects=['⛈️ Thunder Strike', '🌪️ Hurricane Defense', '🌊 Tidal Surge'],
                synergy=0.92,
                special_plays=['Lightning Strike', 'Storm Surge', 'Hurricane Blitz']
            ),
            'Mountain Alliance': QuantumCombo(
                teams=['BRONCOS', 'CARDINALS', 'RAIDERS'],
                name='Mountain Alliance',
                power=0.93,
                effects=['🏔️ Peak Power', '🌵 Desert Force', '⛰️ Mountain Magic'],
                synergy=0.90,
                special_plays=['Altitude Attack', 'Mountain Pass', 'Peak Defense']
            ),
            'Industrial Powerhouse': QuantumCombo(
                teams=['STEELERS', 'BROWNS', 'LIONS'],
                name='Industrial Powerhouse',
                power=0.91,
                effects=['⚒️ Steel Force', '🏭 Factory Power', '🦾 Machine Strength'],
                synergy=0.89,
                special_plays=['Steel Curtain 2.0', 'Factory Floor Defense', 'Industrial Revolution']
            ),
            'Great Plains Thunder': QuantumCombo(
                teams=['CHIEFS', 'COWBOYS', 'TEXANS'],
                name='Great Plains Thunder',
                power=0.94,
                effects=['🌪️ Tornado Alley', '⚡ Lightning Strike', '🐎 Prairie Power'],
                synergy=0.92,
                special_plays=['Thunder Roll', 'Prairie Fire', 'Plains Sweep']
            ),
            'East Coast Energy': QuantumCombo(
                teams=['EAGLES', 'GIANTS', 'PATRIOTS'],
                name='East Coast Energy',
                power=0.93,
                effects=['🗽 Liberty Power', '🌆 City Energy', '🌊 Atlantic Force'],
                synergy=0.91,
                special_plays=['Liberty Strike', 'Metropolitan Blitz', 'Coastal Defense']
            ),
            'Heartland Heroes': QuantumCombo(
                teams=['PACKERS', 'BEARS', 'COLTS'],
                name='Heartland Heroes',
                power=0.95,
                effects=['🌾 Midwest Magic', '🏞️ Lake Effect', '🌪️ Tornado Defense'],
                synergy=0.94,
                special_plays=['Heartland Hustle', 'Midwest Muscle', 'Lake Effect Screen']
            )
        }
        
    def calculate_combo_power(self, combo: QuantumCombo) -> float:
        """Calculate combination's total power"""
        base_power = combo.power
        synergy_bonus = combo.synergy * 0.2
        effect_bonus = len(combo.effects) * 0.05
        play_bonus = len(combo.special_plays) * 0.05
        
        return min(base_power + synergy_bonus + effect_bonus + play_bonus, 1.0)
        
    def display_combo(self, combo_name: str):
        """Display team combination analysis"""
        if combo_name not in self.combos:
            self.console.print(f"[red]Combination {combo_name} not found![/red]")
            return
            
        combo = self.combos[combo_name]
        
        # Create title with team icons
        title = " + ".join([f"{self.icons.get_team_icon(team)} {team}" for team in combo.teams])
        table = Table(title=f"{title}\n{combo.name}")
        
        # Add columns
        table.add_column("Category", style="cyan")
        table.add_column("Details", style="yellow")
        table.add_column("Power", style="magenta")
        
        # Base metrics
        table.add_row(
            "Base Power",
            f"{combo.power:.2f}",
            "⚡" * int(combo.power * 5)
        )
        table.add_row(
            "Synergy",
            f"{combo.synergy:.2f}",
            "🔄" * int(combo.synergy * 5)
        )
        
        # Special effects
        effects_str = "\n".join(combo.effects)
        table.add_row("Effects", effects_str, "✨" * len(combo.effects))
        
        # Special plays
        plays_str = "\n".join(combo.special_plays)
        table.add_row("Special Plays", plays_str, "🎯" * len(combo.special_plays))
        
        # Total power
        total_power = self.calculate_combo_power(combo)
        table.add_row(
            "TOTAL POWER",
            f"{total_power:.2f}",
            "⭐" * int(total_power * 5)
        )
        
        self.console.print(table)
        
        # Special effects based on power
        if total_power > 0.95:
            self.console.print("\n[bold green]🌟 LEGENDARY COMBINATION! 🌟[/bold green]")
            self.console.print("This team combination creates extraordinary quantum synergy!")
        elif total_power > 0.9:
            self.console.print("\n[bold yellow]✨ Powerful Alliance! ✨[/bold yellow]")
            self.console.print("These teams form a formidable quantum bond!")
            
    def find_team_combos(self, team: str) -> List[str]:
        """Find all combinations for a team"""
        team_combos = []
        for name, combo in self.combos.items():
            if team in combo.teams:
                team_combos.append((name, self.calculate_combo_power(combo)))
                
        return sorted(team_combos, key=lambda x: x[1], reverse=True)
        
    def display_all_combos(self):
        """Display all team combinations"""
        self.console.print("\n🏈 NFL QUANTUM COMBINATIONS ANALYSIS\n")
        
        for combo_name in self.combos:
            self.display_combo(combo_name)
            self.console.print("\n" + "="*50 + "\n")
            
def main():
    combinations = NFLCombinations()
    
    # Display all combinations
    combinations.display_all_combos()
    
    # Find Packers combinations for Maria
    packers_combos = combinations.find_team_combos("PACKERS")
    print("\nPackers Special Combinations:")
    for combo, power in packers_combos:
        print(f"{combo}: {power:.2f}")

if __name__ == "__main__":
    main()
