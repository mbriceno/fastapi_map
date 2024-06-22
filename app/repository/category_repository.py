from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List, Optional, Type, Annotated
from app.config.database import sess_db
from app.models.category import Category
from app.schemas.category import CategoryRequest, CategoryResponse


class CategoryRepository:
    def __init__(self, session: Annotated[Session, Depends(sess_db)]):
        self.session = session

    def create(self, data: CategoryRequest) -> CategoryResponse:
        category = Category(**data.model_dump(exclude_none=True))
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        return CategoryResponse(**category.__dict__)

    def get_all(self) -> List[Optional[CategoryResponse]]:
        categories = self.session.query(Category).all()
        return [CategoryResponse(**cat.__dict__) for cat in categories]

    def get_by_id(self, _id: int) -> Type[Category]:
        return self.session.query(Category).filter_by(id=_id).first()

    def get_category(self, _id: int) -> CategoryResponse:
        category = self.session.query(Category).filter_by(id=_id).first()
        return CategoryResponse(**category.__dict__)

    def category_exist_by_name(self, name: str) -> bool:
        category = self.session.query(Category).filter_by(name=name).first()
        return category is not None

    def category_exist_by_id(self, _id: int) -> bool:
        category = self.session.query(Category).filter_by(id=_id).first()
        return category is not None

    def update(
        self,
        category: Type[Category],
        data: CategoryRequest
    ) -> CategoryResponse:
        category.name = data.name
        category.description = data.description
        self.session.commit()
        self.session.refresh(category)
        return CategoryResponse(**category.__dict__)

    def delete(self, category: Type[Category]) -> bool:
        self.session.delete(category)
        self.session.commit()
        return True
