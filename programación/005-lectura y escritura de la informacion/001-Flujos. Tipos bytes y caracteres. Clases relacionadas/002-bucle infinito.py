print("Mi querido diario, v 0.1")
while(True):
fecha = input("1/09/2024")
mensaje = ("Practicas de programación:")
archivo = open("Practiadeprogramación.txt",'a')
archivo.write(fecha+"|"+mensaje+"\n")
archivo.close()
print("Tu registro ha sido guardado")
