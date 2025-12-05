'''
    Programa agenda
    (c) 2024 Andrés Ruiz Torres
'''
# Bienvenida #####################################################

TITULO = "Programa agenda"
AUTOR = "Andrés Ruiz Torres"
print(TITULO,"por",AUTOR)

#Estructura de control de ejecución infinuita#####################

while(True):

# Menu principal##################################################

    print("Escoge una opción")
    print("1.-Insertar")
    print("2.-Listar")
    print("3.-Actualizar")
    print("4.-Eliminar")

#El usuario de nuestra agenda escoge una opción###################

opción = input("selecciona una opción (1-4):")
print("Has seleccionado la opción:",opción)

#El usuario selecciona la operacion que va a realizar#############

if opción == "1":
    print("Vamos a insertar un nuevo cliente")
elif opción == "2":
    print("Vamos a listar los clientes")
elif opción == "3":
    print("Vamos a actualizar un cliente")
elif opción == "4":
    print("Vamos a eliminar un cliente")
