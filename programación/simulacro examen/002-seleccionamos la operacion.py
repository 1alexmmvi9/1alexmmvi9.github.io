class Jugadores:
    def _init_(self,nuevonombre,nuevosapellidos,nuevodorsal,nuevoequipo):
        self.id =  nuevoid
        self.nombre = nuevonombre
        self.apellidos = nueoapellidos
        self.equipo = nuevoequipo

class liga:
    def _init_(self,nuevonombre,nuevoequipo,):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.equipo = nuevoequipo

jugadores = []
liga = []

print("Programa de consola")
print("v 0.1 por Andres Ruiz")

print("Selecciona entidad")
print("1.-jugadores")
print("2.-equipo")

entidad = input("Indica la opcion seleccionada:")

print("Selecciona la operacion")
print("1.-Insertar un nuevo jugador")
print("2.-Listar jugadores")
print("3.Actualizar jugadores")
print("4.Eliminar jugadores")

opcion = input("Selecciona una de estas opercaiones")

if opcion == "1":
    print("Insertamos un nuevo jugador")
if opcion == "2":
    print("Listamos los jugadores")
if opcion == "3":
    print("Insertamos un nuevo jugador")
if opcion == "4":
    print("Insertamos un nuevo jugador")
