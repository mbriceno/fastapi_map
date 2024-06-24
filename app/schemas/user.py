from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: str = Field(min_length=1, max_length=150)


class UserRequest(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
        allow_population_by_field_name = True
