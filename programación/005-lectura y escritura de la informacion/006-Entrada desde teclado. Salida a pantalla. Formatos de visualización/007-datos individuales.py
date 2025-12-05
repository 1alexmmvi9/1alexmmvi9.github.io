# Windows: pip install mysql-connector-python
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
    #print(fila)
    print("########################")
    print("El identificador es:",fila[0])
    print("El nombre es:",fila[1])
    print("El apellido es:",fila[2])
    print("El email es:",fila[3])
    print("La localidad es:",fila[4])
    print("La fecha de nacimiento es:",fila[5])
