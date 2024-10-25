from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20), unique=True)
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

#GASTO
class Gasto(Base):
     __tablename__='gastos'
     id=Column(Integer, primary_key=True, autoincrement=True)
     monto=Column(Integer)
     fecha=Column(Date)
     descripcion=Column(String(200))
     nombre=Column(String(20))
    

#CATEGORIA
class Categoria(Base):
     __tablename__='categoria'
     id=Column(Integer, primary_key=True, autoincrement=True)
     nombreCategoria=Column(String(20))
     descripcion=Column(String(200))
     
#METODOS DE PAGO
class MetodoPago(Base):
     __tablename__='metodopago'
     id=Column(Integer, primary_key=True, autoincrement=True)
     nombreMetodo=Column(String(20))
     descripcion=Column(String(200))
