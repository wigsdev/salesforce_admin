"""
User model for authentication and user management.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    """
    User model for authentication and profile management.
    
    Attributes:
        id: Primary key
        name: Full name of the user
        email: Unique email for login
        password_hash: Hashed password (bcrypt)
        team: Team name (default: VISIONARY ADMINS)
        role: User role (student, instructor, admin)
        is_active: Whether the user account is active
        created_at: Timestamp of account creation
        updated_at: Timestamp of last update
        last_login: Timestamp of last login
    """
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    team = Column(String(50), default="VISIONARY ADMINS")
    role = Column(String(20), default="student")  # student, instructor, admin
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    last_login = Column(DateTime, nullable=True)
    
    # Relationships
    progress = relationship("UserProgress", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', role='{self.role}')>"
