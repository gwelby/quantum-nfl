"""Quantum-Enhanced Machine Learning for NFL Predictions."""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from src.quantum.state import QuantumState
from typing import Dict, List, Tuple

class QuantumMLPredictor:
    """Quantum-enhanced machine learning predictor."""
    
    def __init__(self):
        self.quantum_state = QuantumState()
        self.classifier = RandomForestClassifier(n_estimators=100)
        self.scaler = StandardScaler()
        
    def prepare_quantum_features(self, team_data: Dict) -> np.ndarray:
        """Prepare quantum-enhanced features."""
        quantum_features = []
        
        # Extract quantum states
        quantum_rating = team_data['quantum_rating']
        entanglement = team_data['entanglement_factor']
        momentum = team_data['momentum']
        
        # Calculate quantum-classical interactions
        classical_stats = np.array([
            team_data['wins'],
            team_data['points_scored'],
            team_data['points_allowed']
        ])
        
        # Quantum feature engineering
        quantum_features.extend([
            quantum_rating,
            entanglement,
            momentum,
            quantum_rating * entanglement,  # Interaction term
            momentum * np.mean(classical_stats),  # Quantum-classical coupling
            np.sin(quantum_rating * np.pi/2),  # Non-linear transformation
            np.exp(-entanglement)  # Decay factor
        ])
        
        return np.array(quantum_features)
    
    def train(self, 
             training_data: List[Dict], 
             labels: List[int]) -> None:
        """Train the quantum-enhanced model."""
        X = []
        for game in training_data:
            home_features = self.prepare_quantum_features(game['home_team'])
            away_features = self.prepare_quantum_features(game['away_team'])
            
            # Combine features with quantum interference
            combined_features = np.concatenate([
                home_features,
                away_features,
                home_features * away_features  # Quantum interference
            ])
            
            X.append(combined_features)
            
        X = np.array(X)
        X_scaled = self.scaler.fit_transform(X)
        
        self.classifier.fit(X_scaled, labels)
    
    def predict_game(self, 
                    home_team: Dict, 
                    away_team: Dict) -> Tuple[float, Dict]:
        """Predict game outcome with quantum enhancement."""
        # Prepare features
        home_features = self.prepare_quantum_features(home_team)
        away_features = self.prepare_quantum_features(away_team)
        
        combined_features = np.concatenate([
            home_features,
            away_features,
            home_features * away_features
        ]).reshape(1, -1)
        
        X_scaled = self.scaler.transform(combined_features)
        
        # Get probability prediction
        win_prob = self.classifier.predict_proba(X_scaled)[0][1]
        
        # Calculate confidence metrics
        feature_importance = dict(zip(
            ['quantum_rating', 'entanglement', 'momentum', 'interaction',
             'coupling', 'non_linear', 'decay'],
            self.classifier.feature_importances_[:7]  # First 7 features
        ))
        
        return win_prob, {
            'feature_importance': feature_importance,
            'quantum_confidence': np.mean([
                home_team['quantum_rating'],
                away_team['quantum_rating']
            ]),
            'prediction_entropy': -win_prob * np.log2(win_prob) - \
                (1 - win_prob) * np.log2(1 - win_prob)
        }
    
    def analyze_quantum_impact(self, 
                             game_data: Dict) -> Dict:
        """Analyze quantum effects on prediction."""
        base_prediction = self.predict_game(
            game_data['home_team'],
            game_data['away_team']
        )[0]
        
        # Modify quantum states
        modified_home = game_data['home_team'].copy()
        modified_home['quantum_rating'] *= 0.5
        
        modified_prediction = self.predict_game(
            modified_home,
            game_data['away_team']
        )[0]
        
        return {
            'quantum_impact': abs(base_prediction - modified_prediction),
            'base_prediction': base_prediction,
            'modified_prediction': modified_prediction
        }
    
    def get_feature_importance(self) -> pd.DataFrame:
        """Get quantum feature importance analysis."""
        feature_names = [
            'Home Quantum Rating',
            'Home Entanglement',
            'Home Momentum',
            'Home Interaction',
            'Home Coupling',
            'Home Non-linear',
            'Home Decay',
            'Away Quantum Rating',
            'Away Entanglement',
            'Away Momentum',
            'Away Interaction',
            'Away Coupling',
            'Away Non-linear',
            'Away Decay',
            'Interference Terms'
        ]
        
        importance = self.classifier.feature_importances_
        
        return pd.DataFrame({
            'Feature': feature_names,
            'Importance': importance
        }).sort_values('Importance', ascending=False)
