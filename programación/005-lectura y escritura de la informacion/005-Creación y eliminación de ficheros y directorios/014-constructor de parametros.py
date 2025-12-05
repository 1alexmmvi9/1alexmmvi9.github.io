import pickle

class cliente:
    def _init_(self,nuevonombre,nuevosapellidos,nuevoemail,nuevadirección):
        self.nombre = None
        self.apellidos = None
        self.email = None
        self.dirección = None
        
agenda = []

print("#######################################")
print("Programa agenda v0.1 por Andrés Ruiz")
print("#######################################")

while True:

    print("Menú de navegación")
    print("1.-Introduce un registro")
    print("2.-Listado de registros")
    
    opción = input("Selecciona una opción:")
    print("Has cogido la opción:",opción)

    if opción == "1":
        print("Vamos a insertar un nuevo cliente")
    

        nombre = input("Introduce el nuevo nombre:")
        apellido = input("Introduce los nuevos apellidos:")
        email = input("Introduce el nuevo email:")
        dirección = input("Introduce la nueva dirección:")
    

    elif opción == "2":
        print("Vamos a listar los clientes")

    
