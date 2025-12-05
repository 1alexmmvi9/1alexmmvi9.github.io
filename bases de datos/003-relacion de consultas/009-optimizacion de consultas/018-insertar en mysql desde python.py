import mysql.connector                                                      #importo libreria de la base de datos

servidor = "localhost"                                                      # Creo una variable en la que apunto a mi servidor
usuario = "miempresa"                                                       # Creo una variable para definir el usuario
contrasena = "miempresa"                                                    # Creo una variable para definir la contraseña del usuario
base_de_datos = "miempresa"                                                 # Creo una variable para definiar la base de datos a la que me conecto

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)                                                                           #establezco una conexión con la base de datos con los datos seleccionados

print("Creador de clientes v0.1 por Andrés Ruiz")                           #mensaje de bienvenida
nombre = input("Introduce el nombre del cliente:")                          #pregunto nombre del cliente
apellidos = input("Introduce el apellido del cliente:")                     #pregunto apellido del cliente
email = input("Introduce el email del cliente:")                            #pregunto email del cliente
poblacion = input("Introduce la poblacion del cliente:")                    #pregunto poblacion del cliente
nacimiento = input("Introduce la fecha de nacimiento del cliente:")         #pregunto fecha de nacimiento del cliente

peticion ='''
    INSERT INTO clientes
    VALUES (
    NULL,
    "'''+nombre+'''",
    "'''+apellidos+'''",
    "'''+email+'''",
    "'''+poblacion+'''",
    "'''+nacimiento+'''"
    )
'''                                                                         # Preparo una petición,es una insercion de un nuevo cliente

cursor = conexion.cursor()                                                  # Una petición en Python requiere un cursor

cursor.execute(peticion)                                                    # En el cursor, ejecuto la petición que he dejado preparada arriba
conexion.commit()                                                           # Cuando no realizo un select sino que cualquier otro tipo de operacion, tengo que hacer un commit
