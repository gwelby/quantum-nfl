"""
QuantumHumanLearner - Learning from real NFL data how quantum and human elements interact
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass
import logging
from quantum_human_bridge import QuantumHumanBridge, QuantumHumanState
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import os

@dataclass
class PlayOutcome:
    success: bool
    yards_gained: float
    expected_yards: float
    creativity_score: float
    quantum_alignment: float
    human_factor: float
    emotional_momentum: float

class QuantumHumanLearner:
    def __init__(self, data_path: str = "data/nfl_plays.csv"):
        self.bridge = QuantumHumanBridge()
        self.data_path = data_path
        self.scaler = StandardScaler()
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.logger = logging.getLogger(__name__)
        
        # Create models for different aspects
        self.creativity_model = RandomForestRegressor(n_estimators=100)
        self.quantum_model = RandomForestRegressor(n_estimators=100)
        self.human_model = RandomForestRegressor(n_estimators=100)
        
    def collect_play_data(self, play_data: Dict) -> PlayOutcome:
        """Analyze a single play and collect quantum-human metrics."""
        # Extract basic play information
        formation = play_data.get('formation', '')
        play_type = play_data.get('play_type', '')
        down = play_data.get('down', 1)
        distance = play_data.get('distance', 10)
        
        # Calculate quantum metrics
        quantum_state = self._calculate_quantum_metrics(play_data)
        
        # Calculate human factors
        human_factors = self._calculate_human_factors(play_data)
        
        # Calculate creativity score
        creativity = self._calculate_creativity_score(play_data, quantum_state, human_factors)
        
        return PlayOutcome(
            success=play_data.get('success', False),
            yards_gained=play_data.get('yards_gained', 0),
            expected_yards=play_data.get('expected_yards', 0),
            creativity_score=creativity,
            quantum_alignment=quantum_state['alignment'],
            human_factor=human_factors['spontaneity'],
            emotional_momentum=human_factors['emotional_momentum']
        )
    
    def learn_from_historical_data(self, plays_df: pd.DataFrame):
        """Learn patterns from historical play data."""
        features = self._extract_features(plays_df)
        
        # Train creativity model
        creativity_target = plays_df['yards_gained'] - plays_df['expected_yards']
        self.creativity_model.fit(features, creativity_target)
        
        # Train quantum model
        quantum_target = plays_df['success'].astype(float)
        self.quantum_model.fit(features, quantum_target)
        
        # Train human model
        human_target = plays_df['emotional_momentum']
        self.human_model.fit(features, human_target)
        
        self.logger.info("Models trained on historical data")
    
    def analyze_play_effectiveness(self, play: Dict) -> Dict:
        """Analyze how effective a play was in terms of quantum-human harmony."""
        features = self._extract_single_play_features(play)
        
        creativity_score = self.creativity_model.predict([features])[0]
        quantum_score = self.quantum_model.predict([features])[0]
        human_score = self.human_model.predict([features])[0]
        
        harmony_score = self._calculate_harmony_score(
            creativity_score, quantum_score, human_score
        )
        
        return {
            'creativity_score': creativity_score,
            'quantum_score': quantum_score,
            'human_score': human_score,
            'harmony_score': harmony_score,
            'insights': self._generate_insights(
                creativity_score, quantum_score, human_score
            )
        }
    
    def _calculate_quantum_metrics(self, play_data: Dict) -> Dict:
        """Calculate quantum metrics for a play."""
        # Calculate play precision
        precision = self._calculate_precision(play_data)
        
        # Calculate quantum alignment
        alignment = self._calculate_alignment(play_data)
        
        # Calculate quantum coherence
        coherence = self._calculate_coherence(play_data)
        
        return {
            'precision': precision,
            'alignment': alignment,
            'coherence': coherence
        }
    
    def _calculate_human_factors(self, play_data: Dict) -> Dict:
        """Calculate human factors in a play."""
        # Calculate spontaneity
        spontaneity = self._calculate_spontaneity(play_data)
        
        # Calculate emotional momentum
        emotional_momentum = self._calculate_emotional_momentum(play_data)
        
        # Calculate intuition factor
        intuition = self._calculate_intuition(play_data)
        
        return {
            'spontaneity': spontaneity,
            'emotional_momentum': emotional_momentum,
            'intuition': intuition
        }
    
    def _calculate_precision(self, play_data: Dict) -> float:
        """Calculate the precision of play execution."""
        expected = play_data.get('expected_yards', 0)
        actual = play_data.get('yards_gained', 0)
        return 1.0 / (1.0 + abs(expected - actual))
    
    def _calculate_alignment(self, play_data: Dict) -> float:
        """Calculate quantum alignment of the play."""
        situation_score = self._calculate_situation_score(play_data)
        execution_score = self._calculate_execution_score(play_data)
        return (situation_score + execution_score) / 2
    
    def _calculate_coherence(self, play_data: Dict) -> float:
        """Calculate quantum coherence of the play."""
        return np.random.random()  # Placeholder for actual calculation
    
    def _calculate_spontaneity(self, play_data: Dict) -> float:
        """Calculate spontaneity factor of the play."""
        return np.random.random()  # Placeholder for actual calculation
    
    def _calculate_emotional_momentum(self, play_data: Dict) -> float:
        """Calculate emotional momentum of the team."""
        return np.random.random()  # Placeholder for actual calculation
    
    def _calculate_intuition(self, play_data: Dict) -> float:
        """Calculate intuition factor in play calling."""
        return np.random.random()  # Placeholder for actual calculation
    
    def _calculate_situation_score(self, play_data: Dict) -> float:
        """Calculate how well the play fits the situation."""
        return np.random.random()  # Placeholder for actual calculation
    
    def _calculate_execution_score(self, play_data: Dict) -> float:
        """Calculate how well the play was executed."""
        return np.random.random()  # Placeholder for actual calculation
    
    def _calculate_creativity_score(self, play_data: Dict, 
                                  quantum_state: Dict, 
                                  human_factors: Dict) -> float:
        """Calculate creativity score based on quantum and human factors."""
        quantum_weight = quantum_state['coherence']
        human_weight = human_factors['spontaneity']
        
        return (quantum_weight * human_factors['intuition'] + 
                human_weight * (1 - quantum_state['precision']))
    
    def _extract_features(self, plays_df: pd.DataFrame) -> np.ndarray:
        """Extract features from plays dataframe."""
        feature_columns = [
            'down', 'distance', 'field_position', 'score_differential',
            'time_remaining', 'timeouts_remaining'
        ]
        return plays_df[feature_columns].values
    
    def _extract_single_play_features(self, play: Dict) -> np.ndarray:
        """Extract features from a single play."""
        return np.array([
            play.get('down', 1),
            play.get('distance', 10),
            play.get('field_position', 50),
            play.get('score_differential', 0),
            play.get('time_remaining', 1800),
            play.get('timeouts_remaining', 3)
        ])
    
    def _calculate_harmony_score(self, creativity: float, 
                               quantum: float, 
                               human: float) -> float:
        """Calculate overall harmony score."""
        return (creativity + quantum + human) / 3
    
    def _generate_insights(self, creativity: float, 
                         quantum: float, 
                         human: float) -> List[str]:
        """Generate insights from the scores."""
        insights = []
        
        if creativity > 0.7:
            insights.append("High creativity indicates successful quantum-human fusion")
        if quantum > 0.7:
            insights.append("Strong quantum alignment suggests optimal decision-making")
        if human > 0.7:
            insights.append("Strong human factors enhanced play effectiveness")
        
        if len(insights) == 0:
            insights.append("Play showed balanced quantum-human characteristics")
            
        return insights
    
    def save_models(self, path: str = "models"):
        """Save trained models."""
        os.makedirs(path, exist_ok=True)
        joblib.dump(self.creativity_model, f"{path}/creativity_model.pkl")
        joblib.dump(self.quantum_model, f"{path}/quantum_model.pkl")
        joblib.dump(self.human_model, f"{path}/human_model.pkl")
        
    def load_models(self, path: str = "models"):
        """Load trained models."""
        self.creativity_model = joblib.load(f"{path}/creativity_model.pkl")
        self.quantum_model = joblib.load(f"{path}/quantum_model.pkl")
        self.human_model = joblib.load(f"{path}/human_model.pkl")
