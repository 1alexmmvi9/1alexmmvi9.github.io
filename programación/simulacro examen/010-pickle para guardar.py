import pickle

class Jugador:                                                                                      #defino una clase
    def _init_(self,nuevoid,nuevonombre,nuevosapellido,nuevodorsal,nuevoequipo):
        self.identificador =  nuevoidentificador
        self.nombre = nuevonombre
        self.apellidos = nuevoapellido
        self.dorsal = nuevodorsal
        self.equipo = nuevoequipo

Jugadores = []                                                                                    #creo una lista vacia donde guardar los jugadores
                                                                                          
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
    print("3.-Actualizar jugadores")
    print("4.-Eliminar jugadores")
    print("5.-Guardar")
    opcion = input("Selecciona una de estas operaciones:")                                          #atrapo la operacion que deseo

    if opcion == "1":                                                                               #inseramos un registro
        print("Insertamos un nuevo jugador")                                                        #imprimo el mensaje                                                                                              
        identificador = input("Introduce el id del nuevo jugador:")                                 #añadimos el id del jugador que queremos añadir
        nombre = input("Introduce el nuevo nombre del jugador:")                                    #añadimos el nombre del jugador que queremos añadir
        apellido = input("Introduce el nuevo apellido del jugador:")                                #añadimos el apellido del jugador que queremos añadir
        dorsal = input("Introduce el nuevo dorsal del jugador:")                                    #añadimos el dorsal del jugador que queremos añadir
        equipo = input("Introduce el nuevo equipo del jugador:")                                    #añadimos el equipo del jugador que queremos añadir                                                                                                             
        Jugadores.append(Jugador(identificador,nombre,apellido,dorsal,equipo))                   #añado la instancia a la lista de clientes
        
    elif opcion == "2":
        print("Listamos los jugadores")
        contador = 0   
        for jugador in jugadores:
            print("----------------------------------------")
            print("Id de Python:"+str(contador))
            print("id"+jugador.identificador)
            print("nombre"+jugador.nombre)
            print("apellidos"+jugador.apellido)
            print("dorsal"+jugador.dorsal)
            print("equipo"+jugador.equipo)
            contador+= 1
    elif opcion == "3":
        print("Actualizamos un nuevo jugador")
        idlista == ("selecciona el elemento de la lista de Python que quieres actualizar: ")
        identificador = input("Introduce el id del jugador modificado:")                                 #añadimos el id del jugador que queremos añadir
        nombre = input("Introduce el nombre del jugador modificado:")                                    #añadimos el nombre del jugador que queremos añadir
        apellido = input("Introduce el nuevo apellido del jugador modificado:")                                #añadimos el apellido del jugador que queremos añadir
        dorsal = input("Introduce el nuevo dorsal del jugador modificado:")                                    #añadimos el dorsal del jugador que queremos añadir
        equipo = input("Introduce el nuevo equipo del jugador modificado :")
        jugadores[int(idlista)].identificador = identificador
        jugadores[int(idlista)].nombre = nombre
        jugadores[int(idlista)].apellidos = apellidos
        jugadores[int(idlista)].dorsal = dorsal
        jugadores[int(idlista)].equipo = equipo
    elif opcion == "4":
        print("Eliminamos un nuevo jugador")
        idlista == ("selecciona el elemento de la lista de Python que quieres eliminar: ")
        jugadores.pop(int(idlista))
    elif opcion == "5":
        archivo = open("jugadores.dat", 'wb')
        pickle.dump(clientes,archivo)
        archivo.close
