from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: str = "viewer"
    

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True