from flask_restful import Resource, request
from models.descripcion import Descripcion
from dtos.descripcion_dto import DescripcionRequestDTO, DescripcionResponseDTO
from config import conexion

class DescripcionController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = DescripcionRequestDTO().load(body)
            Nuevadescripcion = Descripcion(
                nombre = data.get('nombre'),
                color = data.get('color'),
                stock = data.get('stock'),
                precio = data.get('precio'),
            )
            
            conexion.session.add(Nuevadescripcion)
            conexion.session.commit()
            respuesta = DescripcionResponseDTO().dump(Nuevadescripcion)

            return {
                'message': 'exitosa creacion',
                'content': respuesta
            }, 201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message':'error',
                'content': e.args 
                }, 400
    def get(self):
        descripcions = conexion.session.query(Descripcion).all()
        respuesta = DescripcionResponseDTO(many=True).dump(descripcions)
        return {
            'message': 'las descripciones son',
            'content': respuesta
        }

class buscarDescripcionController(Resource):
    def get(self):
        query_params = request.args
        print(query_params.get('nombre'))
        
        busquedas = conexion.session.query(Descripcion).filter_by(**query_params).all()  
        print(busquedas)    
        return {
            'message': ''
        }














 





























