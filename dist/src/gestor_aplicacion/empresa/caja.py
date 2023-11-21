class Caja:
    historial_ventas = {}

    def __init__(self, dinero):
        self.dinero = dinero
        self.costos_produccion = {}

    @classmethod
    def ver_historial_compras(cls):
        result = ""
        for producto, venta in cls.historial_ventas.items():
            result += f"El producto {producto.get_nombre()} ha sido comprado {venta} vez{'.' if venta == 1 else ' veces.'}\n"
        return result

    @classmethod
    def historial_ventas_organizado(cls):
        productos_ordenados = sorted(cls.historial_ventas.keys(), key=lambda p: cls.historial_ventas[p], reverse=True)
        return productos_ordenados

    def ingresar_dinero(self, cantidad):
        self.dinero += cantidad

    def restar_dinero(self, cantidad):
        self.dinero -= cantidad

    @classmethod
    def agregar_venta(cls, producto, cantidad_venta):
        if producto in cls.historial_ventas:
            cls.historial_ventas[producto] += cantidad_venta
        else:
            cls.historial_ventas[producto] = cantidad_venta

    @classmethod
    def eliminar_venta(cls, producto, cantidad_venta):
        if producto in cls.historial_ventas:
            cls.historial_ventas[producto] -= cantidad_venta

    def actualizar_costos_produccion(self, producto, nueva_cantidad):
        nuevo_costo = producto.get_precio() * nueva_cantidad
        for producto_hashmap in self.costos_produccion:
            self.costos_produccion[producto_hashmap] = nuevo_costo

    def descontar_valor_lista(self, costos_produccion):
        dinero_actual = self.dinero
        result = ""

        for producto, costo_produccion in costos_produccion.items():
            if dinero_actual >= producto.get_precio() * costo_produccion:
                dinero_actual -= producto.get_precio() * costo_produccion
                result += f"Se ha descontado {producto.get_precio() * costo_produccion} para el producto {producto.get_nombre()}.\n"
            else:
                result += f"No hay suficiente dinero en la caja para descontar el costo de producción de {producto.get_nombre()}.\n"

        self.dinero = dinero_actual
        result += f"Actualmente cuenta con {self.dinero} en la caja.\n"
        return result

    def get_dinero(self):
        return self.dinero

    def set_dinero(self, dinero):
        self.dinero = dinero

    def get_costos_produccion(self):
        return self.costos_produccion
