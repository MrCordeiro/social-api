"""
Defines the formats data must follow both in the request as well as in the response.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


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
    owner_id: int
    owner: UserOut

    class Config:
        # This tells pydantic it will receive a SQLAlchemy instance, and that it
        # should convert to a Pydantic instance before validating it.
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
