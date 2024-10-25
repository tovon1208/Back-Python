from pydantic import BaseModel, Field
from datetime import date

#DTO
class UsuarioDTOPeticion(BaseModel):
    nombre:str
    edad:int
    telefono:str
    correo:str 
    contraseña:str
    fechaRegistro:date
    ciudad:str 
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombre:str
    telefono:str
    ciudad:str
    class Config:
        orm_mode=True

class GastoDTOPeticion(BaseModel):
    monto:int
    fecha:date
    descripcion:str
    nombre:str
    class config:
        orm_mode=True

class GastoDTORespuesta(BaseModel):
    id:int
    monto:int
    fecha:date
    descripcion:str
    nombre:str
    class config:
        orm_mode=True

class CategoriaDTOPeticion(BaseModel):
    nombre:str
    descripcion:str
    fotoicon:str
    class config:
        orm_mode=True

class CategoriaDTORespuesta(BaseModel):
    id:int
    nombre:str
    descripccion:str
    fotoicon:str
    class config:
        orm_mode=True

class MetodoPagoDTOPeticion(BaseModel):
    nombreMetodo:str
    descripcion:str
    class config:
        orm_mode=True

class MetodoPagoDTORespuesta(BaseModel):
    id:str
    nombreMetodo:str
    descripcion:str
    class config:
        orm_mode=True





