from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from datetime import datetime, timedelta

from app.db.session import get_db
from app.schemas.cycle import Cycle, CycleCreate, CycleUpdate, CyclePrediction
from app.services.prediction import PredictionService
from app.crud.cycle import cycle_crud

router = APIRouter()
prediction_service = PredictionService()

@router.get("/cycles", response_model=List[Cycle])
async def get_cycles(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all cycles for the current user"""
    cycles = await cycle_crud.get_multi(db, skip=skip, limit=limit)
    return cycles

@router.post("/cycles", response_model=Cycle)
async def create_cycle(
    cycle: CycleCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new cycle entry"""
    return await cycle_crud.create(db, obj_in=cycle)

@router.get("/cycles/{cycle_id}", response_model=Cycle)
async def get_cycle(
    cycle_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific cycle by ID"""
    cycle = await cycle_crud.get(db, id=cycle_id)
    if not cycle:
        raise HTTPException(status_code=404, detail="Cycle not found")
    return cycle

@router.put("/cycles/{cycle_id}", response_model=Cycle)
async def update_cycle(
    cycle_id: int,
    cycle: CycleUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a cycle entry"""
    db_cycle = await cycle_crud.get(db, id=cycle_id)
    if not db_cycle:
        raise HTTPException(status_code=404, detail="Cycle not found")
    return await cycle_crud.update(db, db_obj=db_cycle, obj_in=cycle)

@router.get("/cycles/predict", response_model=CyclePrediction)
async def predict_next_cycle(
    db: AsyncSession = Depends(get_db)
):
    """Get AI prediction for next cycle"""
    # Get historical cycles
    historical_cycles = await cycle_crud.get_multi(db)

    # Get current symptoms (you'll need to implement this)
    current_symptoms = {}

    # Get user metadata (you'll need to implement this)
    user_metadata = {}

    # Get prediction
    prediction = await prediction_service.predict_cycle(
        historical_cycles=historical_cycles,
        current_symptoms=current_symptoms,
        user_metadata=user_metadata
    )

    return prediction
