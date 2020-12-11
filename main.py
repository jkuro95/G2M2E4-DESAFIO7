from db.user_db import get_user, get_all_users
from db.products_db import ProductInDB, get_all_products, get_single_product, create_product, change_product

from models.user_models import UserIn, UserOut
from models.product_models import ProductOut, ProductAddCantIn, ProductAddCantOut

# import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()


# Homepage Route
@api.get('/')
async def read_root():
    return { "Hello": "SIXGINFO" }


# User Auth Route
@api.post("/user/auth")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return { "Autenticado": False }   
    return { "Autenticado": True }


#All Users Route
@api.get("/user")
async def list_users():
    users_in_db = get_all_users()
    users_out = []
    for user in users_in_db:
        user_out = UserOut(**user.dict())
        users_out.append(user_out)
    return users_out


# All Products Route 
@api.get('/productos')
async def read_products():
    products_in_db = get_all_products()
    products_out = []
    for prod in products_in_db:
        product_out = ProductOut(**prod.dict())     
        products_out.append(product_out)   
    return products_out
    
    
# Specific Product Route
@api.get("/productos/{product_id}")
async def read_product(product_id: int):
    product_in_db = get_single_product(str(product_id)) # FastAPI parses endpoint params based on Python's type hints but the fake db stores dict keys as strings.
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")
    return product_in_db


# New Product Route
@api.post("/productos")
async def add_product(product: ProductInDB):
    product_added_to_db = create_product(product)
    return product_added_to_db

# aumentar la cantidad del producto
@api.put("/productos/{product_id}")
async def add_cant(product_add_cant_in: ProductAddCantIn):

    product_in_db = get_single_product(product_add_cant_in.product_id)

    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")

    product_in_db.cantidad = product_in_db.cantidad + product_add_cant_in.cantidad

    product_change_to_db = change_product(product_in_db, product_add_cant_in.product_id)

    product_add_cant_out = ProductAddCantOut(**{"nombre": product_change_to_db.nombre,
                                                "cantidad": product_change_to_db.cantidad})

    return product_add_cant_out




