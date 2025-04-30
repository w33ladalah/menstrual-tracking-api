from sqlalchemy import Column, String, DateTime, Boolean, JSON, Text, Integer
from app.db.base import Base

class Content(Base):
    title = Column(String, nullable=False)
    content_type = Column(String, nullable=False)  # article, tip, inspiration
    content = Column(Text, nullable=False)
    author = Column(String)
    published_date = Column(DateTime)
    is_published = Column(Boolean, default=True)

    # Content metadata
    tags = Column(JSON, default=[])  # Store tags as JSON array
    category = Column(String)  # health, wellness, lifestyle, etc.
    target_audience = Column(String)  # all, specific_phase, etc.

    # Engagement tracking
    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    share_count = Column(Integer, default=0)
