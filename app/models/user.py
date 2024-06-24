from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    reviews = relationship(
        "LocationCategoryReviewed",
        back_populates="user"
    )
