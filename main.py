from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Product(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None



@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.post("/products", status_code=201)
async def create_product(product: Product):
    return {
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "tax": product.tax
    }