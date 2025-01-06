"""Real-time updates for dashboard."""
from typing import Callable, Dict, List, Any
import asyncio
import json
from datetime import datetime

class RealTimeUpdater:
    def __init__(self):
        self.subscribers: List[Callable] = []
        self.update_queue = asyncio.Queue()
        self.last_update = datetime.now()
        
    def subscribe(self, callback: Callable):
        """Subscribe to real-time updates."""
        self.subscribers.append(callback)
        
    def unsubscribe(self, callback: Callable):
        """Unsubscribe from real-time updates."""
        if callback in self.subscribers:
            self.subscribers.remove(callback)
            
    async def start(self):
        """Start real-time updates."""
        while True:
            update = await self.update_queue.get()
            await self._process_update(update)
            
    async def _process_update(self, update: Dict[str, Any]):
        """Process an update."""
        for subscriber in self.subscribers:
            try:
                subscriber(update)
            except Exception as e:
                print(f"Error processing update: {str(e)}")
                
    def _emit_update(self, update: Dict[str, Any]):
        """Emit an update to subscribers."""
        self.last_update = datetime.now()
        asyncio.create_task(self._process_update(update))
        
    async def simulate_updates(self):
        """Simulate updates for testing."""
        while True:
            await asyncio.sleep(1)
            self._emit_update({
                "type": "quantum_change",
                "team": "GB",
                "value": 0.85
            })
