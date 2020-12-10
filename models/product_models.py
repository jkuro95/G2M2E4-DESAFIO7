from pydantic import BaseModel

class ProductSchema(BaseModel):
    nombre: str
    descripcion: str
    precio: float
