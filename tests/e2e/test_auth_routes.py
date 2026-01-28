
from datetime import datetime
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from app.main import app
from app.dependencies import get_current_user
from app.models.user import User

client = TestClient(app)

# --- E2E AUTH ROUTE TESTS ---

@patch("app.routers.auth.AuthService.authenticate_user")
def test_login_successful(mock_auth):
    """Test successful login returns a JWT token."""
    mock_user = MagicMock()
    mock_user.email = "test@lumina.edu"
    mock_user.id = 1
    
    mock_auth.return_value = mock_user
    
    response = client.post("/api/auth/login", json={
        "email": "test@lumina.edu",
        "password": "correctpassword"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

@patch("app.routers.auth.AuthService.authenticate_user")
def test_login_failed(mock_auth):
    """Test failed login returns 401."""
    mock_auth.return_value = None 
    
    response = client.post("/api/auth/login", json={
        "email": "wrong@lumina.edu",
        "password": "wrongpassword"
    })
    
    assert response.status_code == 401
    assert "Incorrect email or password" in response.json().get("detail", "")

def test_get_current_user_me_overriding_dependency():
    """Test /api/users/me by overriding the dependency directly."""
    # Create a mock user with COMPLETE fields required by UserResponse schema
    mock_user = User(
        id=1, 
        email="override@lumina.edu", 
        name="Override User", 
        team="Lumina",
        role="student",          # Missing Field 1
        is_active=True,          # Missing Field 2
        created_at=datetime.utcnow() # Missing Field 3
    )
    
    # Define override function
    async def override_get_current_user():
        return mock_user
    
    # Apply override
    app.dependency_overrides[get_current_user] = override_get_current_user
    
    try:
        response = client.get("/api/users/me", headers={"Authorization": "Bearer mocked-token"})
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "override@lumina.edu"
        assert data["name"] == "Override User"
    finally:
        # Clean up
        app.dependency_overrides = {}

def test_get_current_user_me_no_token():
    """Test /api/users/me without token returns 403 (Not Authenticated/Forbidden)."""
    # Ensure no overrides
    app.dependency_overrides = {}
    
    response = client.get("/api/users/me")
    # FastAPI HTTPBearer returns 403 Not Authenticated when header is missing in some versions, or 401. 
    # Let's check for either to be robust, usually it is 403 Forbidden for missing creds in AutoError=True
    assert response.status_code in [401, 403]
