"""Test suite for analytics dashboard."""
import pytest
from unittest.mock import Mock, patch
from src.dashboard.data_provider import DashboardDataProvider
from src.dashboard.real_time import RealTimeUpdater
from src.dashboard.visualization import VisualizationEngine

class TestDashboard:
    @pytest.fixture
    def data_provider(self):
        return DashboardDataProvider()
        
    @pytest.fixture
    def real_time(self):
        return RealTimeUpdater()
        
    @pytest.fixture
    def viz_engine(self):
        return VisualizationEngine()
        
    def test_data_loading(self, data_provider):
        """Test dashboard data loading."""
        data = data_provider.get_dashboard_data()
        
        assert "quantum_states" in data
        assert "team_stats" in data
        assert "historical_trends" in data
        assert len(data["quantum_states"]) > 0
        
    def test_real_time_updates(self, real_time):
        """Test real-time data updates."""
        mock_callback = Mock()
        real_time.subscribe(mock_callback)
        
        # Simulate update
        real_time._emit_update({
            "type": "quantum_change",
            "team": "GB",
            "value": 0.85
        })
        
        mock_callback.assert_called_once()
        
    def test_visualization_rendering(self, viz_engine):
        """Test visualization rendering."""
        test_data = {
            "nodes": [{"id": "GB", "value": 0.85}],
            "edges": [{"source": "GB", "target": "CHI", "value": 0.5}]
        }
        
        rendered = viz_engine.render_network(test_data)
        
        assert rendered["width"] > 0
        assert rendered["height"] > 0
        assert len(rendered["elements"]) > 0
        
    def test_performance_metrics(self, data_provider):
        """Test performance metrics calculation."""
        metrics = data_provider.get_performance_metrics()
        
        assert "api_latency" in metrics
        assert "quantum_ops" in metrics
        assert "prediction_accuracy" in metrics
        assert all(v >= 0 for v in metrics.values())
        
    def test_historical_analysis(self, data_provider):
        """Test historical data analysis."""
        history = data_provider.get_historical_analysis("GB")
        
        assert "quantum_ratings" in history
        assert "win_rates" in history
        assert "trends" in history
        assert len(history["quantum_ratings"]) > 0
        
    def test_data_filtering(self, data_provider):
        """Test data filtering capabilities."""
        filters = {
            "team": "GB",
            "date_range": ["2025-01-01", "2025-01-02"],
            "metrics": ["quantum_rating", "momentum"]
        }
        
        filtered_data = data_provider.apply_filters(filters)
        
        assert all(d["team"] == "GB" for d in filtered_data)
        assert all("quantum_rating" in d for d in filtered_data)
        
    def test_export_functionality(self, data_provider):
        """Test data export functionality."""
        export_data = data_provider.export_dashboard_data()
        
        assert "timestamp" in export_data
        assert "data" in export_data
        assert "format_version" in export_data
        
    def test_error_handling(self, data_provider):
        """Test error handling in dashboard."""
        with pytest.raises(ValueError):
            data_provider.get_team_data("")  # Empty team name
            
        with pytest.raises(ValueError):
            data_provider.apply_filters({})  # Empty filters
            
    def test_accessibility(self, viz_engine):
        """Test accessibility features."""
        config = viz_engine.get_accessibility_settings()
        
        assert "color_blind_safe" in config
        assert "high_contrast" in config
        assert "text_size" in config
        
    def test_responsive_layout(self, viz_engine):
        """Test responsive layout adaptation."""
        layouts = viz_engine.get_responsive_layouts()
        
        assert "mobile" in layouts
        assert "tablet" in layouts
        assert "desktop" in layouts
        assert all("grid" in l for l in layouts.values())
