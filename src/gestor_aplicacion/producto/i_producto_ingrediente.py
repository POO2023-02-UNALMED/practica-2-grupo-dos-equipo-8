from abc import ABC, abstractmethod

class IProductoIngrediente(ABC):
    @abstractmethod
    def calcularPrecio(self, costoBase):
        pass
