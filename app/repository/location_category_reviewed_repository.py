from datetime import datetime
from sqlalchemy.orm import Session
from typing import List, Optional, Annotated, Type
from fastapi import Depends
from app.models.location_category_reviewed import LocationCategoryReviewed
from app.schemas.location_category_reviewed import (
    LocationCategoryReviewedRequest as ReviewRequest,
    LocationCategoryReviewedResponse as ReviewResponse,
)
from app.schemas.category import CategoryResponse
from app.schemas.location import LocationResponse
from app.config.database import sess_db


class LocationCategoryReviewedRepository:
    def __init__(self, session: Annotated[Session, Depends(sess_db)]):
        self.session = session

    def create(
        self, data: ReviewRequest
    ) -> ReviewResponse:
        review = LocationCategoryReviewed(**data.model_dump(exclude_none=True))
        self.session.add(review)
        self.session.commit()
        self.session.refresh(review)
        return self._map_review_object(review)

    def get_all(self) -> List[Optional[ReviewResponse]]:
        reviews = self.session.query(LocationCategoryReviewed).all()
        return self._map_review_list(reviews)

    def get_by_id(self, _id: int) -> Type[LocationCategoryReviewed]:
        return self.session \
            .query(LocationCategoryReviewed) \
            .filter_by(id=_id) \
            .first()

    def get_review(self, _id: int) -> ReviewResponse:
        review = self.session \
            .query(LocationCategoryReviewed) \
            .filter_by(id=_id) \
            .first()
        return self._map_review_object(review)

    def review_exist(self, category_id: int, location_id: int) -> bool:
        review = self.session \
            .query(LocationCategoryReviewed) \
            .filter_by(category_id=category_id, location_id=location_id) \
            .first()
        return review is not None

    def review_exist_by_id(self, _id: int) -> bool:
        review = self.session \
            .query(LocationCategoryReviewed) \
            .filter_by(id=_id) \
            .first()
        return review is not None

    def update(
        self,
        review: Type[LocationCategoryReviewed]
    ) -> ReviewResponse:
        review.visit += 1
        review.last_visit = datetime.now()
        self.session.commit()
        self.session.refresh(review)
        return self._map_review_object(review)

    @staticmethod
    def _map_review_list(
        reviews: List[Type[LocationCategoryReviewed]]
    ) -> List[ReviewResponse]:
        return [
            __class__._map_review_object(r)
            for r in reviews
        ]

    @staticmethod
    def _map_review_object(
        r: Type[LocationCategoryReviewed]
    ) -> ReviewResponse:
        return ReviewResponse(
            id=r.id,
            category=CategoryResponse(
                id=r.category.id,
                name=r.category.name,
                description=r.category.description
            ),
            location=LocationResponse(
                id=r.location.id,
                name=r.location.name,
                latitude=r.location.latitude,
                longitude=r.location.longitude,
            ),
            visit=r.visit,
            last_visit=r.last_visit
        )
