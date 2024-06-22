from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from app.config.database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    locations = relationship(
        "LocationCategoryReviewed",
        back_populates="category"
    )
