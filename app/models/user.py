from sqlalchemy import Column, String, Boolean, DateTime, JSON
from app.db.base import Base

class User(Base):
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # Account linking
    linked_accounts = Column(JSON, default={})  # Store OAuth providers and tokens
    consent_given = Column(Boolean, default=False)
    consent_date = Column(DateTime)
    consent_version = Column(String)  # Track which version of consent was given
