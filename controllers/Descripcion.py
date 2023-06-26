from flask_restful import Resource, request
from models.descripcion import Descripcion
from dtos.descripcion_dto import DescripcionRequestDTO, DescripcionResponseDTO, BuscarDescripcionRequestDTO
from dtos.pagina_dto import PageRequestDTO
from config import conexion
from math import ceil

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
        query_params = request.args
        paginacion = PageRequestDTO().load(query_params)
        perPage = paginacion.get('perPage')
        page = paginacion.get('page')
        skip = perPage * (page - 1)
        descripcions = conexion.session.query(Descripcion).limit(paginacion.get('perPage')).offset(skip).all()
        total = conexion.session.query(Descripcion).count()
        itemsXpages = perPage if total >= perPage else total
        totalPages = ceil(total / itemsXpages) if itemsXpages > 0 else None
        prevPage = page - 1 if page > 1 and page <= totalPages else None
        nextPage = page + 1 if page > 1 and page < totalPages else None
        respuesta = DescripcionResponseDTO(many=True).dump(descripcions)
        return {
            'message': 'las descripciones son',
            'pagination': {
                'total': total,
                'items': itemsXpages,
                'prevPage': prevPage,
                'nextPage': nextPage
            },
            'content': respuesta
        }

class buscarDescripcionController(Resource):
    def get(self):
        query_params = request.args
        try:
            parametros = BuscarDescripcionRequestDTO().load(query_params)
            print(parametros)

            busqueda2 = conexion.session.query(Descripcion).filter(Descripcion.nombre.like('a')).all()
            print(busqueda2)
            nombre = parametros.get('nombre', '')
            if parametros.get('nombre') is not None:
                del parametros['nombre']
            busquedas = conexion.session.query(Descripcion).filter(Descripcion.nombre.like('%{}%'.format(nombre))).filter_by(**parametros).all()  
            resultado = DescripcionResponseDTO(many=True).dump(busquedas)
            print(busquedas)

            return {
                'message': '',
                'content': resultado
            }
        except Exception as e:
            return { 
                'message': 'error al buscar',
                'content': e.args
            }, 400













 





























