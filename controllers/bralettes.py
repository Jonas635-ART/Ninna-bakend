from flask_restful import Resource, request
from config import conexion
from dtos.bralettes_dto import  (
                                BraletteRequestDTO,BraletteResponseDTO)
from models.bralettes import Bralette
# todos los metodos http que utilizamos se definen como metodos de la clase
class BralettesController(Resource):
    #definimos el metodo a usar como, get,post, put, delete, patch
    def get(self):
        resultado=conexion.session.query(Bralette).all()
        print(resultado)

        return {
            'message':'soy el get de ropa',
            'content': {
                'id':resultado['id'],
                'nombre':resultado['nombre']
                }
        }
    def post(self):
        print(request.get_json())
        #registramos un nuevo producto
        try:
            nuevobralette = Bralette()
            nuevobralette.nombre = 'Luisa'

            conexion.session.add(nuevobralette)
            conexion.session.commit()
            return {
                'message':'Producto registrado'
            }

        except Exception as e:
            print(e.args[0])
            conexion.session.rollback()
            return {
                'message':'soy el error',
                'content':e.args[0]
            }


class BraletteController(Resource):
    def get(self, id): #Aqui estamos retornando el id del un producto
        resultado = conexion.session.query(Bralette).filter_by(id=id).first()
        print(resultado)
        if resultado:
            resultado = BraletteResponseDTO().dump(Bralette)
            return {
                'id': id,
                'result': resultado
            }
        else: 
            return {
                'message':'el producto no existe'
            }, 404  
    def put(self, id):
        bralette = conexion.session.query(Bralette).filter_by(id=id).first()
        try:
            if bralette:
                body = request.get_json()
                #validamos la info enviada por el usuario
                data_validada = BraletteRequestDTO().load(body)
                #
                bralette.nombre = data_validada.get('nombre')
                #solo hacemos un commit ya que no estamos agregando nuevos valores
                conexion.session.commit()

                resultado = BraletteResponseDTO().dump(data_validada)
                return {
                    'message':'Producto actualizado',
                    'content': resultado
                } 
            else: 
                return {
                'message':'el dato no existe'}, 404
        except Exception as e:
            return {
                'message':'error al actualizado',
                'content': e.args
            }, 400








































