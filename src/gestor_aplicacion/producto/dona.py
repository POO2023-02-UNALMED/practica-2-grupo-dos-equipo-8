from Producto import Producto

class Donas(Producto):
    def __init__(self, nombre, espacioAlmacenamiento, ingredientesNecesarios, precioBase, ID, peso, chips, cobertura):
        super().__init__(nombre, ingredientesNecesarios, precioBase, ID, peso)
        self.chips = chips
        self.cobertura = cobertura

    def listaCaracteristicas(self):
        str = super().__str__()
        str += f"Chips: {self.isChips()}\n"
        str += f"Cobertura: {self.getCobertura()}\n"
        str += "-" * 50 + "\n"
        return str

    def isChips(self):
        return self.chips

    def setChips(self, chips):
        self.chips = chips

    def getCobertura(self):
        return self.cobertura

    def setCobertura(self, cobertura):
        self.cobertura = cobertura
