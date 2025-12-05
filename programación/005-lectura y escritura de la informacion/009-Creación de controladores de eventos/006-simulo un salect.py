import mysql.connector

connection = mysql.connector.connect(
    host='localhost',   
    user='miempresa',   
    password='miempresa',
    database='miempresa' 
)

cursor = connection.cursor()

print("Programa de gestión de empresa v0.1")
print("por Andrés Ruiz")

print("Selecciona una tabla de la base de datos:")

peticion = "SHOW TABLES;"

cursor.execute(peticion)
filas = cursor.fetchall()
tablas = []
for fila in filas:
    tablas.append(fila[0])
contador = 0
for tabla in tablas:
    print(contador,"-",tabla)
    contador+=1
    opcion = input("Selecciona una opcion:")

print("Vamos a trabajar con la entidad:",tablas[int(opcion)])
peticion = "SELECT * FROM "+tablas[int(opcion)]
print("La petición que voy a tirar contra la base de datos es: "+peticion)
