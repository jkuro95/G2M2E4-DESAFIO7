from pydantic import BaseModel

class AddProductIn(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    costo: float
    cantidad: int

class AddProductOut(BaseModel):
    nombre: str
    cantidad: int
    mensaje: str
    
class AllProductOut(BaseModel):
    product_id: int
    nombre: str
    cantidad: int
    precio: float

class ProductAddCantIn(BaseModel):
    product_id: str
    cantidad: int

class ProductAddCantOut(BaseModel):
    nombre: str
    cantidad: int

