import mysql.connector

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

peticion = "SELECT = FROM clientes;"

cursor = conexion.cursor()

cursor.execute(peticion)
filas = cursor.fetchall()

for fila in filas:
    print(fila)

