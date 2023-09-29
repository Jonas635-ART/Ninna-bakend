from flask_restful import Resource, request
from models import UsuarioModel
from bcrypt import gensalt, hashpw, checkpw
from dtos import UsuarioRequestDTO, UsuarioResponseDTO, LoginRequestDTO
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from bd import conexion


class RegistroController(Resource):
    def post(self):
        try:
            dto = UsuarioRequestDTO()
            dataValidada = dto.load(request.get_json())
            

            salt = gensalt()
            password = dataValidada.get('password')
            #password a bytes
            passwordBybytes = bytes(password, 'utf-8')
            #mezclamos de password con salt y lo convertimos a string
            passwordHasheada = hashpw(passwordBybytes, salt).decode('utf-8')
            #sobrescribe la contraseña conel texto aleatorio
            dataValidada['password'] = passwordHasheada
            #fin 
            nuevoUsuario = UsuarioModel(**dataValidada)
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            dtoResponse = UsuarioResponseDTO()
            return {
                'message': 'Usuario Creado',
                'content': dtoResponse.dump(nuevoUsuario)
            },201
        except Exception as e:
            return {
                'message': 'error al crear',
                'content':e.args
            }, 400


class UsuarioController(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()

        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = identity).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario no existe'
            }, 404
        dto = UsuarioResponseDTO()

        return {
            'content': dto.dump(usuarioEncontrado)
        }

class LoginController(Resource):
    def post(self):
        
        dto = LoginRequestDTO()
        try:
           print(request.get_json())
           dataValidada = dto.load(request.get_json())
           usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(correo = dataValidada.get('correo')).first()
           if not usuarioEncontrado:
               return {
                   'message': 'E usuario no existe'
               }, 400
           password = bytes(usuarioEncontrado.password, 'utf-8')
           passwordEntrante = bytes(dataValidada.get('password'), 'utf-8')
           #valida si es el password
           resultado = checkpw(passwordEntrante, password)

           if resultado == False:
                return {
                    'message': 'Credenciales incorrectas'
                }, 400
           token = create_access_token(identity= usuarioEncontrado.id)
           print(token)
           return {
               'content': token
           }
           #ayuda para crear la token en jwt
            
        
        except Exception as e:
            return {
                'message': 'E usuario no existe',
                'content': e.args
            }, 400
            



























































