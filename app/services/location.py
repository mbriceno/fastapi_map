from fastapi import HTTPException, Depends
from typing import List, Optional, Annotated
from app.repository.location_repository import LocationRepository
from app.schemas.location import LocationRequest, LocationResponse


class LocationService:
    def __init__(
            self,
            repo: Annotated[LocationRepository, Depends(LocationRepository)]
            ):
        self.repository = repo

    def create(self, data: LocationRequest) -> LocationResponse:
        if self.repository.location_exist(data.latitude, data.longitude):
            raise HTTPException(
                status_code=400,
                detail="Location already exists"
                )
        return self.repository.create(data)

    def get_all(self) -> List[Optional[LocationResponse]]:
        return self.repository.get_all()

    def delete(self, _id: int) -> bool:
        if not self.repository.location_exist_by_id(_id):
            raise HTTPException(status_code=404, detail="Location not found")
        location = self.repository.get_by_id(_id)
        self.repository.delete(location)
        return True

    def update(self, _id: int, data: LocationRequest) -> LocationResponse:
        if not self.repository.location_exist_by_id(_id):
            raise HTTPException(status_code=404, detail="Category not found")
        location = self.repository.get_by_id(_id)
        return self.repository.update(location, data)
