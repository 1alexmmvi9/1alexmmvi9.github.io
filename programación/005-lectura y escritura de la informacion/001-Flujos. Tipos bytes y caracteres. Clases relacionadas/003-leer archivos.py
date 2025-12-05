archivo = open("Practiadeprogramación.txt",'a')

lineas = archivo.readlines()

for linea in lineas:
    print(linea)
