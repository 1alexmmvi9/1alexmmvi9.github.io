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
    print("1.-Añadir bloque")
    option = input("Selecciona una opcion:")


peticion = "SELECT * FROM"+tabla[int(opcion)]
print ("La peticion que voy a tirar contra la base de datos es:"+peticion)


if opcion == "1":
    print("Vamos a insertar un nuevo subtitulo ",tablas[int(opcion)])
    print("Vamos a insertar un nuevo texto",tablas[int(opcion)])
