"""API client for mobile applications."""
from typing import Dict, Any, Optional
import requests
import json
from datetime import datetime

class MobileAPIClient:
    def __init__(self):
        self.base_url = "https://api.quantum-nfl.example.com"
        self.offline_mode = False
        self.retry_count = 0
        self.max_retries = 3
        
    def set_offline(self, offline: bool):
        """Set offline mode."""
        self.offline_mode = offline
        
    def fetch_data(self, endpoint: str, timeout: float = 5.0) -> Dict[str, Any]:
        """Fetch data from API."""
        if self.offline_mode:
            return self._get_cached_data(endpoint)
            
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.retry_count += 1
            if self.retry_count < self.max_retries:
                return self.fetch_data(endpoint, timeout * 1.5)
            raise ConnectionError(f"Failed to fetch data: {str(e)}")
            
    def sync_data(self, local_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sync local data with server."""
        if not local_data:
            return {}
            
        try:
            response = requests.post(
                f"{self.base_url}/sync",
                json=local_data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return local_data  # Keep local data on failure
            
    def get_data_with_fallback(self) -> Optional[Dict[str, Any]]:
        """Get data with fallback to cache."""
        try:
            return self.fetch_data("data")
        except ConnectionError:
            return self._get_cached_data("data")
            
    def _get_cached_data(self, key: str) -> Dict[str, Any]:
        """Get cached data."""
        try:
            with open(f"cache_{key}.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
