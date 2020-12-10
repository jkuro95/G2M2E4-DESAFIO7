from db.user_db import get_user
from db.products_db import ProductInDB, get_all_products, get_single_product, create_product

from models.user_models import UserIn, UserOut
from models.product_models import ProductSchema

# import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Homepage Route
@app.get('/')
async def read_root():
    return { "Hello": "SIXGINFO" }

# User Auth Route
@app.post("/user/auth")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        return { "Autenticado": False }
    
    return { "Autenticado": True }

# All Products Route 
@app.get('/productos')
async def read_products():
    products_in_db = get_all_products()
    product_list = []
    for prod in products_in_db:
        product_list.append(prod)
    return product_list
    
# Specific Product Route
@app.get("/productos/{product_id}")
async def read_product(product_id: int):
    product_in_db = get_single_product(str(product_id)) # FastAPI parses endpoint params based on Python's type hints but the fake db stores dict keys as strings.
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")
    return product_in_db

# New Product Route
@app.post("/productos")
# async def add_product(product: ProductSchema):
async def add_product(product: ProductInDB):
    # product_added_to_db = create_product(ProductInDB(product))
    product_added_to_db = create_product(product)
    return product_added_to_db
