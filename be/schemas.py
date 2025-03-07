
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int


class AssetBase(BaseModel):
    name: str
    description: str

class AssetCreate(AssetBase):
    pass

class AssetRead(AssetBase):
    id: int