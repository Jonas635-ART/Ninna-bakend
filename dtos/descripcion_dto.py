from config import validador
from models.descripcion import Descripcion
from marshmallow import fields


class DescripcionRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Descripcion

class DescripcionResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Descripcion

class BuscarDescripcionRequestDTO(validador.SQLAlchemyAutoSchema):
    nombre = fields.String(required= True)
    color = fields.String(required= False)
    stock = fields.Integer(required= False)
    precio = fields.String(required= True)









































