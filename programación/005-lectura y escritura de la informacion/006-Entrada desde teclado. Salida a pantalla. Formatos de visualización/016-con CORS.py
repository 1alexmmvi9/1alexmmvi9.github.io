import mysql.connector
from flask import Flask
from flask_cors import CORS
# pip install flask-cors - pip3 install flask-cors

servidor = "localhost"
usuario = "miempresa"
contrasena = "miempresa"
base_de_datos = "miempresa"

conexion = mysql.conector.connect(
    host=servidor,
    database=base_de_datos,
   user=usuario,  
    password=contrasena
)

@aplicacion.route('/')
def inicio():
    peticion = "SELECT = FROM clientes;"

    cursor = conexion.cursor()

    cursor.execute(peticion)
    filas = cursor.fetchall()
    contenido = []
    for fila in filas:
        print(fila)
    return contenido

aplicacion.run(debug=True)
