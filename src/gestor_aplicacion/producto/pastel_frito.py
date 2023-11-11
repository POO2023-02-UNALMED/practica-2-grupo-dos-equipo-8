import sys
sys.path.append('C:/Users/manue/Desktop/Poo/practica-2-grupo-dos-equipo-8/src/gestor_aplicacion')



from producto import Producto


class PastelesFritos(Producto):
    def __init__(self, nombre, espacioAlmacenamiento, ingredientesNecesarios, precioBase, ID, peso, dulce, salsa):
        super().__init__(nombre, ingredientesNecesarios, precioBase, ID, peso)
        self.dulce = dulce
        self.salsa = salsa

    def listaCaracteristicas(self):
        str = super().listaCaracteristicas()
        str += "Dulce: " + ("Si" if self.dulce else "No") + "\n"
        str += "Salsa: " + self.salsa + "\n"
        str += "-" * 50 + "\n"
        return str

    def isDulce(self):
        return self.dulce

    def setDulce(self, dulce):
        self.dulce = dulce

    def getSalsa(self):
        return self.salsa

    def setSalsa(self, salsa):
        self.salsa = salsa
