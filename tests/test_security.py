"""Security test suite for the Quantum NFL platform."""
import pytest
import jwt
import bcrypt
from datetime import datetime, timedelta
from src.security.auth import AuthManager
from src.security.quantum_state import QuantumStateProtector
from src.security.rate_limiter import RateLimiter

class TestSecurity:
    """Test suite for security features."""
    
    @pytest.fixture
    def auth_manager(self):
        """Create AuthManager instance."""
        return AuthManager()
        
    @pytest.fixture
    def quantum_protector(self):
        """Create QuantumStateProtector instance."""
        return QuantumStateProtector()
        
    @pytest.fixture
    def rate_limiter(self):
        """Create RateLimiter instance."""
        return RateLimiter()
        
    def test_password_hashing(self, auth_manager):
        """Test password hashing and verification."""
        password = "SecurePass123!"
        hashed = auth_manager.hash_password(password)
        assert bcrypt.checkpw(password.encode(), hashed)
        
    def test_jwt_token(self, auth_manager):
        """Test JWT token generation and validation."""
        user_data = {"id": 1, "username": "test_user"}
        token = auth_manager.generate_token(user_data)
        decoded = auth_manager.verify_token(token)
        assert decoded["username"] == user_data["username"]
        
    def test_token_expiration(self, auth_manager):
        """Test token expiration."""
        user_data = {"id": 1, "username": "test_user"}
        token = auth_manager.generate_token(user_data, expires_in=timedelta(seconds=1))
        time.sleep(2)
        with pytest.raises(jwt.ExpiredSignatureError):
            auth_manager.verify_token(token)
            
    def test_rate_limiting(self, rate_limiter):
        """Test rate limiting functionality."""
        user_id = "test_user"
        endpoint = "/api/predictions"
        
        # Should allow initial requests
        for _ in range(5):
            assert rate_limiter.check_rate_limit(user_id, endpoint)
            
        # Should block excessive requests
        assert not rate_limiter.check_rate_limit(user_id, endpoint)
        
    def test_quantum_state_protection(self, quantum_protector):
        """Test quantum state protection."""
        state = {
            "team": "Packers",
            "quantum_rating": 0.85,
            "entanglement_factor": 0.92
        }
        
        # Test state encryption
        encrypted = quantum_protector.encrypt_state(state)
        decrypted = quantum_protector.decrypt_state(encrypted)
        assert decrypted == state
        
    def test_invalid_token(self, auth_manager):
        """Test invalid token handling."""
        with pytest.raises(jwt.InvalidTokenError):
            auth_manager.verify_token("invalid.token.here")
            
    def test_sql_injection_prevention(self, auth_manager):
        """Test SQL injection prevention."""
        malicious_input = "'; DROP TABLE users; --"
        assert auth_manager.sanitize_input(malicious_input) != malicious_input
        
    def test_xss_prevention(self, auth_manager):
        """Test XSS prevention."""
        malicious_input = "<script>alert('xss')</script>"
        sanitized = auth_manager.sanitize_input(malicious_input)
        assert "<script>" not in sanitized
        
    def test_csrf_token(self, auth_manager):
        """Test CSRF token generation and validation."""
        token = auth_manager.generate_csrf_token()
        assert auth_manager.verify_csrf_token(token)
        
    def test_quantum_noise_reduction(self, quantum_protector):
        """Test quantum noise reduction in protected states."""
        noisy_state = {
            "team": "Vikings",
            "quantum_rating": 0.75,
            "noise_factor": 0.15
        }
        cleaned_state = quantum_protector.reduce_quantum_noise(noisy_state)
        assert cleaned_state["noise_factor"] < noisy_state["noise_factor"]
        
    def test_decoherence_prevention(self, quantum_protector):
        """Test decoherence prevention in quantum states."""
        initial_state = {
            "team": "Bears",
            "coherence": 0.95
        }
        protected_state = quantum_protector.prevent_decoherence(initial_state)
        assert protected_state["coherence"] >= initial_state["coherence"]
        
    def test_quantum_memory_security(self, quantum_protector):
        """Test quantum memory security measures."""
        memory_state = {
            "team": "Lions",
            "quantum_memory": [0.5, 0.7, 0.3]
        }
        secured = quantum_protector.secure_quantum_memory(memory_state)
        assert "access_log" in secured
        assert secured["encryption_level"] >= 0.9
