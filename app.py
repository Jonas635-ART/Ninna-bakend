from flask import Flask 
from datetime import datetime
from flask_restful import Api
from controllers.bralettes import ( BralettesController, 
                                    BraletteController )
from controllers.Descripcion import (DescripcionController,
                                     buscarDescripcionController )
from config import conexion,validador

app = Flask(__name__)
# Creamos la instancia flask_restful y le indicamos que toda la config se agreguea esta instancia
api = Api(app=app)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/ninnary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ->jala la config del flask y extrae su conexion a la base de datos
conexion.init_app(app)
# ->indicamos la creacion de todas las tablas
# ->tenemos que declarar en el parametro app nuestra app
validador.init_app(app)
#conexion.create_all(app=app)

@app.route('/status', methods=['GET'])
def status():
    return{
        'status': True,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        } 
     
@app.route('/')
def inicio():
    return {'hello world'}
# Definiremos las rutas que vamos a utilizar con un controlador
api.add_resource(BralettesController, '/bralettes', '/bralette')
api.add_resource(BraletteController, '/Producto/<int:id>')
api.add_resource(DescripcionController, '/description')
api.add_resource(buscarDescripcionController, '/buscar_Description')

# -> comprueba si la clase flask se ejecuta en el archivo principal del proyecto, esto evita un posible error en el flask

#-> este archivo no es el principal
if __name__ == '__main__':
    app.run(debug=True)

