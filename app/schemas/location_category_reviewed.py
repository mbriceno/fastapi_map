from pydantic import BaseModel
from datetime import datetime
from typing import Union
from app.schemas.category import CategoryResponse
from app.schemas.location import LocationResponse


class LocationCategoryReviewedBase(BaseModel):
    visit: int
    last_visit: Union[datetime, None]


class LocationCategoryReviewedRequest(LocationCategoryReviewedBase):
    category_id: int
    location_id: int


class LocationCategoryReviewedResponse(LocationCategoryReviewedBase):
    id: int
    category: CategoryResponse
    location: LocationResponse

    class Config:
        orm_mode = True
