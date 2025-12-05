'''
    Programa CRUD completo
    v0.1 Andres Ruiz
    El objetivo de este programa es construir el CRUD completo contra MySQL
'''
import mysql.connector

servidor = "localhost"
usuario = "miempresa"
contrasena = "miempresa"
base_de_datos = "miempresa"

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena
)

print("##############")
print("Programa CRUD completo")
print("##############")

while True:
    
    print("Selecciona una opción")
    print("1.-Crear nuevo cliente")
    print("2.-Leer clientes existentes")
    print("3.-Actualizar cliente existente")
    print("4.-Eliminar cliente")
    print("5.-Salir del programa")

    opcion = input("Selecciona una de las opciones:")
    print("Has seleccionado la opcion:",opcion)

    if opcion == "1":
        print("Vamos a insertar un nuevo cliente")
        nombre = input("Introduce un nuevo nombre:")
        apellidos = input("Introduce los nuevos apellidos:")
        email = input("Introduce el email:")
        poblacion = input("Introduce la poblacion:")
        fechadenacimiento = input("Introduce la fecha de nacimiento:")
        peticion = "INSERT INTO clientes VALUES (NULL,'"+nombre+"','"+apellidos+"','"+email+"','"+poblacion+"','"+fechadenacimiento+"');"
        cursor = conexion.cursor()
        cursor.execute(peticion)
        conexion.commit()

    elif opcion == "2":
        
        print("vamos a listar los clientes")
        peticion = "SELECT * FROM clientes;"
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
    
    elif opcion == "3":
        print("Vamos a actualizar a un cliente")
         identificador = input("Introduce el id del cliente que vas a actualizar")
         nombre = input("Introduce un nuevo nombre:")
         apellidos = input("Introduce los nuevos apellidos:")
         email = input("Introduce el email:")
         poblacion = input("Introduce la poblacion:")
         fechadenacimiento = input("Introduce la fecha de nacimiento:")
         peticion = """
                UPDATE clientes
                SET
                nombre = '"""+nombre+"""',
                apellidos = '"""+apellidos+"""',
                email = '"""+email+"""',
                poblacion = '"""+poblacion+"""',
                fechadenacimiento = '"""+fechadenacimiento+"""'
                WHERE Identificador = """+identificador+"""
            ;"""
         cursor = conexion.cursor()
         cursor.execute(peticion)
         conexion.commit()
    elif opcion == "4":
        print("Vamos a eliminar a un cliente")
    elif opcion == "5":
        exit()
    else:
        print("Lo que has escogido no es una opción válida")
