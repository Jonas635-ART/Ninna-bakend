from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from models import *
from controllers import (CategoriasController, 
                         RegistroController, 
                         ProductosController,
                         PedidoController,
                         UsuarioController,
                          LoginController )
from flask_jwt_extended import JWTManager
from bd import conexion
from os import environ
from flask_cors import CORS
from json import load
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=2) #days

JWTManager(app)
CORS(app, origins='*')
api = Api(app)

conexion.init_app(app)

api.add_resource(CategoriasController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(ProductosController, '/productos')
api.add_resource(PedidoController, '/pedidos')
api.add_resource(UsuarioController, '/perfil')
api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)


