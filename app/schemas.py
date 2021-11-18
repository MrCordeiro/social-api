"""
Defines the formats data must follow both in the request as well as in the response.
"""
from datetime import datetime
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    """Schema used when retuning the Post in a response"""

    id: int
    created_at: datetime

    class Config:
        # This tells pydantic it will receive a SQLAlchemy instance, and that it
        # should convert to a Pydantic instance before validating it.
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
