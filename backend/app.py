from fastapi import FastAPI
from pydantic import BaseModel, Field

fake_products = [
    {"name": "Pelota futbol", "description": "La pelota de futbol oficial", "price": 125},
    {"name": "Pelota basket", "description": "La de basket oficial", "price": 75},
    {"name": "Pelota raqueta", "description": "La raqueta oficial", "price": 60}
]
app = FastAPI()

class Product(BaseModel):
    name: str
    description: str
    price: float | None = Field(gt=0, description="Price must be greater than zero.")


@app.get('/')
def get_main():
    return "hello world"

@app.post('/products')
def create_product(product: Product) -> Product:
    fake_products.append(product)
    return product

@app.get('/products') 
def get_products() -> list[Product]:
    return fake_products