from abc import ABC, abstractmethod
from i_producto_ingrediente import IProductoIngrediente


class Producto(IProductoIngrediente):
    def __init__(self, nombre, ingredientesNecesarios, precioBase, ID, peso):
        espacioCalculado = 0
        for ingrediente, cantidad in ingredientesNecesarios.items():
            pesoIngrediente = ingrediente.espacioAlmacenamiento
            espacioCalculado += cantidad * pesoIngrediente
        espacioAproximado = round(espacioCalculado * 1.1)

        self.nombre = nombre
        self.espacioAlmacenamiento = espacioAproximado
        self.ingredientesNecesarios = ingredientesNecesarios
        self.precio = self.calcularPrecio(precioBase)
        self.ID = ID
        self.peso = peso
        self.diasBodega = 0
        self.asignadoAEnvio = False

    def listarIngredientesNecesarios(self):
        result = ""
        for ingrediente, cantidad in self.ingredientesNecesarios.items():
            result += f"Necesita la cantidad de {cantidad} {ingrediente.getNombre()}.\n"
        return result

    def calcularPrecio(self, precioBase):
        precio = precioBase if precioBase >= 0 else 0
        for ingrediente, cantidad in self.ingredientesNecesarios.items():
            precio += ingrediente.getPrecio() * cantidad
        return precio

    def __str__(self):
        saltoLinea = "\n"
        result = "-" * 50 + saltoLinea
        result += f"Nombre: {self.getNombre()}{saltoLinea}"
        result += f"Espacio almacenamiento: {self.getEspacioAlmacenamiento()}{saltoLinea}"
        result += f"ID: {self.getID()}{saltoLinea}"
        result += "Ingredientes Necesarios: \n"
        ingredientesNecesarios = self.listarIngredientesNecesarios().split(saltoLinea)
        for ingrediente in ingredientesNecesarios:
            result += f"\t{ingrediente}\n"
        result += f"Precio: {self.getPrecio()}{saltoLinea}"
        result += f"Peso: {self.getPeso()}{saltoLinea}"
        result += f"Días en bodega: {self.getDiasBodega()}{saltoLinea}"
        return result

    @abstractmethod
    def listaCaracteristicas(self):
        pass

    def getEspacioAlmacenamiento(self):
        return self.espacioAlmacenamiento

    def setEspacioAlmacenamiento(self, espacioAlmacenamiento):
        self.espacioAlmacenamiento = espacioAlmacenamiento

    def getIngredientesNecesarios(self):
        return self.ingredientesNecesarios

    def setIngredientesNecesarios(self, ingredientesNecesarios):
        self.ingredientesNecesarios = ingredientesNecesarios

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getDiasBodega(self):
        return self.diasBodega

    def setDiasBodega(self, diasBodega):
        self.diasBodega = diasBodega

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def isAsignadoAEnvio(self):
        return self.asignadoAEnvio

    def setAsignadoAEnvio(self, asignadoAEnvio):
        self.asignadoAEnvio = asignadoAEnvio
