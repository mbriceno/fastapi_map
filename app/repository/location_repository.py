from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List, Optional, Type, Annotated
from app.config.database import sess_db
from app.models.location import Location
from app.schemas.location import LocationRequest, LocationResponse


class LocationRepository:
    def __init__(self, session: Annotated[Session, Depends(sess_db)]):
        self.session = session

    def create(self, data: LocationRequest) -> LocationResponse:
        location = Location(**data.model_dump(exclude_none=True))
        self.session.add(location)
        self.session.commit()
        self.session.refresh(location)
        return LocationResponse(**location.__dict__)

    def get_all(self) -> List[Optional[LocationResponse]]:
        categories = self.session.query(Location).all()
        return [LocationResponse(**cat.__dict__) for cat in categories]

    def get_by_id(self, _id: int) -> Type[Location]:
        return self.session.query(Location).filter_by(id=_id).first()

    def get_location(self, _id: int) -> LocationResponse:
        location = self.session.query(Location).filter_by(id=_id).first()
        return LocationResponse(**location.__dict__)

    def location_exist(self, lat: float, lon: float) -> bool:
        location = self.session \
            .query(Location) \
            .filter_by(latitude=lat, longitude=lon) \
            .first()
        return location is not None

    def location_exist_by_id(self, _id: int) -> bool:
        location = self.session.query(Location).filter_by(id=_id).first()
        return location is not None

    def update(
            self,
            location: Type[Location],
            data: LocationRequest) -> LocationResponse:
        location.name = data.name
        location.latitude = data.latitude
        location.longitude = data.longitude
        self.session.commit()
        self.session.refresh(location)
        return LocationResponse(**location.__dict__)

    def delete(self, location: Type[Location]) -> bool:
        self.session.delete(location)
        self.session.commit()
        return True
