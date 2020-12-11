from pydantic import BaseModel


class ProductOut(BaseModel):
    nombre: str
    descripcion: str
    precio: float
