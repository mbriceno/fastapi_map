from fastapi import HTTPException, Depends
from typing import List, Optional, Annotated
from app.repository.category_repository import CategoryRepository
from app.schemas.category import CategoryRequest, CategoryResponse


class CategoryService:
    def __init__(
            self,
            repo: Annotated[CategoryRepository, Depends(CategoryRepository)]
            ):
        self.repository = repo

    def create(self, data: CategoryRequest) -> CategoryResponse:
        if self.repository.category_exist_by_name(data.name):
            raise HTTPException(
                status_code=400,
                detail="Category already exists"
                )
        return self.repository.create(data)

    def get_all(self) -> List[Optional[CategoryResponse]]:
        return self.repository.get_all()

    def delete(self, _id: int) -> bool:
        if not self.repository.category_exists_by_id(_id):
            raise HTTPException(status_code=404, detail="Category not found")
        category = self.repository.get_by_id(_id)
        self.repository.delete(category)
        return True

    def update(self, _id: int, data: CategoryRequest) -> CategoryResponse:
        if not self.repository.category_exist_by_id(_id):
            raise HTTPException(status_code=404, detail="Category not found")
        category = self.repository.get_by_id(_id)
        return self.repository.update(category, data)
