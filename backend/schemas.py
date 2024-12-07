from pydantic import BaseModel, Field
from typing import Optional
class Product(BaseModel):
    name: str = Field(max_length=100, description='Product name.')
    description: str = Field(max_length=100, description='Product description.')
    price: float | None = Field(gt=0, description="Price must be greater than zero.")

    class Config:
        orm_mode = True


class ProductPatch(BaseModel):
    name: Optional[str] = Field(None, max_length=100, description="Product name.")
    description: Optional[str] = Field(None, max_length=100, description="Product description.")
    price: Optional[float] = Field(default=None, gt=0, description='Price must be greater than zero')
    
    class Config:
        orm_mode = True
