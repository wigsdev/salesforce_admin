
import pytest
from datetime import timedelta
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

from app.utils.security import hash_password, verify_password, create_access_token, verify_token
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate
from app.models.user import User

# --- SECURITY UTILS TESTS ---

def test_password_hashing():
    """Test that password hashing works and is irreversible (practically)."""
    password = "supersecretpassword123"
    hashed = hash_password(password)
    
    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("wrongpassword", hashed) is False

def test_jwt_token_creation_and_verification():
    """Test creating and verifying a JWT token."""
    data = {"sub": "test@lumina.edu"}
    # Create token valid for 1 hour
    token = create_access_token(data, expires_delta=timedelta(hours=1))
    
    # Verify
    payload = verify_token(token)
    assert payload is not None
    assert payload["sub"] == "test@lumina.edu"
    assert "exp" in payload

def test_jwt_token_expiration():
    """Test that expired tokens are rejected (simulated with negative time)."""
    data = {"sub": "expired@lumina.edu"}
    # Create token that expired 1 second ago
    token = create_access_token(data, expires_delta=timedelta(seconds=-1))
    
    # Verify should fail (return None or raise error depending on implementation, 
    # verify_token returns None on JWTError including expiry)
    payload = verify_token(token)
    assert payload is None

# --- AUTH SERVICE TESTS (With Mocks) ---

def test_auth_service_create_user():
    """Test creating a user via AuthService (hashing should happen)."""
    mock_db = MagicMock(spec=Session)
    # Simulator query returning None (user not exists)
    mock_db.query.return_value.filter.return_value.first.return_value = None
    
    user_data = UserCreate(
        name="Test User",
        email="newuser@lumina.edu",
        password="plainpassword",
        team="Lumina"
    )
    
    # Call service
    user = AuthService.create_user(mock_db, user_data)
    
    # Assertions
    assert user.email == "newuser@lumina.edu"
    assert user.password_hash != "plainpassword"
    assert verify_password("plainpassword", user.password_hash) is True
    
    # Check DB usage
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

def test_auth_service_authenticate_success():
    """Test successful authentication."""
    mock_db = MagicMock(spec=Session)
    
    # Setup mock user in DB
    password = "mypassword"
    hashed = hash_password(password)
    mock_user = User(
        id=1, 
        email="valid@lumina.edu", 
        password_hash=hashed,
        is_active=True
    )
    
    mock_db.query.return_value.filter.return_value.first.return_value = mock_user
    
    # Action
    authenticated_user = AuthService.authenticate_user(mock_db, "valid@lumina.edu", "mypassword")
    
    # Assert
    assert authenticated_user is not None
    assert authenticated_user.email == "valid@lumina.edu"

def test_auth_service_authenticate_failure():
    """Test failed authentication (wrong password)."""
    mock_db = MagicMock(spec=Session)
    
    # Setup mock user in DB
    password = "mypassword"
    hashed = hash_password(password)
    mock_user = User(
        id=1, 
        email="valid@lumina.edu", 
        password_hash=hashed,
        is_active=True
    )
    
    mock_db.query.return_value.filter.return_value.first.return_value = mock_user
    
    # Action (Wrong Password)
    authenticated_user = AuthService.authenticate_user(mock_db, "valid@lumina.edu", "WRONGPASSWORD")
    
    # Assert
    assert authenticated_user is None
