from fastapi import APIRouter, Depends
from typing import List, Annotated
from app.schemas.category import CategoryRequest, CategoryResponse
from app.services.category import CategoryService


router = APIRouter(
    prefix="/categories",
    tags=["category"],
)


@router.post("", status_code=201, response_model=CategoryResponse, summary="Create Category")
def create(
    data: CategoryRequest,
    handler: Annotated[CategoryService, Depends(CategoryService)],
):
    return handler.create(data)


@router.get("", status_code=200, response_model=List[CategoryResponse])
def get_categories(
    handler: Annotated[CategoryService, Depends(CategoryService)]
):
    return handler.get_all()


@router.delete("/{_id}", status_code=204)
def delete_category(
    _id: int,
    handler: Annotated[CategoryService, Depends(CategoryService)]
):
    return handler.delete(_id)


@router.put("/{_id}", status_code=200, response_model=CategoryResponse)
def update_category(
    _id: int,
    data: CategoryRequest,
    handler: Annotated[CategoryService, Depends(CategoryService)]
):
    return handler.update(_id, data)
