from typing import Dict
from pydantic import BaseModel
from models.product_models import AllProductOut, ProductAddCantIn, ProductAddCantOut, AddProductIn

class ProductInDB(BaseModel):
    product_id: int
    nombre: str
    descripcion: str
    precio: float
    costo: float
    cantidad: int

database_products = Dict[str, ProductInDB]

database_products = {
    "1": ProductInDB(**{"product_id": 1,
                        "nombre": "laptop",
                        "descripcion": "lenovo thinkpad x1 carbon 6th generation",
                        "precio": 1299.99,
                        "costo": 900,
                        "cantidad":25}),
    "2": ProductInDB(**{"product_id":2,
                        "nombre": "teclado",
                        "descripcion": "Corsair K68 RGB Gaming Keyboard",
                        "precio": 150,
                        "costo": 70,
                        "cantidad": 32}),
}

def get_all_products():
    return database_products.values()

def get_single_product(product_id: str):
    if product_id in database_products.keys():
        return database_products[product_id]
    else:
        return None

def create_product(Add_Product_In: AddProductIn):

    new_idx = len(database_products) + 1

    product_in_db = ProductInDB(**{"product_id": new_idx,
                                    "nombre": Add_Product_In.nombre,
                                    "descripcion": Add_Product_In.descripcion,
                                    "precio": Add_Product_In.precio,
                                    "costo": Add_Product_In.costo,
                                    "cantidad": Add_Product_In.cantidad})
    database_products[str(new_idx)] = product_in_db
    return database_products[str(new_idx)]

def change_product(product_in_db: ProductInDB, product_id: str):
    temp_product = {product_id : product_in_db}
    database_products.update(temp_product)
    return database_products[product_id]