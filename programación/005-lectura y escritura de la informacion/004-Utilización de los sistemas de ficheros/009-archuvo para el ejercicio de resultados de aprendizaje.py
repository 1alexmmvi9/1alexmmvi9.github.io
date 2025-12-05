import os

try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe, continuamos...")

print("Bienvenidos a Mi Querido Diario de futbol v0.2"
      )
while(True):
    
    print("Selecciona una de las siguiente opciones")
    print("1.-Introducir un nuevo Jugador de futbol")
    print("2.-Leer jugadores existentes")
    opcion = input("Selecciona una de las opciones anteriores:")
    print("La opción que has seleccionado es:",opcion)

    if opcion == "1":
        print("Has elegido introducir un nuevo jugador")
        archivo = open("basededatos/miqueridodiario.txt",'a')
        jugador = input("Introduce el jugador:")
        dorsal = input("Introduce el dorsal:")
        archivo.write(jugador+"|"+dorsal+"\n")
        archivo.close()
    elif opcion == "2":
        print("Has elegido leer los jugadores")
        archivo = open("basededatos/miqueridodiario.txt",'r')
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
    else:
        print("La opcion que has elegido no es valida")
