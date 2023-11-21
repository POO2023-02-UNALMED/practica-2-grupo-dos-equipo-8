##from src.gestor_aplicacion.producto.i_producto_ingrediente import IProductoIngrediente
from gestor_aplicacion.producto.i_producto_ingrediente import IProductoIngrediente


class Ingrediente(IProductoIngrediente):
    ingredientes_disponibles = []

    def __init__(self, nombre, precio_base=None, identificador=None, espacio_almacenamiento=None):
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
                "leche": 4,
                "mantequila": 5
            }
            self.precio = self.calcular_precio(precios_base.get(nombre.lower(), 1))
            self.identificador = [1, 2, 3, 4,5].index(precios_base.get(nombre.lower(), 5)) + 1
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
    
    def get_nombre(self):
        return self.nombre
    
    def ser_nombre(self, nombre):
        self.nombre = nombre
        
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio
        
    def get_cantidad(self):
        return self.cantidad
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def get_identificador(self):
        return self.identificador
    
    def set_identificador(self, identificador):
        self.identificador = identificador
        
    def get_espacio_almacenamiento(self):
        return self.espacio_almacenamiento
    
    def set_espacio_almacenamiento(self, espacio_almacenamiento):
        self.espacio_almacenamiento = espacio_almacenamiento
        
    def get_ingredientes_disponibles():
        return Ingrediente.ingredientes_disponibles