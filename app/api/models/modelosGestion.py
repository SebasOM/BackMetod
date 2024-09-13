from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#crear instancia de la base para crear tablas
Base=declarative_base()

#Listado modelos de la Aplicacion

#USUARIO
class Usuario(Base):
    _tablename_='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(20))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

#GASTO
class Gasto(Base):
    _tablename_='Gastos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(100))
    nombre=Column(String(50))

#INGRESO
class Ingreso(Base):
    _tablename_='Ingreso'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(100))
    nombre=Column(String(50))

#CATEGORIA
class Categoria(Base):
    _tablename_='Categoria'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(100))

#MOVIMIENTO
class Movimiento(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    Cantidad=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(100))
    
#METODO DE PAGO
class MetodoPago(Base):
    _tablename_='MetodoPago'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(100))

#FACTURA
class Factura(Base):
    _tablename_='Factura'
    id=Column(Integer, primary_key=True, autoincrement=True)