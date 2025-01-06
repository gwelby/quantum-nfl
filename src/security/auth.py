"""Authentication and authorization manager."""
import jwt
import bcrypt
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

class AuthManager:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.token_expiry = timedelta(hours=24)
        self.refresh_token_expiry = timedelta(days=30)
        
    def create_user(self, username: str, password: str) -> Dict[str, Any]:
        """Create a new user."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        
        return {
            "username": username,
            "password_hash": hashed.decode(),
            "created_at": datetime.now().isoformat()
        }
        
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash."""
        return bcrypt.checkpw(
            password.encode(),
            hashed.encode()
        )
        
    def generate_token(self, user_data: Dict[str, Any]) -> Dict[str, str]:
        """Generate JWT token."""
        now = datetime.now()
        
        token_payload = {
            "sub": user_data["username"],
            "iat": now,
            "exp": now + self.token_expiry
        }
        
        refresh_payload = {
            "sub": user_data["username"],
            "iat": now,
            "exp": now + self.refresh_token_expiry
        }
        
        return {
            "access_token": jwt.encode(
                token_payload,
                self.secret_key,
                algorithm="HS256"
            ),
            "refresh_token": jwt.encode(
                refresh_payload,
                self.secret_key,
                algorithm="HS256"
            )
        }
        
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verify JWT token."""
        try:
            return jwt.decode(
                token,
                self.secret_key,
                algorithms=["HS256"]
            )
        except jwt.InvalidTokenError:
            return None
            
    def refresh_token(self, refresh_token: str) -> Optional[Dict[str, str]]:
        """Refresh access token using refresh token."""
        payload = self.verify_token(refresh_token)
        if not payload:
            return None
            
        user_data = {"username": payload["sub"]}
        return self.generate_token(user_data)
        
    def change_password(
        self,
        user_data: Dict[str, Any],
        old_password: str,
        new_password: str
    ) -> bool:
        """Change user password."""
        if not self.verify_password(old_password, user_data["password_hash"]):
            return False
            
        salt = bcrypt.gensalt()
        new_hash = bcrypt.hashpw(new_password.encode(), salt)
        user_data["password_hash"] = new_hash.decode()
        
        return True
        
    def invalidate_token(self, token: str):
        """Invalidate a token."""
        # In a real implementation, this would add the token to a blacklist
        # or revocation list, possibly in Redis or a database
        pass
        
    def get_user_permissions(self, user_data: Dict[str, Any]) -> Dict[str, bool]:
        """Get user permissions."""
        return {
            "can_read": True,
            "can_write": user_data.get("role") == "admin",
            "can_delete": user_data.get("role") == "admin"
        }
