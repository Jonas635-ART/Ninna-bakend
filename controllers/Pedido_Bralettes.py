from flask_restful import Resource, request
from models.Pedido_Bralette import PedidoBralette
from dtos.PedidoBralette_dto import PedidoBraletteRequestDTO
from config import conexion

class PedidoBraletteController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = PedidoBraletteRequestDTO().load(body)
            nuevo=PedidoBralette(**data)
            conexion.session.add(nuevo)
            conexion.session.commit()
        except Exception as e:
            conexion.session.rollback()
            return {
                'message':'Error as ingresar',
                'content': e.args
            }, 400

























































