from config import conexion
from sqlalchemy import Column, types

class Descripcion (conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String(length=45), nullable=False)
    color = Column(type_=types.String(length=45), nullable=False)
    stock = Column(type_=types.Integer, nullable=False)
    precio = Column(type_=types.String(length=45), nullable=False)

    __tablename__ = 'descripciones'












































