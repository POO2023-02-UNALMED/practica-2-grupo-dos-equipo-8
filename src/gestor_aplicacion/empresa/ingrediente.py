##from src.gestor_aplicacion.producto.i_producto_ingrediente import IProductoIngrediente
from gestor_aplicacion.producto.i_producto_ingrediente import IProductoIngrediente


class Ingrediente(IProductoIngrediente):
    ingredientes_disponibles = []

    def __init__(self, nombre, precio_base, identificador=None, espacio_almacenamiento=None):
        self.nombre = nombre
        self.cantidad = 0

        if precio_base is not None:
            self.precio = self.calcular_precio(precio_base)
            self.identificador = identificador
            self.espacio_almacenamiento = espacio_almacenamiento

            if not any(ingrediente.nombre == self.nombre for ingrediente in Ingrediente.ingredientes_disponibles):
                Ingrediente.ingredientes_disponibles.append(self)
        else:
            precios_base = {
                "harina": 2,
                "huevos": 1,
                "azucar": 3,
                "leche": 4
            }
            self.precio = self.calcular_precio(precios_base.get(nombre.lower(), 1))
            self.identificador = [1, 2, 3, 4].index(precios_base.get(nombre.lower(), 5)) + 1
            self.espacio_almacenamiento = [10, 5, 8, 7][self.identificador - 1]

            if not any(ingrediente.nombre == self.nombre for ingrediente in Ingrediente.ingredientes_disponibles):
                Ingrediente.ingredientes_disponibles.append(self)

    @staticmethod
    def obtener_lista_ingredientes():
        resultado = "Lista de ingredientes disponibles:\n\n"
        numeracion = 1

        for ingrediente in Ingrediente.ingredientes_disponibles:
            resultado += f"{numeracion}. {ingrediente.nombre} - precio: ${ingrediente.precio} - Espacio de almacenamiento: {ingrediente.espacio_almacenamiento}\n"
            numeracion += 1

        return resultado

    def calcular_precio(self, precioBase):
        p = precioBase * 1.19
        return round(p)