from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.schemas.DTO import GastoDTOPeticion, GastoDTORespuesta
from app.api.schemas.DTO import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.schemas.DTO import MetodoPagoDTOPeticion, MetodoPagoDTORespuesta
from app.api.models.modelosApp import Gasto, Usuario, Categoria, MetodoPago
from app.database.configuration import sessionLocal, engine

#Para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase)):
    print(datosPeticion)
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        return usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario: {str(error)}")

    
    
@rutas.post("/gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion:GastoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        gastos=Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre,
        )
        db.add(gastos)
        db.commit()
        db.refresh(gastos)
        return gastos
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el gasto: {str(error)}")

@rutas.post("/categoria", response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion:CategoriaDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        categoria=Categoria(
            nombreCategoria=datosPeticion.nombreCategoria,
            descripcion=datosPeticion.descripcion,
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar la categoria: {str(error)}")


@rutas.post("/metodopago", response_model=MetodoPagoDTORespuesta)       
def guardarMetodoPago(datosPeticion:MetodoPagoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        metodopago=MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            descripcion=datosPeticion.descripcion,
        )
        db.add(metodopago)
        db.commit()
        db.refresh()
        return metodopago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el metodo de pago: {str(error)}")


@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return listadoDeUsuarios
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario: {str(error)}")
        
@rutas.get("/gastos", response_model=List[GastoDTORespuesta])
def buscarGastos(db:Session=Depends(getDataBase)):
    try:
        listadoDeGastos=db.query(Gasto).all()
        return listadoDeGastos
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el gasto: {str(error)}")

@rutas.get("/categoria", response_model=List[CategoriaDTORespuesta])
def buscarCategoria(db:Session=Depends(getDataBase)):
    try:
        listadoDeCategoria=db.query(Categoria).all()
        return listadoDeCategoria
    except Exception as error:
        db.raollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar la categoria: {str(error)}")

@rutas.get("/metodopago", response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoDePago(db:Session=Depends(getDataBase)):
    try:
        listadoDeMetodoDePago=db.query(MetodoPago).all()
        return listadoDeMetodoDePago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el metodo de pago: {str(error)}")
          
