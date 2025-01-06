"""Quantum NFL Slack Bot Example."""
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from quantum_nfl import QuantumNFL

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
quantum_client = QuantumNFL(api_key=os.getenv("NFL_API_KEY"))

@app.command("/predict")
def predict_game(ack, respond, command):
    """Predict game outcome using quantum analysis."""
    ack()
    try:
        teams = command["text"].split()
        if len(teams) != 2:
            respond("Please provide home and away teams: `/predict GB CHI`")
            return

        home_team, away_team = teams
        prediction = quantum_client.predict_game(home_team, away_team)
        
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🏈 Quantum Game Prediction"
                }
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Home Team:* {home_team}"},
                    {"type": "mrkdwn", "text": f"*Away Team:* {away_team}"},
                    {"type": "mrkdwn", 
                     "text": f"*Win Probability:* {prediction['home_win_prob']:.2%}"}
                ]
            }
        ]
        
        respond(blocks=blocks)
    except Exception as e:
        respond(f"Error: {str(e)}")

@app.command("/quantum")
def quantum_state(ack, respond, command):
    """Get team's quantum state."""
    ack()
    try:
        team = command["text"].strip()
        state = quantum_client.get_team_quantum_state(team)
        
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "⚛️ Team Quantum State"
                }
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Team:* {team}"},
                    {"type": "mrkdwn", 
                     "text": f"*Quantum Rating:* {state['quantum_rating']:.2f}"},
                    {"type": "mrkdwn", 
                     "text": f"*Entanglement:* {state['entanglement_factor']:.2f}"}
                ]
            }
        ]
        
        respond(blocks=blocks)
    except Exception as e:
        respond(f"Error: {str(e)}")

def main():
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()

if __name__ == "__main__":
    main()
