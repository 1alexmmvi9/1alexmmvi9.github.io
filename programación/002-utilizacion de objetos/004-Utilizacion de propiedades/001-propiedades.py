class Gato:
    def __init__(self):
        self.altura = None
        self.edad = None
        self.peso = None
        self.nombre = None
    def maulla(self,numero):
        cadena = "MIAU"*numero
        print(cadena)
    def estufera(self):
        print("FFFFFFFFFFF")


gato1 = Gato()
print("El nombre del gato1 es",gato1.nombre)
gato1.nombre = "Misifu"
print("El nombre del gato1",gato1.nombre)
