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
