from typing import Dict
from pydantic import BaseModel

from random import seed
from random import random

seed(42)

class ProductInDB(BaseModel):
    nombre: str
    descripcion: str
    precio: float

database_products = Dict[str, ProductInDB]

database_products = {
    "1": ProductInDB(**{"nombre": "laptop",
                        "descripcion": "lenovo thinkpad x1 carbon 6th generation",
                        "precio": 1300.99}),
    "2": ProductInDB(**{"nombre": "teclado",
                        "descripcion": "Corsair K68 RGB Gaming Keyboard",
                        "precio": 150}),
}

def get_all_products():
    return database_products.values()

def get_single_product(product_id: str):
    if product_id in database_products.keys():
        return database_products[product_id]
    else:
        return None

# no sirve xd
# def add_product(product: ProductInDB):
#     new_idx = random()
#     database_products[str(new_idx)] = product
#     return database_products[str(new_idx)]