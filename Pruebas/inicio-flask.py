from flask import Flask
from datetime import datetime

app = Flask(__name__) # __name__ muestra si es el archivo que activa el proyecto, en ese caso sera main, 

@app.route('/api/info')
def info_app():
    return {
        'fecha': datetime.now().strftime('%Y %H:%M: %a, %b, %d ')
    }

@app.route('/')
def inicial():
    print('Hello excuse mee')
    return 'Api 🍕🍗🥤🚲'


#run > incilaixza el servidor
app.run(debug=True) # debug=True significa que debe reiniciar el servidor








































