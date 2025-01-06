#!/usr/bin/env python3
"""Quantum NFL CLI Tool."""
import click
import rich
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from quantum_nfl import QuantumNFL

console = Console()

@click.group()
@click.version_option()
def cli():
    """Quantum NFL Command Line Interface."""
    pass

@cli.command()
@click.argument('home_team')
@click.argument('away_team')
@click.option('--detailed', is_flag=True, help='Show detailed quantum analysis')
def predict(home_team, away_team, detailed):
    """Predict game outcome using quantum analysis."""
    with Progress() as progress:
        task = progress.add_task("[cyan]Calculating quantum states...", total=100)
        
        client = QuantumNFL()
        prediction = client.predict_game(home_team, away_team, detailed=detailed)
        
        progress.update(task, advance=100)
    
    table = Table(title="Game Prediction")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Home Team", home_team)
    table.add_row("Away Team", away_team)
    table.add_row("Win Probability", f"{prediction['home_win_prob']:.2%}")
    
    if detailed:
        table.add_row("Quantum Rating", f"{prediction['quantum_rating']:.2f}")
        table.add_row("Entanglement", f"{prediction['entanglement']:.2f}")
    
    console.print(table)

@cli.command()
@click.argument('team')
def quantum(team):
    """Get team's quantum state."""
    client = QuantumNFL()
    state = client.get_team_quantum_state(team)
    
    table = Table(title="Team Quantum State")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    for key, value in state.items():
        table.add_row(key.replace('_', ' ').title(), f"{value:.2f}")
    
    console.print(table)

@cli.command()
@click.argument('team1')
@click.argument('team2')
def rivalry(team1, team2):
    """Analyze rivalry quantum effects."""
    client = QuantumNFL()
    analysis = client.analyze_rivalry(team1, team2)
    
    table = Table(title="Rivalry Analysis")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Resonance", f"{analysis['resonance']:.2f}")
    table.add_row("Historical Echo", f"{analysis['echo']:.2f}")
    table.add_row("Interference", f"{analysis['interference']:.2f}")
    
    console.print(table)

@cli.command()
def simulate_season():
    """Simulate entire NFL season with quantum effects."""
    with Progress() as progress:
        task = progress.add_task("[cyan]Simulating season...", total=100)
        
        client = QuantumNFL()
        results = client.simulate_season()
        
        progress.update(task, advance=100)
    
    table = Table(title="Season Simulation")
    table.add_column("Team", style="cyan")
    table.add_column("Wins", style="magenta")
    table.add_column("Quantum Rating", style="blue")
    
    for team in sorted(results, key=lambda x: x['wins'], reverse=True):
        table.add_row(
            team['name'],
            str(team['wins']),
            f"{team['quantum_rating']:.2f}"
        )
    
    console.print(table)

if __name__ == '__main__':
    cli()
