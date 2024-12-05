from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    description: str
    price: float | None = Field(gt=0, description="Price must be greater than zero.")

    class Config:
        orm_mode = True