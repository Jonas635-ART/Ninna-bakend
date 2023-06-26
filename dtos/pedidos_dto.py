from config import validador
from models.pedidos import Pedidos
from marshmallow_sqlalchemy import fields
from models.bralettes import Bralettes

class PedidosRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Pedidos
        include_fk = True

class BraletteResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Bralettes

class PedidosresponseDTO(validador.SQLAlchemyAutoSchema):
    producto = fields.Nested(nested=PedidosresponseDTO, dat_key='pedidos')

    class Meta:
        model = Pedidos
        load_instance = True
        include_fk = True 
        include_realtionships = True






































