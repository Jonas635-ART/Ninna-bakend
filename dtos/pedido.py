from marshmallow import Schema, fields
from models import PedidoModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class DetallePedidoRequestDto(Schema):
    productoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)
    precio = fields.Float(required=True)
    

class PedidoRequestDto(Schema):
    detallePedido = fields.List(cls_or_instance=fields.Nested(nested = DetallePedidoRequestDto()))

class PedidoResponseDTO(SQLAlchemyAutoSchema):
    pedido = fields.Nested(PedidoRequestDto)
    class Meta:
        model= PedidoModel

