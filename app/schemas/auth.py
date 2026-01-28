"""
Pydantic schemas for authentication.
"""

from pydantic import BaseModel


class TokenResponse(BaseModel):
    """Schema for token response."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Schema for token payload data."""

    email: str | None = None
