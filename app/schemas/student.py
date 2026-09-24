from pydantic import BaseModel, EmailStr, Field


class StudentBase(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    age: int = Field(
        ge=1,
        le=100
    )

    course: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):

    id: int

    class Config:
        from_attributes = True