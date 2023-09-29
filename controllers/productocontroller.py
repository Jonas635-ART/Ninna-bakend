from flask_restful import Resource, request
from models import ProductoModel, CategoriaModel
from decorators import validador_usuario_admin
from dtos import ProductoRequestDto, ProductoResponseDto
from bd import conexion

class ProductosController(Resource):
      @validador_usuario_admin
      def post(self):
        data = request.get_json()
        dto = ProductoRequestDto()
        try:
            dataValidada = dto.load(data)

            nuevoProducto = ProductoModel(**dataValidada)

            conexion.session.add(nuevoProducto)
            conexion.session.commit()
            dtoRpta = ProductoResponseDto()
            
            return {
                'message': 'Producto creado exitosamente',
                'content': dtoRpta.dump(nuevoProducto)
            }
        
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            },400
      def get(self):
       
            productoEncontrados  = conexion.session.query(ProductoModel).all()
                                                                                 
         
            dto = ProductoResponseDto()
            return {
                'content': dto.dump(productoEncontrados, many=True)}































































