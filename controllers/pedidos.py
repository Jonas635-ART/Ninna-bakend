from flask_restful import Resource, request
from models.pedidos import Pedidos
from dtos.pedidos_dto import PedidosRequestDTO, PedidosresponseDTO
from config import conexion

 
class PedidosController(Resource):
    def post(self):
        try:
            body = request.get_json()
            data = PedidosRequestDTO().load(body)
            print(data)
            nuevopedido = Pedidos(**data)
            conexion.session.add(nuevopedido)
            conexion.session.commit()
            respuesta = PedidosresponseDTO().dump(nuevopedido)           
            return {
                'message': 'bien',
                'content': respuesta
            },201

        except Exception as e:
            return {
                'message': 'error',
                'content': e.args
            }, 400
    def get(self):
        pedido: Pedidos | None = conexion.session.query(Pedidos).filter_by(id=1).first()
        print(pedido)
        print(pedido.Bralettes_id)
        return {
            'message': 'ok',
        }









































