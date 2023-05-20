from flask import Flask, request
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app=app, origins=[''], methods='*', allow_headers=['Content_type'])

clientes = [
    {
    "nombre": "Fernada",
    "pais": "Ecuador",
    "id": 1,
    "edad": 32
    }
]



def buscar_usuario(id):
  
    for cliente in clientes:
      if cliente.get('id') == id:
            return cliente

@app.route('/')
@cross_origin(origins=['http://127.0.0.1:8080'])
def estado():
    hora = datetime.now()
    return {
        'status': True,
        'hour': hora.strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route("/clientes", methods=['POST', 'GET'])
def obten_clientes():
    # solo request es llamado en cada controlador(funcion que se ejecuta cuando el front hace una peticion)
    print(request.method)
    # request.method > mostrara el tipo de metodo al cual hace la consulta el front
    print(request.get_json())
    # request.get_json() > devuelve la info enviada al body y la convierte en un diccionario para que python lo entienda
    # y manipula
    if request.method == 'POST':
        # ingresa cuando sea POST
        data = request.get_json()
        data['id'] = len(clientes) + 1  # ->esto no sirve para asignar
        clientes.append(data)
        return {
            'message': 'Cliente agregado',
            'client': data
        }

    else:
    # elif request.method == 'GET':
    # ingresa cuando el metodo sea GET
        return {
        'message': 'lista de clientes',
        'clients': clientes
        }


@app.route("/cliente/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def gestion_usuario(id):
    print(id)
    if request.method == 'GET':
        usuario = buscar_usuario(id)
        if usuario:
            return usuario
        else:
            return {
                'message': 'no encontro usuario'
            }, 404
    elif request.method == 'PUT':
        resultado = buscar_usuario(id)
        if resultado is not None:
            [cliente, posicion] = resultado

            data = request.get_json()
            data['id'] = id
            clientes[posicion] = data
            return clientes[posicion]
    elif request.method == 'DELETE':
        resultado = buscar_usuario(id)
        if resultado:
            [usuario, posicion] = resultado
            cliente_eliminado = clientes.pop(posicion)
            return {
                'message':'eliminado',
                'cliente': cliente_eliminado
            }

        else:
            return {
            'message': 'El cliente a modificar no se encontro'
            }, 404



# debug > si esta hablitado (True) se reinicia el srvidor en automatico cada vez que guardamos cambios
# port > indica que puerto usaremos, por defecto el 8080
app.run(debug=True, port=8080)
