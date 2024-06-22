from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from app.config.database import Base


class LocationCategoryReviewed(Base):
    __tablename__ = "location_category_reviewed"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    location_id = Column(
        Integer,
        ForeignKey('locations.id'),
        primary_key=True
    )
    location = relationship(
        "Location",
        back_populates="categories"
    )
    category_id = Column(
        Integer,
        ForeignKey('categories.id'),
        primary_key=True
    )
    category = relationship(
        "Category",
        back_populates="locations"
    )
    visit = Column(Integer, nullable=False, default=0)
    last_visit = Column(DateTime, nullable=True)
