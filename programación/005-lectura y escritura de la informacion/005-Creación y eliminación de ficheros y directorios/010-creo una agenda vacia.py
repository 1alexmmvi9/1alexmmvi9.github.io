import pickle

class cliente:
    def _init_(self):
        self.nombre = None
        self.apellidos = None
        self.email = None
        self.dirección = None

agenda = []


print("#######################################")
print("Programa agenda v0.1 por Andrés Ruiz")
print("#######################################")

print("Menu de navegación")
print("1.-Introduce un registro")
print("2.-Listado de registros")

opción = input("Selecciona una opción:")
print("Has cogido la opción:",opción)

        
