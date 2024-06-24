from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from typing import List, Optional, Annotated
from app.repository.location_category_reviewed_repository import (
    LocationCategoryReviewedRepository as ReviewRepository
)
from app.repository.category_repository import CategoryRepository
from app.repository.location_repository import LocationRepository
from app.schemas.location_category_reviewed import (
    LocationCategoryReviewedRequest as ReviewRequest,
    LocationCategoryReviewedResponse as ReviewRespose,
)


class LocationCategoryReviewedService:
    def __init__(
            self,
            review_repo: Annotated[
                ReviewRepository, Depends(ReviewRepository)
            ],
            category_repo: Annotated[
                CategoryRepository, Depends(CategoryRepository)
            ],
            location_repo: Annotated[
                LocationRepository, Depends(LocationRepository)
            ],
            ):
        self.review_repo = review_repo
        self.category_repo = category_repo
        self.location_repo = location_repo

    def create(self, data: ReviewRequest) -> ReviewRespose:
        if not self.location_repo.location_exist_by_id(data.location_id):
            raise HTTPException(
                status_code=400,
                detail="Location not found"
            )
        if not self.category_repo.category_exist_by_id(data.category_id):
            raise HTTPException(
                status_code=400,
                detail="Category not found"
            )

        if self.review_repo.review_exist(data.category_id, data.location_id):
            raise HTTPException(
                status_code=400,
                detail="Review all ready created"
            )
        return self.review_repo.create(data)

    def get_all(self) -> List[Optional[ReviewRespose]]:
        return self.review_repo.get_all()

    def get_suggested(self, user_id: int, days_ago: int, results: int):
        date_days_ago = datetime.now() - timedelta(days=days_ago)

        return self.review_repo.get_suggested(user_id, date_days_ago, results)

    def update(self, _id: int) -> ReviewRespose:
        if not self.review_repo.review_exist_by_id(_id):
            raise HTTPException(status_code=404, detail="Review not found")
        review = self.review_repo.get_by_id(_id)
        return self.review_repo.update(review)
