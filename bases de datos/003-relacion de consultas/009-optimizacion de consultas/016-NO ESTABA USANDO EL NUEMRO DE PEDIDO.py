'''
    Programa generador de tickets de tienda v 0.1
    (c)2024 Andrés Ruiz

    Este software se conecta con una base de datos para sacar un ticket
'''
import mysql.connector                          #importo libreria de la base de datos
print("##################################")     #imprimo un separador visualen el ticket 
print("Factura")
print("##################################")

servidor = "localhost"                          # Creo una variable en la que apunto a mi servidor
usuario = "miempresa"                           # Creo una variable para definir el usuario
contrasena = "miempresa"                        # Creo una variable para definir la contraseña del usuario
base_de_datos = "miempresa"                     # Creo una variable para definiar la base de datos a la que me conecto

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)                                               #establezco una conexión con la base de datos con los datos seleccionados

pedido = "3"                                     #indico un número de pedido -ahora luego esto se va a hacer dinamico

######################################## DATOS DEL CLIENTE ##############################################################

peticion ='''
SELECT
    clientes.nombre,
    clientes.apellidos,
    clientes.email,
    clientes.poblacion
    
    FROM pedidos
    LEFT JOIN clientes
    ON pedidos.clientes_apellidos = clientes.id
    
    WHERE pedidos.id = '''+pedido+'''
'''                                             # Preparo una petición,en este caso pido los datos de clientes

cursor = conexion.cursor()                      # Una petición en Python requiere un cursor

cursor.execute(peticion)                        # En el cursor, ejecuto la petición que he dejado preparada arriba
filas = cursor.fetchall()
print ("")                                      # En una variable llamadas filas, almaceno los resultados que me da la base de datos
print("##################################")
print("Datos del cliente:")
print("##################################")
for fila in filas:
    for dato in fila:
        print (dato)                            # Como filas representa a todas las filas, yo quiero coger una a una
        
######################################## DATOS DEL CLIENTE ##############################################################

######################################## DATOS DEL PEDIDO ##############################################################
        
peticion ='''
SELECT

    pedidos.id,
    pedidos .fecha
    
    FROM pedidos
    LEFT JOIN clientes
    ON pedidos.clientes_apellidos = clientes.id
    
    WHERE pedidos.id = '''+pedido+'''
'''          

cursor = conexion.cursor()                      

cursor.execute(peticion)                       
filas = cursor.fetchall()
print ("")                                      
print("##################################")
print("Datos del pedido:")
print("##################################")
for fila in filas:
    for dato in fila:
        print (dato)
        
######################################## DATOS DEL PEDIDO ##############################################################
        
######################################## LINEAS DEL PEDIDO ##############################################################
        
peticion ='''
SELECT

    productos.nombre, 
    productos.descripcion, 
    productos.precio, 
    lineaspedido.cantidad, 
    productos.precio*lineaspedido.cantidad 
    FROM lineaspedido 
    LEFT JOIN pedidos 
    ON lineaspedido.pedidos_fecha = pedidos.id 
    LEFT JOIN productos 
    ON lineaspedido.productos_nombre = productos.id 
    WHERE pedidos.id = '''+pedido+'''
'''          

cursor = conexion.cursor()                      

cursor.execute(peticion)                       
filas = cursor.fetchall()
print ("")                                      
print("##################################")
print("LINEAS DE PEDIDO:")
print("##################################")
for fila in filas:
    print("-------------------")
    for dato in fila:
        print (dato)
######################################## LINEAS DEL PEDIDO ##############################################################
