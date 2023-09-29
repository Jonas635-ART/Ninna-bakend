from bd import conexion
from sqlalchemy import Column, ForeignKey, types
from sqlalchemy.orm import relationship

class ProductoModel(conexion.Model):
    __tablename__='productos'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text)
    precio = Column(type_=types.Float, nullable=False)
    imagen = Column(type_=types.Text)
    stock = Column(type_=types.Integer, nullable=False)
    categoriaId = Column(ForeignKey(column='categorias.id'), type_=types.Integer
    , name='categoria_id')


    categoria = relationship('CategoriaModel', backref='productos')



