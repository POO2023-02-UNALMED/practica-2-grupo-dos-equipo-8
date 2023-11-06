from Producto import Producto

class Tortas(Producto):
    def __init__(self, nombre, espacioAlmacenamiento, hashMap, precioBase, ID, peso, porciones, cobertura):
        super().__init__(nombre, hashMap, precioBase, ID, peso)
        self.porciones = porciones
        self.cobertura = cobertura

    def listaCaracteristicas(self):
        str = super().__str__()
        str += f"Porciones: {self.getPorciones()}\n"
        str += f"Cobertura: {self.getCobertura()}\n"
        str += "-" * 50 + "\n"
        return str

    def getPorciones(self):
        return self.porciones

    def setPorciones(self, porciones):
        self.porciones = porciones

    def getCobertura(self):
        return self.cobertura

    def setCobertura(self, cobertura):
        self.cobertura = cobertura
