

from producto import Producto


class Galleta(Producto):
    def __init__(self, nombre, espacioAlmacenamiento, ingredientesNecesarios, precioBase, ID, peso, chips, relleno):
        super().__init__(nombre, ingredientesNecesarios, precioBase, ID, peso)
        self.chips = chips
        self.relleno = relleno

    def listaCaracteristicas(self):
        str = super().toString()
        str += "Chips: " + ("Si" if self.chips else "No") + "\n"
        str += "Relleno: " + self.relleno + "\n"
        str += "-" * 50 + "\n"
        return str

    def isChips(self):
        return self.chips

    def setChips(self, chips):
        self.chips = chips

    def getRelleno(self):
        return self.relleno

    def setRelleno(self, relleno):
        self.relleno = relleno
