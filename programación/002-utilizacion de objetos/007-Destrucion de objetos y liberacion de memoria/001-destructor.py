class Cliente:
    def __init__(self,
                 nuevonombre,
                 nuevosapellidos,
                 nuevoemail,
                 nuevotelefono
                 ):
        self.nombre = nuevonombre
        self.apellidos = nuevosapellidos
        self.email = nuevoemail
        self.telefono = nuevotelefono
    def dameDatos(self):
        print(
            "Nombre:",
            self.nombre,
            " - Apellidos:",
            self.apellidos,
            " - Email:",
            self.email,
            " - Teléfono:",
            self.telefono)

cliente1 = Cliente(
    "Andres",
    "Ruiz",
    "andresruiztorres782@gmail.com",
    601457173
    )
cliente2 = Cliente(
    "Pepe",
    "Garcia",
    "pepegarcia@gmail.com",
    611659845
    )

cliente1.dameDatos()
cliente2.dameDatos()

print(cliente1)
cliente1 = None
print(cliente1)
