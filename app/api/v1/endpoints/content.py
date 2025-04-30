from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.db.session import get_db
from app.schemas.content import Content, ContentCreate, ContentUpdate, ContentResponse
from app.crud.content import content_crud
from app.api.deps import get_current_active_user
from app.models.user import User

router = APIRouter()


@router.get("/content", response_model=List[Content])
async def get_content(
    skip: int = 0,
    limit: int = 10,
    content_type: Optional[str] = None,
    category: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Get content with optional filtering"""
    filters = {}
    if content_type:
        filters["content_type"] = content_type
    if category:
        filters["category"] = category

    content = await content_crud.get_multi(
        db,
        skip=skip,
        limit=limit,
        filters=filters
    )
    return content

@router.get("/content/{content_id}", response_model=ContentResponse)
async def get_content_by_id(
    content_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific content by ID"""
    content = await content_crud.get(db, id=content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    # Calculate engagement rate
    total_views = content.view_count or 0
    total_engagement = (content.like_count or 0) + (content.share_count or 0)
    engagement_rate = (total_engagement / total_views) if total_views > 0 else 0

    return ContentResponse(
        **content.dict(),
        engagement_rate=engagement_rate
    )

@router.post("/content", response_model=Content)
async def create_content(
    content: ContentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create new content"""
    return await content_crud.create(db, obj_in=content)

@router.put("/content/{content_id}", response_model=Content)
async def update_content(
    content_id: int,
    content: ContentUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update existing content"""
    db_content = await content_crud.get(db, id=content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return await content_crud.update(db, db_obj=db_content, obj_in=content)

@router.post("/content/{content_id}/like")
async def like_content(
    content_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Increment like count for content"""
    content = await content_crud.get(db, id=content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    content.like_count = (content.like_count or 0) + 1
    await db.commit()
    return {"message": "Content liked successfully"}

@router.post("/content/{content_id}/share")
async def share_content(
    content_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Increment share count for content"""
    content = await content_crud.get(db, id=content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    content.share_count = (content.share_count or 0) + 1
    await db.commit()
    return {"message": "Content shared successfully"}
