# Windows: pip install flask
from flask import Flask                     

aplicacion = Flask(__name__)
def inicio():
    contenido = {"resultado":"ok"}
    return contenido

@aplicacion.route('/')

mensaje = {"resultado":"ok"}
print(mensaje)
