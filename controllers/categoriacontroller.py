from flask_restful import Resource, request
from models import CategoriaModel
from dtos import CategoriaRequestDto
from decorators import validador_usuario_admin
from flask_jwt_extended import jwt_required, get_jwt_identity
from bd import conexion


class CategoriasController(Resource):
    @validador_usuario_admin
    def post(self):
      
        dto = CategoriaRequestDto()
        try:
            dataVerificada = dto.load(request.get_json())
            nuevaCategoria = CategoriaModel(**dataVerificada)
            conexion.session.add(nuevaCategoria)
            conexion.session.commit()
            return {
                'message': 'Categoria creada'
            }, 200
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'error al crear',
                'content': e.args
            }, 400

  






