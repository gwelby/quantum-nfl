"""Quantum NFL Discord Bot Example."""
import os
import discord
from discord.ext import commands
from quantum_nfl import QuantumNFL

class QuantumNFLBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!nfl ")
        self.quantum_client = QuantumNFL(api_key=os.getenv("NFL_API_KEY"))

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

    @commands.command(name="predict")
    async def predict_game(self, ctx, home_team: str, away_team: str):
        """Predict the outcome of a game using quantum analysis."""
        prediction = self.quantum_client.predict_game(home_team, away_team)
        
        embed = discord.Embed(title="🏈 Quantum Game Prediction")
        embed.add_field(name="Home Team", value=home_team, inline=True)
        embed.add_field(name="Away Team", value=away_team, inline=True)
        embed.add_field(name="Win Probability", 
                       value=f"{prediction['home_win_prob']:.2%}", 
                       inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name="quantum")
    async def quantum_state(self, ctx, team: str):
        """Get the quantum state of a team."""
        state = self.quantum_client.get_team_quantum_state(team)
        
        embed = discord.Embed(title="⚛️ Team Quantum State")
        embed.add_field(name="Team", value=team, inline=False)
        embed.add_field(name="Quantum Rating", 
                       value=f"{state['quantum_rating']:.2f}", 
                       inline=True)
        embed.add_field(name="Entanglement", 
                       value=f"{state['entanglement_factor']:.2f}", 
                       inline=True)
        
        await ctx.send(embed=embed)

def main():
    bot = QuantumNFLBot()
    bot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    main()
