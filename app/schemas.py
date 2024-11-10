from pydantic import BaseModel, EmailStr, Field
from bson.objectid import ObjectId

class UserSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr = Field(...)
    password: str = Field(...)
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }