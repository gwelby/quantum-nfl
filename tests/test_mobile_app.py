"""Test suite for mobile app functionality."""
import pytest
from unittest.mock import Mock, patch
from src.mobile.api_client import MobileAPIClient
from src.mobile.websocket_client import WebSocketClient
from src.mobile.state_manager import StateManager

class TestMobileApp:
    @pytest.fixture
    def api_client(self):
        return MobileAPIClient()
        
    @pytest.fixture
    def ws_client(self):
        return WebSocketClient()
        
    @pytest.fixture
    def state_manager(self):
        return StateManager()
        
    def test_real_time_updates(self, ws_client):
        """Test WebSocket real-time updates."""
        mock_callback = Mock()
        ws_client.subscribe("quantum_updates", mock_callback)
        
        # Simulate incoming data
        ws_client._on_message({
            "type": "quantum_update",
            "data": {"team": "GB", "quantum_rating": 0.85}
        })
        
        mock_callback.assert_called_once()
        
    def test_offline_cache(self, api_client, state_manager):
        """Test offline data caching."""
        # Cache data
        test_data = {"team": "GB", "stats": {"wins": 10}}
        state_manager.cache_data("team_stats", test_data)
        
        # Simulate offline mode
        api_client.set_offline(True)
        cached_data = state_manager.get_cached_data("team_stats")
        
        assert cached_data == test_data
        
    def test_data_sync(self, api_client, state_manager):
        """Test data synchronization."""
        local_data = {"timestamp": "2025-01-01", "data": {"wins": 10}}
        server_data = {"timestamp": "2025-01-02", "data": {"wins": 11}}
        
        state_manager.set_local_data(local_data)
        synced_data = api_client.sync_data(local_data)
        
        assert synced_data["data"]["wins"] == server_data["data"]["wins"]
        
    @pytest.mark.asyncio
    async def test_live_game_updates(self, ws_client):
        """Test live game update streaming."""
        updates = []
        
        def on_update(data):
            updates.append(data)
            
        ws_client.subscribe_to_game("GB-CHI", on_update)
        
        # Simulate 3 game updates
        for i in range(3):
            await ws_client._simulate_game_update({
                "game_id": "GB-CHI",
                "score": f"{i}-0"
            })
            
        assert len(updates) == 3
        
    def test_quantum_visualization(self, state_manager):
        """Test quantum state visualization data."""
        quantum_state = {
            "team": "GB",
            "quantum_rating": 0.85,
            "entanglement": 0.92,
            "momentum": 0.78
        }
        
        viz_data = state_manager.prepare_visualization(quantum_state)
        
        assert "nodes" in viz_data
        assert "edges" in viz_data
        assert len(viz_data["nodes"]) > 0
        
    def test_performance_optimization(self, state_manager):
        """Test performance optimization features."""
        # Test memory usage
        initial_memory = state_manager.get_memory_usage()
        
        # Add large dataset
        large_data = {"data": [i for i in range(10000)]}
        state_manager.process_data(large_data)
        
        final_memory = state_manager.get_memory_usage()
        
        # Should use efficient memory management
        assert (final_memory - initial_memory) < 1000000  # Less than 1MB increase
        
    def test_error_handling(self, api_client):
        """Test error handling and recovery."""
        with pytest.raises(ConnectionError):
            api_client.fetch_data(timeout=0.1)  # Force timeout
            
        # Should automatically retry
        assert api_client.retry_count > 0
        
        # Should fall back to cached data
        fallback_data = api_client.get_data_with_fallback()
        assert fallback_data is not None
        
    def test_accessibility(self, state_manager):
        """Test accessibility features."""
        viz_config = state_manager.get_accessibility_config()
        
        assert "colorBlindMode" in viz_config
        assert "highContrast" in viz_config
        assert "textSize" in viz_config
