class Jugador:                                                                                    #defino una clase
    def _init_(self,nuevonombre,nuevosapellidos,nuevodorsal,nuevoequipo):
        self.id =  nuevoidentificador
        self.nombre = nuevonombre
        self.apellidos = nueoapellidos
        self.equipo = nuevoequipo

class Liga:                                                                                         #defino otra clase
    def _init_(self,nuevonombre,nuevoequipo,):
        self.id = nuevoidentificador
        self.nombre = nuevonombre
        self.equipo = nuevoequipo

jugadores = []                                                                                      #creo una lista vacia donde guardar los jugadores
liga = []                                                                                           #creo una lista vacia donde guardar la liga

print("Programa de consola")                                                                        #imprimo un mensaje de bienvenida
print("v 0.1 por Andres Ruiz")                                                                      #imprimo el autor

while True:                                                                                         #añadimos un bucle infinito
    
    print("###############################")                                                        #añadimos un separador
    print("Selecciona entidad")                                                                     #seleccionamos una entidad
    print("1.-jugadores")
    print("2.-equipo")

    entidad = input("Indica la opcion seleccionada:")                                               #atrapamos una opcion

    print("Selecciona la operacion")                                                                #muestro el menu de operaciones 
    print("1.-Insertar un nuevo jugador")
    print("2.-Listar jugadores")
    print("3.Actualizar jugadores")
    print("4.Eliminar jugadores")

    opcion = input("Selecciona una de estas opercaiones:")                                          #atrapo la operacion que deseo

    if opcion == "1":                                                                               #inseramos un registro
        print("Insertamos un nuevo jugador")                                                        #imprimo el mensaje                                                                                                 
        identificador = input("Introduce el id del nuevo jugador:")                                 #añadimos el id del jugador que queremos añadir
        nombre = input("Introduce el nombre del nuevo jugador:")                                    #añadimos el nombre del jugador que queremos añadir
        apellido = input("Introduce el nuevo apellido del jugador:")                                #añadimos el apellido del jugador que queremos añadir
        dorsal = input("Introduce el nuevo dorsal del jugador:")                                    #añadimos el dorsal del jugador que queremos añadir
        equipo = input("Introduce el nuevo equipo del jugador:")                                    #añadimos el equipo del jugador que queremos añadir
        Jugador = Jugador(identificador, nombre, apellidos, dorsal, equipo)                         #creo una nueva instancia
        jugador.append(jugador)                                                                     #añado la instancia a la lista de clientes
    if opcion == "2":
        print("Listamos los jugadores")
    if opcion == "3":
        print("Insertamos un nuevo jugador")
    if opcion == "4":
        print("Insertamos un nuevo jugador")
