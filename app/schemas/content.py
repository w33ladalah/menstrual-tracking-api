from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ContentBase(BaseModel):
    title: str
    content_type: str
    content: str
    author: Optional[str] = None
    tags: List[str] = []
    category: Optional[str] = None
    target_audience: Optional[str] = None

class ContentCreate(ContentBase):
    pass

class ContentUpdate(ContentBase):
    title: Optional[str] = None
    content_type: Optional[str] = None
    content: Optional[str] = None

class ContentInDBBase(ContentBase):
    id: int
    published_date: datetime
    is_published: bool
    view_count: int
    like_count: int
    share_count: int

    class Config:
        from_attributes = True

class Content(ContentInDBBase):
    pass

class ContentResponse(Content):
    engagement_rate: Optional[float] = None
