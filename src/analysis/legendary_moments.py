"""
NFL Legendary Moments Analysis System
Quantum analysis of historic NFL moments across all teams
"""

from dataclasses import dataclass
from typing import Dict, List
from rich.console import Console
from rich.table import Table
from ..visualization.nfl_team_icons import NFLTeamIcons

@dataclass
class NFLMoment:
    team: str
    player: str
    year: int
    game: str
    impact: float
    energy: float
    resonance: float
    description: str

class NFLLegends:
    """NFL legends analysis system"""
    
    def __init__(self):
        self.console = Console()
        self.icons = NFLTeamIcons()
        
        # Historic moments for all teams
        self.moments = {
            'PACKERS': [
                NFLMoment("PACKERS", "Vince Lombardi", 1967, "Ice Bowl", 1.0, 0.98, 0.99, "The legendary Ice Bowl victory"),
                NFLMoment("PACKERS", "Bart Starr", 1967, "Ice Bowl", 0.99, 0.97, 0.98, "Game-winning QB sneak"),
                NFLMoment("PACKERS", "Brett Favre", 1996, "Super Bowl XXXI", 0.95, 0.94, 0.96, "Super Bowl triumph")
            ],
            'BEARS': [
                NFLMoment("BEARS", "Walter Payton", 1985, "Super Bowl XX", 0.98, 0.97, 0.96, "Sweetness dominates"),
                NFLMoment("BEARS", "Gale Sayers", 1965, "Six TD Game", 0.97, 0.96, 0.95, "Six touchdown performance")
            ],
            'CHIEFS': [
                NFLMoment("CHIEFS", "Patrick Mahomes", 2020, "Super Bowl LIV", 0.96, 0.97, 0.98, "Comeback victory"),
                NFLMoment("CHIEFS", "Len Dawson", 1970, "Super Bowl IV", 0.95, 0.94, 0.93, "First Super Bowl win")
            ],
            'STEELERS': [
                NFLMoment("STEELERS", "Franco Harris", 1972, "Immaculate Reception", 0.99, 0.98, 0.97, "Miraculous catch"),
                NFLMoment("STEELERS", "Mean Joe Greene", 1979, "Coke Commercial", 0.94, 0.93, 0.95, "Hey kid, catch!")
            ],
            'COWBOYS': [
                NFLMoment("COWBOYS", "Roger Staubach", 1975, "Hail Mary", 0.96, 0.95, 0.94, "Original Hail Mary pass"),
                NFLMoment("COWBOYS", "Emmitt Smith", 1995, "Record Rush", 0.95, 0.94, 0.93, "All-time rushing record")
            ],
            '49ERS': [
                NFLMoment("49ERS", "Joe Montana", 1982, "The Catch", 0.98, 0.97, 0.96, "Montana to Clark"),
                NFLMoment("49ERS", "Jerry Rice", 1995, "Record Game", 0.97, 0.96, 0.95, "Reception record")
            ],
            'BILLS': [
                NFLMoment("BILLS", "Don Beebe", 1993, "The Chase", 0.94, 0.93, 0.95, "Never give up play"),
                NFLMoment("BILLS", "Bruce Smith", 1990, "200th Sack", 0.93, 0.92, 0.94, "Defensive milestone")
            ],
            'RAIDERS': [
                NFLMoment("RAIDERS", "Marcus Allen", 1984, "Super Bowl Run", 0.96, 0.95, 0.94, "Reverse field run"),
                NFLMoment("RAIDERS", "Ken Stabler", 1974, "Sea of Hands", 0.95, 0.94, 0.93, "Miraculous TD")
            ]
            # Add more teams and moments as needed
        }
        
    def analyze_moment(self, moment: NFLMoment) -> Dict:
        """Analyze a legendary moment's quantum impact"""
        current_year = 2025
        time_factor = 1 - (current_year - moment.year) / 100
        
        resonance = moment.resonance * time_factor
        energy = moment.energy * time_factor
        impact = moment.impact * (resonance + energy) / 2
        
        return {
            'team': moment.team,
            'moment': f"{moment.player} - {moment.game}",
            'year': moment.year,
            'resonance': resonance,
            'energy': energy,
            'impact': impact,
            'description': moment.description
        }
        
    def display_team_moments(self, team: str):
        """Display analysis of a team's legendary moments"""
        if team not in self.moments:
            self.console.print(f"[red]No moments found for {team}![/red]")
            return
            
        team_icon = self.icons.get_team_icon(team)
        table = Table(title=f"{team_icon} {team} Legendary Moments")
        
        table.add_column("Moment", style="cyan")
        table.add_column("Year", style="yellow")
        table.add_column("Resonance", style="magenta")
        table.add_column("Energy", style="green")
        table.add_column("Impact", style="red")
        table.add_column("Description", style="blue")
        
        for moment in self.moments[team]:
            analysis = self.analyze_moment(moment)
            table.add_row(
                analysis['moment'],
                str(analysis['year']),
                "✨" * int(analysis['resonance'] * 5),
                "⚡" * int(analysis['energy'] * 5),
                "🌟" * int(analysis['impact'] * 5),
                analysis['description']
            )
            
        self.console.print(table)
        
    def get_team_legacy_power(self, team: str) -> float:
        """Calculate team's total legacy power"""
        if team not in self.moments:
            return 0.0
            
        total_power = sum(
            self.analyze_moment(moment)['impact']
            for moment in self.moments[team]
        )
        return total_power / len(self.moments[team])
        
    def display_all_teams(self):
        """Display legendary moments for all teams"""
        self.console.print("\n🏈 NFL LEGENDARY MOMENTS ANALYSIS\n")
        
        for team in self.moments:
            self.display_team_moments(team)
            legacy_power = self.get_team_legacy_power(team)
            self.console.print(
                f"\n{self.icons.get_team_icon(team)} {team} Legacy Power: "
                f"{'⭐' * int(legacy_power * 5)} ({legacy_power:.2f})\n"
            )
            
def main():
    legends = NFLLegends()
    legends.display_all_teams()

if __name__ == "__main__":
    main()
