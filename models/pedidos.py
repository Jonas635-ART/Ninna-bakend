from config import conexion
from sqlalchemy import Column, types, orm
from sqlalchemy.sql.schema import ForeignKey

class Pedidos(conexion.Model):
    __tablename__ = 'pedidos'
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(length=45), nullable=False)
    telefono = Column(type_=types.Integer, nullable=False)
    direccion = Column(type_=types.String(length=45), nullable=False)
    Bralettes_id = Column(ForeignKey(column='Bralettes_id', type_=types.Integer))

    Bralette = orm.relationship('Bralette',backref='Pedidos')
   







































