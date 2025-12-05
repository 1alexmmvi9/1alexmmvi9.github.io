# Windows: pip install flask
from flask import Flask                     

aplicacion = Flask(__name__)
def inicio():
    contenido = '<p>Esta es la página de inicio</p>'
    return contenido

@aplicacion.route('/')

mensaje = {"resultado":"ok"}
print(mensaje)
