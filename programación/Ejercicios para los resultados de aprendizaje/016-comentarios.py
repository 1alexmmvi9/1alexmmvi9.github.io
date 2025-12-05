'''
    Programa de Biblioteca 
    (c) 2024 Andrés Ruiz Torres
'''

import pickle                                                                                       #Importo una libreria que me permite leer y escribir

class libro:                                                                                        #creo una clase
    def __init__(self,nuevolibro,nuevaeditorial,nuevonumerodeserie,nuevatapa):                      #creo un constructor con parametros     
        self.nombre = nuevolibro                                                                    #A las propiedades les paso los parametros del constructor
        self.editorial = nuevaeditorial
        self.numerodeserie = nuevonumerodeserie
        self.tapa = nuevatapa

agenda = []                                                                                         #creo una ageda vacia 


# Bienvenida #################################################

TITULO = "Programa de Biblioteca"                                                                   #mensaje de bienvenida
AUTOR = "Andrés Ruiz Torres"
print(TITULO,"por",AUTOR)

'''
    Programa de Biblioteca 
    (c) 2024 Andrés Ruiz GTorres
'''

# Bucle infinito ################

while(True):                                                                                        #creo un bucle infinito

    # Menu principal #############################################

    print("Escoge una opción")                                                                      #imprimo un menu principal
    print("1.-Insertar un nuevo libro")
    print("2.-Listar los libros")
    print("3.-Eliminar un libro")
    print("4.-Salir del programa")


    # El usuario escoge una opción ###############################

    opcion = input("Selecciona una opción (1-4):")                                                  #atrapo la opcion del usuario
    print("Has seleccionado la opción:",opcion)                                                     #le indicamos que ha seleccionado dicha opcion

    # Selecciono la operación a realizar #########################

    if opcion == "1":                                                                               #en caso de que el usuario haya seleccionado la opcion 1
        print("Vamos a insertar un nuevo libro")                                                    #le digo que vamos a insertar un nuevo libro

        nombre = input("introduce el nuevo nombre del libro:")                                      #atrapo los datos que me proporciona el usuario
        editorial = input("Introduce la nueva editorial:")
        numerodeserie = input("introduce el nuevo numero de serie:")
        tapa = input("Introduce si la tapa es dura o blanda:")

        nuevolibro = libro(nombre,editorial,numerodeserie,tapa)                                     #creo una instancia de la clase libro

        agenda.append(nuevolibro)                                                                   #la anexo a la agenda

    elif opcion == "2":                                                                             #en caso de que el usuario haya escogido la opcion 2
        for libro in agenda:                                                                        #para cada uno de los libros de la agenda
            print("-----------------------")
            print("nombre:",libro.nombre)                                                           #imprimo cada uno pero en un formato ordenado y bonito
            print("editorial:",libro.editorial)
            print("numerodeserie:",libro.numerodeserie)
            print("tapa:",libro.tapa)
        
    elif opcion == "3":                                                                             #en el caso de que el cliente haya escogido la opcion 3
        print("Vamos a eliminar un libro")                                                          #vamos a eliminar un libro
        opcion = input("que libro quieres eliminar:")
        opcion = int(opcion)
        agenda.pop(opcion)
    elif opcion == "4":                                                                             #en el caso que el usuario haya elegido la opcion 4
        print("Salimos")                                                                            #salimos del programa
        exit()                                                                                      #hemos salido




 
