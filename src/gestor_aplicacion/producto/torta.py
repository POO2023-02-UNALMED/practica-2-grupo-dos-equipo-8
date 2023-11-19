
from .producto import Producto

class Tortas(Producto):
    def __init__(self, nombre, espacio_almacenamiento, hash_map, precio_base, ID, peso, porciones, cobertura):
        super().__init__(nombre, hash_map, precio_base, ID, peso)
        self.porciones = porciones
        self.cobertura = cobertura

    def lista_caracteristicas(self):
        str = super().__str__()
        str += f"Porciones: {self.get_porciones()}\n"
        str += f"Cobertura: {self.get_cobertura()}\n"
        str += "-" * 50 + "\n"
        return str

    def get_porciones(self):
        return self.porciones

    def set_porciones(self, porciones):
        self.porciones = porciones
        
    def get_espacio_almacenamiento(self):
        return self.espacio_almacenamiento
    
    def set_espacio_almacenamiento(self, espacioAlmacenamiento):
        self.espacio_almacenamiento = espacioAlmacenamiento
        
    
    