'''
    Programa de Biblioteca 
    (c) 2024 Andrés Ruiz Torres
'''

import pickle

class libro:
    def __init__(self,nuevolibro,nuevaeditorial,nuevonumerodeserie,nuevatapa):
        self.nombre = nuevolibro
        self.editorial = nuevaeditorial
        self.numerodeserie = nuevonumerodeserie
        self.tapa = nuevatapa

agenda = []


# Bienvenida #################################################

TITULO = "Programa de Biblioteca"
AUTOR = "Andrés Ruiz Torres"
print(TITULO,"por",AUTOR)

'''
    Programa de Biblioteca 
    (c) 2024 Andrés Ruiz GTorres
'''

# Estructura de control de ejecución infinita ################

while(True):

    # Menu principal #############################################

    print("Escoge una opción")
    print("1.-Insertar un nuevo libro")
    print("2.-Listar los libros")
    print("3.-Eliminar un libro")
    print("4.-Salir del programa")


    # El usuario escoge una opción ###############################

    opcion = input("Selecciona una opción (1-4):")
    print("Has seleccionado la opción:",opcion)

    # Selecciono la operación a realizar #########################

    if opcion == "1":
        print("Vamos a insertar un nuevo libro")

        nombre = input("introduce el nuevo nombre del libro:")
        editorial = input("Introduce la nueva editorial:")
        numerodeserie = input("introduce el nuevo numero de serie:")
        tapa = input("Introduce si la tapa es dura o blanda:")

        nuevolibro = libro(nombre,editorial,numerodeserie,tapa)

        agenda.append(nuevolibro)

    elif opcion == "2":
        print("Vamos a listar los libros")
    elif opcion == "3":
        print("Vamos a eliminar un libro")
    elif opcion == "4":
        print("Salimos")
        exit()




 
