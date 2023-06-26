from config import conexion
from sqlalchemy import Column, types, orm 
from sqlalchemy.sql.schema import ForeignKey

class PedidoBralette(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    bralette_id = Column(ForeignKey(column='bralette_id'),type_=types.Integer)
    Descripcion_id = Column(ForeignKey(column='Descripcion_id'),type_=types.Integer)

    bralette = orm.relationship('bralette', backref='bralette_Descripcion')
    Descripcion = orm.relationship('Descripcion', backref='Descripcion_bralette')
    
    __tablename__ = 'bralette_Descripcion'











































