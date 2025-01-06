"""Rate limiter for API protection."""
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import threading
import time

class RateLimiter:
    def __init__(self, limit: int, window: int):
        """Initialize rate limiter.
        
        Args:
            limit: Maximum number of requests
            window: Time window in seconds
        """
        self.limit = limit
        self.window = window
        self.requests: Dict[str, list] = {}
        self.lock = threading.Lock()
        
    def is_allowed(self, key: str) -> bool:
        """Check if request is allowed."""
        with self.lock:
            now = datetime.now()
            self._cleanup(key, now)
            
            if key not in self.requests:
                self.requests[key] = []
                
            if len(self.requests[key]) >= self.limit:
                return False
                
            self.requests[key].append(now)
            return True
            
    def _cleanup(self, key: str, now: datetime):
        """Clean up old requests."""
        if key not in self.requests:
            return
            
        window_start = now - timedelta(seconds=self.window)
        self.requests[key] = [
            t for t in self.requests[key]
            if t >= window_start
        ]
        
    def get_remaining(self, key: str) -> int:
        """Get remaining requests in window."""
        with self.lock:
            self._cleanup(key, datetime.now())
            return max(0, self.limit - len(self.requests.get(key, [])))
            
    def reset(self, key: str):
        """Reset rate limit for key."""
        with self.lock:
            if key in self.requests:
                del self.requests[key]
                
    def wait_if_needed(self, key: str) -> bool:
        """Wait if rate limit is exceeded."""
        with self.lock:
            now = datetime.now()
            self._cleanup(key, now)
            
            if key not in self.requests:
                self.requests[key] = []
                return True
                
            if len(self.requests[key]) < self.limit:
                self.requests[key].append(now)
                return True
                
            # Calculate wait time
            oldest = min(self.requests[key])
            wait_time = (
                oldest +
                timedelta(seconds=self.window) -
                now
            ).total_seconds()
            
            if wait_time > 0:
                time.sleep(wait_time)
                
            self.requests[key] = [now]
            return True
            
    def get_stats(self, key: str) -> Dict[str, Any]:
        """Get rate limiting stats."""
        with self.lock:
            now = datetime.now()
            self._cleanup(key, now)
            
            requests = self.requests.get(key, [])
            return {
                "total": len(requests),
                "remaining": self.get_remaining(key),
                "window": self.window,
                "limit": self.limit
            }
