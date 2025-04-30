from sqlalchemy import Column, Integer, DateTime, Float, Boolean, ForeignKey, JSON, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cycle(Base):
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    is_predicted = Column(Boolean, default=False)

    # Symptoms and tracking
    symptoms = Column(JSON, default={})  # Store symptoms as JSON
    mood = Column(String)
    flow_intensity = Column(String)  # light, medium, heavy
    notes = Column(String)

    # AI predictions
    predicted_ovulation_date = Column(DateTime)
    predicted_period_start = Column(DateTime)
    prediction_confidence = Column(Float)
    prediction_metadata = Column(JSON)  # Store AI model metadata

    # Relationships
    user = relationship("User", back_populates="cycles")
