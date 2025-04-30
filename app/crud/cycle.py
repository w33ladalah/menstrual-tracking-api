from typing import List, Optional
from app.crud.base import CRUDBase
from app.models.cycle import Cycle
from app.schemas.cycle import CycleCreate, CycleUpdate

class CRUDCycle(CRUDBase[Cycle, CycleCreate, CycleUpdate]):
    async def get_by_user(
        self, db: AsyncSession, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Cycle]:
        return await self.get_multi(
            db,
            skip=skip,
            limit=limit,
            filters={"user_id": user_id}
        )

    async def get_current_cycle(
        self, db: AsyncSession, *, user_id: int
    ) -> Optional[Cycle]:
        result = await db.execute(
            select(self.model)
            .filter(self.model.user_id == user_id)
            .order_by(self.model.start_date.desc())
        )
        return result.scalar_one_or_none()

cycle_crud = CRUDCycle(Cycle)
