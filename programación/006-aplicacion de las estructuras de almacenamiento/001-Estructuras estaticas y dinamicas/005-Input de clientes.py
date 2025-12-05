clientes = []

clientes.append("Andrés Ruiz")
print(clientes)
clientes.append("Pepe")
print(clientes)

while(True):
    nombre = input("Introduce el nombre de un nuevo cliente:")
    clientes.append(nombre)
    print(clientes)
