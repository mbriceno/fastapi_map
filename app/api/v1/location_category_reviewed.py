from fastapi import APIRouter, Depends
from typing import List, Annotated
from app.schemas.location_category_reviewed import (
    LocationCategoryReviewedRequest as ReviewRequest,
    LocationCategoryReviewedResponse as ReviewResponse
)
from app.services.location_category_reviewed import (
    LocationCategoryReviewedService as ReviewService
)


router = APIRouter(
    prefix="/reviews",
    tags=["review"]
)


@router.post(
    "",
    status_code=201,
    response_model=ReviewResponse,
    summary="Create a new recommendation associating a category and location"
)
def create(
    data: ReviewRequest,
    handler: Annotated[ReviewService, Depends(ReviewService)],
):
    return handler.create(data)


@router.get(
    "",
    status_code=200,
    response_model=List[ReviewResponse],
    summary="Return a list of all the reviews. "
    "@TODO: add pagination with fastapi-pagination module or any other"
)
def get_locations(
    handler: Annotated[ReviewService, Depends(ReviewService)]
):
    return handler.get_all()


@router.get(
    "/suggested",
    status_code=200,
    response_model=List[ReviewResponse],
    summary="Return by default a top 10 locations-cateogry "
    "reviewed by user in the last 30 days"
)
def get_suggested(
    handler: Annotated[ReviewService, Depends(ReviewService)],
    user_id: int,
    days_ago: int = 30,
    page_size: int = 10,
):
    return handler.get_suggested(user_id, days_ago, page_size)


@router.put(
    "/{_id}",
    status_code=200,
    response_model=ReviewResponse,
    summary="Update visits and last visit attributes "
    "in location-category object"
)
def update_location(
    _id: int,
    handler: Annotated[ReviewService, Depends(ReviewService)]
):
    return handler.update(_id)
