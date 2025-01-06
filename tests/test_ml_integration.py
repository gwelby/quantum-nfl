"""Test suite for machine learning integration."""
import pytest
import numpy as np
from src.ml.quantum_ml import QuantumMLPredictor
from src.quantum.state import QuantumState

class TestMLIntegration:
    @pytest.fixture
    def predictor(self):
        return QuantumMLPredictor()
        
    @pytest.fixture
    def quantum_state(self):
        return QuantumState()
        
    def test_feature_engineering(self, predictor):
        """Test quantum feature engineering."""
        team_data = {
            "quantum_rating": 0.85,
            "entanglement_factor": 0.92,
            "momentum": 0.78,
            "wins": 10,
            "points_scored": 300,
            "points_allowed": 200
        }
        
        features = predictor.prepare_quantum_features(team_data)
        
        assert len(features) > 0
        assert isinstance(features, np.ndarray)
        assert not np.any(np.isnan(features))
        
    def test_model_training(self, predictor):
        """Test model training with quantum features."""
        training_data = [
            {
                "home_team": {
                    "quantum_rating": 0.85,
                    "entanglement_factor": 0.92,
                    "momentum": 0.78,
                    "wins": 10
                },
                "away_team": {
                    "quantum_rating": 0.75,
                    "entanglement_factor": 0.88,
                    "momentum": 0.72,
                    "wins": 8
                }
            }
            for _ in range(100)  # Generate test data
        ]
        
        labels = [1, 0] * 50  # Alternate wins/losses
        
        predictor.train(training_data, labels)
        
        # Check if model is trained
        assert predictor.classifier is not None
        assert hasattr(predictor.classifier, 'predict_proba')
        
    def test_prediction_accuracy(self, predictor):
        """Test prediction accuracy."""
        # Train with some data first
        predictor.train([], [])  # Add proper training data
        
        home_team = {
            "quantum_rating": 0.85,
            "entanglement_factor": 0.92,
            "momentum": 0.78,
            "wins": 10
        }
        
        away_team = {
            "quantum_rating": 0.75,
            "entanglement_factor": 0.88,
            "momentum": 0.72,
            "wins": 8
        }
        
        win_prob, metrics = predictor.predict_game(home_team, away_team)
        
        assert 0 <= win_prob <= 1
        assert "feature_importance" in metrics
        assert "quantum_confidence" in metrics
        
    def test_quantum_impact_analysis(self, predictor):
        """Test quantum impact analysis."""
        game_data = {
            "home_team": {
                "quantum_rating": 0.85,
                "entanglement_factor": 0.92,
                "momentum": 0.78,
                "wins": 10
            },
            "away_team": {
                "quantum_rating": 0.75,
                "entanglement_factor": 0.88,
                "momentum": 0.72,
                "wins": 8
            }
        }
        
        impact = predictor.analyze_quantum_impact(game_data)
        
        assert "quantum_impact" in impact
        assert "base_prediction" in impact
        assert "modified_prediction" in impact
        
    def test_feature_importance(self, predictor):
        """Test feature importance analysis."""
        # Train the model first
        predictor.train([], [])  # Add proper training data
        
        importance_df = predictor.get_feature_importance()
        
        assert len(importance_df) > 0
        assert "Feature" in importance_df.columns
        assert "Importance" in importance_df.columns
        assert importance_df["Importance"].sum() > 0
        
    def test_model_persistence(self, predictor, tmp_path):
        """Test model saving and loading."""
        # Train the model
        predictor.train([], [])  # Add proper training data
        
        # Save the model
        save_path = tmp_path / "model.pkl"
        predictor.save_model(save_path)
        
        # Load the model
        new_predictor = QuantumMLPredictor()
        new_predictor.load_model(save_path)
        
        # Compare predictions
        test_data = {
            "quantum_rating": 0.85,
            "entanglement_factor": 0.92,
            "momentum": 0.78,
            "wins": 10
        }
        
        pred1 = predictor.prepare_quantum_features(test_data)
        pred2 = new_predictor.prepare_quantum_features(test_data)
        
        np.testing.assert_array_almost_equal(pred1, pred2)
        
    def test_error_handling(self, predictor):
        """Test error handling in ML pipeline."""
        with pytest.raises(ValueError):
            predictor.prepare_quantum_features({})  # Empty data
            
        with pytest.raises(ValueError):
            predictor.train([], [])  # Empty training data
            
        with pytest.raises(ValueError):
            predictor.predict_game({}, {})  # Empty team data
