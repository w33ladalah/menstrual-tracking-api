from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime

class CycleBase(BaseModel):
    start_date: datetime
    end_date: Optional[datetime] = None
    symptoms: Dict = {}
    mood: Optional[str] = None
    flow_intensity: Optional[str] = None
    notes: Optional[str] = None

class CycleCreate(CycleBase):
    pass

class CycleUpdate(CycleBase):
    pass

class CycleInDBBase(CycleBase):
    id: int
    user_id: int
    is_predicted: bool = False
    predicted_ovulation_date: Optional[datetime] = None
    predicted_period_start: Optional[datetime] = None
    prediction_confidence: Optional[float] = None
    prediction_metadata: Optional[Dict] = None

    class Config:
        from_attributes = True

class Cycle(CycleInDBBase):
    pass

class CyclePrediction(BaseModel):
    predicted_ovulation_date: datetime
    predicted_period_start: datetime
    confidence: float
    metadata: Optional[Dict] = None
