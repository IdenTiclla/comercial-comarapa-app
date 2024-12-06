from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
# from pydantic import BaseModel, Field
from . import models, schemas
from .database import engine, get_db

# create database tables
models.Base.metadata.create_all(bind=engine)

# fake_products = [
#     {"name": "Pelota futbol", "description": "La pelota de futbol oficial", "price": 125},
#     {"name": "Pelota basket", "description": "La de basket oficial", "price": 75},
#     {"name": "Pelota raqueta", "description": "La raqueta oficial", "price": 60}
# ]
app = FastAPI()




@app.get('/')
def get_main():
    return "hello world"

@app.post('/products')
def create_product(product: schemas.Product, db: Session = Depends(get_db)) -> schemas.Product:
    new_product = models.Product(
        name = product.name,
        description = product.description,
        price = product.price
    )
    # fake_products.append(product)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get('/products/{product_id}')
def get_specific_product(product_id: int, db: Session = Depends(get_db)) -> schemas.Product:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El producto con el id: {product_id} no existe."
        )
    return product

@app.delete('/products/{product_id}')
def delete_specific_user(product_id: int, db: Session = Depends(get_db)) -> schemas.Product:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El producto con el id: {product_id} no existe."
        )
    
    # Borrando el producto
    db.delete(product)
    db.commit()

    return product


@app.get('/products') 
def get_products(db: Session = Depends(get_db)) -> list[schemas.Product]:
    users = db.query(models.Product).all()
    return users