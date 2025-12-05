import mysql.connector
print("##################################")
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
)                

pedido = 3
peticion ='''
SELECT
    clientes.nombre,
    clientes.apellidos,
    clientes.email,
    clientes.poblacion
    
    FROM pedidos
    LEFT JOIN clientes
    ON pedidos.clientes_apellidos = clientes.id
    
    WHERE pedidos.id = 3
'''            # Preparo una petición

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

peticion ='''
SELECT

    pedidos.id,
    pedidos .fecha
    
    FROM pedidos
    LEFT JOIN clientes
    ON pedidos.clientes_apellidos = clientes.id
    
    WHERE pedidos.id = 3
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
    WHERE pedidos.id = 3
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

