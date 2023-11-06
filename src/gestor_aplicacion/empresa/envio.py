class Envio:
    lista_envios_no_asignados = []
    lista_envios_asignados = []

    def __init__(self, codigo_de_envio, productos, caja, bodega):
        peso_total = 0
        self.bodega = bodega
        self.codigo_de_envio = codigo_de_envio
        self.productos = productos
        self.caja = caja
        for producto in productos:
            producto.set_asignado_a_envio(True)  # Todos los productos aquí ya estarán asignados
            self.bodega.productos.remove(producto)  # se eliminan estos productos de la bodega
            # Se le resta uno a la cantidad de este producto
            valor_actual = self.bodega.contabilidad_productos[producto.get_nombre()]
            clave = producto.get_nombre()
            self.bodega.contabilidad_productos[clave] = valor_actual - 1
            # Agregamos venta al historial de ventas
            Caja.agregar_venta(producto, 1)
            caja.ingresar_dinero(producto.get_precio())

        # se suma el dinero del envío a la caja
        for producto in productos:
            peso_total += producto.get_peso()
        self.peso_total = peso_total
        Envio.lista_envios_no_asignados.append(self)
        # Los envíos deben efectuar cambios en la bodega y caja

    # Devuelve aquellos envíos que no han sido asignados, importantes para la funcionalidad 5
    @classmethod
    def envios_por_asignar(cls):
        result = ""
        numeracion = 1

        for envio in cls.lista_envios_no_asignados:
            if not envio.asignado_a_un_camion:
                result += f"{numeracion}. Envío con código {envio.get_codigo_de_envio()}, con un peso de {envio.get_peso_total()}\n"
                numeracion += 1

        return result

    # Añade un producto al envío con sus repercusiones en bodega y en caja
    def anadir_producto(self, producto):
        self.productos.append(producto)
        self.peso_total += producto.get_peso()
        self.caja.ingresar_dinero(producto.get_precio())
        self.bodega.productos.append(producto)
        clave = producto.get_nombre()
        self.bodega.contabilidad_productos[clave] += 1
        Caja.agregar_venta(producto, 1)

    # Elimina un producto al envío con sus repercusiones en bodega y en caja
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            self.peso_total -= producto.get_peso()
            self.caja.restar_dinero(producto.get_precio())
            self.bodega.productos.remove(producto)
            clave = producto.get_nombre()
            self.bodega.contabilidad_productos[clave] -= 1
            Caja.eliminar_venta(producto, 1)

    # Getters y Setters

    def get_codigo_de_envio(self):
        return self.codigo_de_envio

    def get_camion_asignado(self):
        return self.camion_asignado

    def get_productos(self):
        return self.productos

    def get_peso_total(self):
        return self.peso_total

    def get_caja(self):
        return self.caja

    def set_codigo_de_envio(self, codigo_de_envio):
        self.codigo_de_envio = codigo_de_envio

    def set_camion_asignado(self, camion_asignado):
        self.camion_asignado = camion_asignado

    def set_productos(self, productos):
        self.productos = productos

    def set_peso_total(self, peso_total):
        self.peso_total = peso_total

    def set_caja(self, caja):
        self.caja = caja

    def is_asignado_a_un_camion(self):
        return self.asignado_a_un_camion

    def set_asignado_a_un_camion(self, asignado_a_un_camion):
        self.asignado_a_un_camion = asignado_a_un_camion

    @classmethod
    def get_lista_envios(cls):
        return cls.lista_envios_no_asignados

    @classmethod
    def set_lista_envios(cls, lista_envios):
        cls.lista_envios_no_asignados = lista_envios

    @classmethod
    def get_lista_envios_no_asignados(cls):
        return cls.lista_envios_no_asignados

    @classmethod
    def set_lista_envios_no_asignados(cls, lista_envios_no_asignados):
        cls.lista_envios_no_asignados = lista_envios_no_asignados

    @classmethod
    def get_lista_envios_asignados(cls):
        return cls.lista_envios_asignados

    @classmethod
    def set_lista_envios_asignados(cls, lista_envios_asignados):
        cls.lista_envios_asignados = lista_envios_asignados

    def get_bodega(self):
        return self.bodega

    def set_bodega(self, bodega):
        self.bodega = bodega
