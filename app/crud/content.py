from typing import List, Optional
from app.crud.base import CRUDBase
from app.models.content import Content
from app.schemas.content import ContentCreate, ContentUpdate

class CRUDContent(CRUDBase[Content, ContentCreate, ContentUpdate]):
    async def get_by_type(
        self, db: AsyncSession, *, content_type: str, skip: int = 0, limit: int = 100
    ) -> List[Content]:
        return await self.get_multi(
            db,
            skip=skip,
            limit=limit,
            filters={"content_type": content_type}
        )

    async def get_by_category(
        self, db: AsyncSession, *, category: str, skip: int = 0, limit: int = 100
    ) -> List[Content]:
        return await self.get_multi(
            db,
            skip=skip,
            limit=limit,
            filters={"category": category}
        )

    async def increment_view_count(
        self, db: AsyncSession, *, content_id: int
    ) -> Optional[Content]:
        content = await self.get(db, id=content_id)
        if content:
            content.view_count = (content.view_count or 0) + 1
            await db.commit()
            await db.refresh(content)
        return content

content_crud = CRUDContent(Content)
