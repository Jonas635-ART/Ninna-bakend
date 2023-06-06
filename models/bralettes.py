from config import conexion
from sqlalchemy import Column, types

class Bralette(conexion.Model):

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(45), nullable=False, unique=True)

    __tablename__ = 'bralettes'








































