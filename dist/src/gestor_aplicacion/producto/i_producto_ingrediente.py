from abc import ABC, abstractmethod

class IProductoIngrediente(ABC):
    @abstractmethod
    def calcular_precio(self, costo_base):
        pass
