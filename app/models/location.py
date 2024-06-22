from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from app.config.database import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    categories = relationship(
        "LocationCategoryReviewed",
        back_populates="location"
    )
