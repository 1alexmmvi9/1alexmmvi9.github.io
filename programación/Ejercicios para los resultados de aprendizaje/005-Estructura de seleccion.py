'''
    Programa de Biblioteca 
    (c) 2024 Andrés Ruiz GTorres
'''
# Bienvenida #################################################

TITULO = "Programa de Biblioteca"
AUTOR = "Andrés Ruiz Torres"
print(TITULO,"por",AUTOR)

'''
    Programa de Biblioteca 
    (c) 2024 Andrés Ruiz GTorres
'''

# Menu principal #############################################

print("Escoge una opción")
print("1.-Insertar un nuevo libro")
print("2.-Listar los libros")
print("3.-Eliminar un libro")


# El usuario escoge una opción ###############################

opcion = input("Selecciona una opción (1-3):")
print("Has seleccionado la opción:",opcion)

# Selecciono la operación a realizar #########################

if opcion == "1":
    print("Vamos a insertar un nuevo libro")
elif opcion == "2":
    print("Vamos a listar los libros")
elif opcion == "3":
    print("Vamos a eliminar un libro")




 
