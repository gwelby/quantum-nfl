"""
NFL Team Matchup Quantum Visualization
Advanced visualization for team matchups and quantum interactions
"""

import numpy as np
import plotly.graph_objects as go
from dataclasses import dataclass
from typing import Dict, List, Tuple
from .nfl_team_icons import NFLTeamIcons

@dataclass
class TeamQuantumState:
    """Team's quantum state"""
    offense_power: float
    defense_power: float
    momentum: float
    fan_energy: float
    field_advantage: float
    quantum_sync: float

class TeamMatchups:
    """NFL team matchup visualization system"""
    
    def __init__(self):
        self.icons = NFLTeamIcons()
        
    def calculate_quantum_interference(self, 
                                    team1: TeamQuantumState, 
                                    team2: TeamQuantumState) -> np.ndarray:
        """Calculate quantum interference between teams"""
        # Create interference pattern
        x = np.linspace(0, 100, 100)
        y = np.linspace(0, 100, 100)
        X, Y = np.meshgrid(x, y)
        
        # Team 1 wave
        wave1 = (team1.offense_power * np.sin(X/10) + 
                team1.defense_power * np.cos(Y/10)) * team1.momentum
                
        # Team 2 wave
        wave2 = (team2.offense_power * np.sin(X/10) + 
                team2.defense_power * np.cos(Y/10)) * team2.momentum
                
        # Calculate interference
        interference = wave1 + wave2
        return interference
        
    def create_matchup_visualization(self,
                                   team1: str,
                                   team2: str,
                                   team1_state: TeamQuantumState,
                                   team2_state: TeamQuantumState) -> go.Figure:
        """Create visualization for team matchup"""
        fig = go.Figure()
        
        # Calculate interference pattern
        interference = self.calculate_quantum_interference(team1_state, team2_state)
        
        # Add interference surface
        fig.add_trace(go.Surface(
            z=interference,
            colorscale='Viridis',
            name='Quantum Interference'
        ))
        
        # Add team markers
        fig.add_trace(go.Scatter3d(
            x=[25],
            y=[25],
            z=[np.max(interference)],
            mode='text',
            text=[self.icons.get_team_icon(team1)],
            textfont=dict(size=20),
            name=team1
        ))
        
        fig.add_trace(go.Scatter3d(
            x=[75],
            y=[75],
            z=[np.max(interference)],
            mode='text',
            text=[self.icons.get_team_icon(team2)],
            textfont=dict(size=20),
            name=team2
        ))
        
        # Add quantum metrics
        metrics1 = f"""
        Offense: {'⚡' * int(team1_state.offense_power * 5)}
        Defense: {'🛡️' * int(team1_state.defense_power * 5)}
        Momentum: {'🌊' * int(team1_state.momentum * 5)}
        Fan Energy: {'🔥' * int(team1_state.fan_energy * 5)}
        Field Advantage: {'🏟️' * int(team1_state.field_advantage * 5)}
        Quantum Sync: {'✨' * int(team1_state.quantum_sync * 5)}
        """
        
        metrics2 = f"""
        Offense: {'⚡' * int(team2_state.offense_power * 5)}
        Defense: {'🛡️' * int(team2_state.defense_power * 5)}
        Momentum: {'🌊' * int(team2_state.momentum * 5)}
        Fan Energy: {'🔥' * int(team2_state.fan_energy * 5)}
        Field Advantage: {'🏟️' * int(team2_state.field_advantage * 5)}
        Quantum Sync: {'✨' * int(team2_state.quantum_sync * 5)}
        """
        
        fig.add_annotation(
            x=0, y=0,
            text=metrics1,
            showarrow=False,
            xanchor='left',
            yanchor='bottom'
        )
        
        fig.add_annotation(
            x=100, y=100,
            text=metrics2,
            showarrow=False,
            xanchor='right',
            yanchor='top'
        )
        
        # Update layout
        fig.update_layout(
            title=f"{self.icons.get_team_icon(team1)} {team1} vs {team2} {self.icons.get_team_icon(team2)}",
            scene=dict(
                xaxis_title="Field Position",
                yaxis_title="Time",
                zaxis_title="Quantum State"
            ),
            showlegend=True
        )
        
        return fig
        
    def analyze_matchup(self,
                       team1: str,
                       team2: str,
                       team1_state: TeamQuantumState,
                       team2_state: TeamQuantumState) -> Dict:
        """Analyze quantum matchup between teams"""
        # Calculate advantage metrics
        offense_advantage = team1_state.offense_power - team2_state.defense_power
        defense_advantage = team1_state.defense_power - team2_state.offense_power
        momentum_factor = team1_state.momentum / team2_state.momentum
        energy_factor = team1_state.fan_energy * team1_state.field_advantage
        sync_factor = team1_state.quantum_sync / team2_state.quantum_sync
        
        # Calculate overall advantage
        total_advantage = (offense_advantage + 
                         defense_advantage + 
                         momentum_factor + 
                         energy_factor + 
                         sync_factor) / 5
                         
        return {
            'team1': team1,
            'team2': team2,
            'offense_advantage': offense_advantage,
            'defense_advantage': defense_advantage,
            'momentum_factor': momentum_factor,
            'energy_factor': energy_factor,
            'sync_factor': sync_factor,
            'total_advantage': total_advantage
        }
        
    def display_matchup(self,
                       team1: str,
                       team2: str,
                       team1_state: TeamQuantumState,
                       team2_state: TeamQuantumState):
        """Display complete matchup analysis"""
        # Create visualization
        fig = self.create_matchup_visualization(team1, team2, team1_state, team2_state)
        
        # Analyze matchup
        analysis = self.analyze_matchup(team1, team2, team1_state, team2_state)
        
        # Display results
        print(f"\n{self.icons.get_team_icon(team1)} {team1} vs {team2} {self.icons.get_team_icon(team2)}")
        print("\nQuantum Advantage Analysis:")
        print(f"Offense: {'▲' if analysis['offense_advantage'] > 0 else '▼'} {abs(analysis['offense_advantage']):.2f}")
        print(f"Defense: {'▲' if analysis['defense_advantage'] > 0 else '▼'} {abs(analysis['defense_advantage']):.2f}")
        print(f"Momentum: {'▲' if analysis['momentum_factor'] > 1 else '▼'} {abs(analysis['momentum_factor']):.2f}")
        print(f"Energy: {'▲' if analysis['energy_factor'] > 1 else '▼'} {abs(analysis['energy_factor']):.2f}")
        print(f"Sync: {'▲' if analysis['sync_factor'] > 1 else '▼'} {abs(analysis['sync_factor']):.2f}")
        print(f"\nTotal Advantage: {'▲' if analysis['total_advantage'] > 0 else '▼'} {abs(analysis['total_advantage']):.2f}")
        
        # Show visualization
        fig.show()
        
def main():
    # Example usage
    matchups = TeamMatchups()
    
    # Create sample states
    packers_state = TeamQuantumState(0.9, 0.85, 0.95, 0.9, 1.0, 0.92)
    bears_state = TeamQuantumState(0.82, 0.88, 0.87, 0.85, 0.9, 0.89)
    
    # Display matchup
    matchups.display_matchup("PACKERS", "BEARS", packers_state, bears_state)

if __name__ == "__main__":
    main()
