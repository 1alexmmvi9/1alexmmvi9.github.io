import mysql.connector

connector = mysql.connector.connect(
        host='localhost',
        user='avisolegal',
        password='avisolegal',
        database='avisolegal',
    )

cursor = connector.cursor() 


print("Examen programacion")
print("v01 creada por Andres Ruiz")

peticion = 'SHOW TABLES'

cursor.execute(peticion)
filas = cursor.fetchall()
tablas = []
for fila in filas:
    tablas.append(filas[0])
contador = 0
for tablas in tablas:
    print(contador,"-",tablas)
    contador+= 1
    option = input("Selecciona una opcion:")
    option = input("1.-Añade un subtitulo: ")
    option = input("1.-Añade un texto: ")

peticion = "SELECT * FROM"+tablas[int(opcion)]
print ("La peticion que voy a tirar contra la base de datos es:"+peticion)

