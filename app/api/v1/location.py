from fastapi import APIRouter, Depends
from typing import List, Annotated
from app.schemas.location import LocationRequest, LocationResponse
from app.services.location import LocationService


router = APIRouter(
    prefix="/locations",
    tags=["location"]
)


@router.post(
    "",
    status_code=201,
    response_model=LocationResponse,
    summary="Create a new Location"
)
def create(
    data: LocationRequest,
    handler: Annotated[LocationService, Depends(LocationService)],
):
    return handler.create(data)


@router.get(
    "",
    status_code=200,
    response_model=List[LocationResponse],
    summary="Return a list with Location objects"
)
def get_locations(
    handler: Annotated[LocationService, Depends(LocationService)]
):
    return handler.get_all()


@router.delete(
    "/{_id}",
    status_code=204,
    summary="Delete a Location by id"
)
def delete_location(
    _id: int,
    handler: Annotated[LocationService, Depends(LocationService)]
):
    return handler.delete(_id)


@router.put(
    "/{_id}",
    status_code=200,
    response_model=LocationResponse,
    summary="Update all attributes in a Location object"
)
def update_location(
    _id: int,
    data: LocationRequest,
    handler: Annotated[LocationService, Depends(LocationService)]
):
    return handler.update(_id, data)
