"""WebSocket client for real-time updates."""
import asyncio
import websockets
import json
from typing import Callable, Dict, Any

class WebSocketClient:
    def __init__(self):
        self.ws = None
        self.subscribers = {}
        self.connected = False
        
    async def connect(self):
        """Connect to WebSocket server."""
        try:
            self.ws = await websockets.connect(
                "wss://ws.quantum-nfl.example.com"
            )
            self.connected = True
            await self._listen()
        except Exception as e:
            print(f"WebSocket connection failed: {str(e)}")
            self.connected = False
            
    async def _listen(self):
        """Listen for WebSocket messages."""
        while self.connected:
            try:
                message = await self.ws.recv()
                data = json.loads(message)
                await self._handle_message(data)
            except websockets.exceptions.ConnectionClosed:
                self.connected = False
                break
                
    async def _handle_message(self, data: Dict[str, Any]):
        """Handle incoming WebSocket message."""
        message_type = data.get("type")
        if message_type in self.subscribers:
            for callback in self.subscribers[message_type]:
                callback(data)
                
    def subscribe(self, event_type: str, callback: Callable):
        """Subscribe to WebSocket events."""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
        
    def unsubscribe(self, event_type: str, callback: Callable):
        """Unsubscribe from WebSocket events."""
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(callback)
            
    async def send(self, data: Dict[str, Any]):
        """Send data through WebSocket."""
        if self.connected and self.ws:
            await self.ws.send(json.dumps(data))
            
    def subscribe_to_game(self, game_id: str, callback: Callable):
        """Subscribe to game updates."""
        self.subscribe(f"game_{game_id}", callback)
        
    async def _simulate_game_update(self, data: Dict[str, Any]):
        """Simulate game update for testing."""
        await self._handle_message({
            "type": f"game_{data['game_id']}",
            "data": data
        })
