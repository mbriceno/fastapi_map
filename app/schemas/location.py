from pydantic import BaseModel, Field


class LocationBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    latitude: float
    longitude: float


class LocationRequest(LocationBase):
    pass


class LocationResponse(LocationBase):
    id: int

    class Config:
        from_attributes = True
        allow_population_by_field_name = True
