from gestor_aplicacion.empresa.caja import Caja
from gestor_aplicacion.empresa.ingrediente import Ingrediente


class Bodega:
    def __init__(self, identificador, contabilidad_productos, espacio_almacenamiento, contabilidad_ingredientes, productos, ingredientes):
        self.identificador = identificador
        self.contabilidad_productos = contabilidad_productos
        self.contabilidad_ingredientes = contabilidad_ingredientes
        self.espacio_almacenamiento = espacio_almacenamiento
        self.productos = productos
        self.ingredientes = ingredientes
        
        for producto in productos:
            self.espacio_almacenamiento -= producto.get_espacio_almacenamiento()
        for ingrediente in ingredientes:
            self.espacio_almacenamiento -= ingrediente.espacio_almacenamiento
    
    def mostrar_contabilidad_ingredientes(self):
        resultado = "Contabilidad de Ingredientes:\n"
        numeracion = 1
        
        for ingrediente, cantidad in self.contabilidad_ingredientes.items():
            resultado += f"{numeracion}. {ingrediente} : {cantidad}\n"
            numeracion += 1
        
        return resultado

    def mostrar_productos(self):
        resultado = ""
        indice = 1
        
        for producto in self.productos:
            resultado += f"{indice}. {producto.get_nombre()} - Precio: ${producto.get_precio()}\n"
            indice += 1
        
        return resultado

    def productos_no_asignados_a_envios(self):
        resultado = ""
        
        for producto in self.productos:
            if not producto.asignado_a_envio:
                resultado += str(producto) + "\n"
        
        return resultado

    def pedir_cantidad_ingrediente(self, opcion, cantidadPedida, administrador):
        try:
            ingredienteSeleccionado = Ingrediente.get_ingredientes_disponibles()[opcion - 1]
            nombreIngrediente, precioIngrediente = ingredienteSeleccionado.get_nombre(), ingredienteSeleccionado.get_precio()

            if nombreIngrediente not in self.contabilidad_ingredientes:
                self.contabilidad_ingredientes[nombreIngrediente] = 0

            for _ in range(cantidadPedida):
                nuevoIngrediente = Ingrediente(nombreIngrediente)
                self.ingredientes.append(nuevoIngrediente)
                self.contabilidad_ingredientes[nombreIngrediente] += 1

            administrador.get_caja().restar_dinero(precioIngrediente * cantidadPedida)
            mensaje = "Se ha realizado el pedido con éxito.\n"
            mensaje += f"Nueva cantidad de {nombreIngrediente}: {self.contabilidad_ingredientes[nombreIngrediente]}"
            return mensaje

        except IndexError:
            return "Opción no válida. Seleccione un ingrediente disponible."
        


    def mostrar_ingredientes_escasos(self):
        resultado = "Ingredientes escasos:\n"

        for ingrediente, cantidad in self.contabilidad_ingredientes.items():
            if cantidad < 10:
                resultado += f"{ingrediente}: {cantidad}\n"

        return resultado

    def stringProductosOrdenadosPorDiasBodega(self):
        productos_ordenados = self.productos_ordenados_por_dias_bodega()
        resultado = "Estancia de Productos en Bodega (Orden por Días en Bodega):\n"
        
        for producto in productos_ordenados:
            tiempo_en_bodega = producto.get_dias_bodega()
            nombre_producto = producto.get_nombre()
            resultado += f"Producto: {nombre_producto}, Tiempo en Bodega: {tiempo_en_bodega} días\n"

        return resultado

    def productos_ordenados_por_dias_bodega(self):
        productos_ordenados = list(self.productos)
        productos_ordenados.sort(key=lambda p: p.get_dias_bodega(), reverse=True)
        return productos_ordenados

    def actualizar_produccion_precio(self, actualizarProduccion=False, actualizarPrecio=False, fabrica=None):
        mensaje = ""
        
        if actualizarProduccion:
            mensaje += self.actualizar_produccion_base_ventas(fabrica) + "\n"

        if actualizarPrecio:
            mensaje += self.actualizar_precio_base_bodega() + "\n"

        return mensaje

    def actualizar_produccion_base_ventas(self, fabrica):
        try:
            productos = Caja.historialVentasOrganizado()
            produccion = fabrica.getProduccionDiaria()
            productoMayorVendido = productos[0]

            for i in range(len(productos)):
                producto = productos[i]
                if i != 0 and produccion.get(producto) is not None:
                    if produccion.get(productoMayorVendido) > produccion.get(producto):
                        produccion[producto] = int(produccion[producto] * 0.85)
                    else:
                        produccion[producto] = int(produccion[producto] * 0.70)
            
            fabrica.set_produccion_diaria(produccion)
            return "Producción actualizada en base a las ventas de los productos."
        
        except Exception:
            return "Ocurrió un error al actualizar la producción."

    def actualizar_precio_base_bodega(self):
        try:
            productos = self.productos_ordenados_por_dias_bodega()

            for producto in productos:
                if producto.get_dias_bodega() >= 5 and producto.get_precio() > 1:
                    producto.setPrecio(int(producto.get_precio() * 0.50))

            return "Se ha actualizado correctamente los precios con respecto a sus días en bodega."
        
        except Exception:
            return "Ha ocurrido un error."

    def guardar_en_bodega(self, tanda):
        for producto, cantidad in tanda.items():
            nombre_producto = producto.get_nombre()
            if nombre_producto in self.contabilidadProductos:
                cantidad_actual = self.contabilidadProductos[nombre_producto]
                self.contabilidadProductos[nombre_producto] = cantidad_actual + cantidad
            else:
                self.contabilidadProductos[nombre_producto] = cantidad

    def verificar_tanda_bodega(self, tanda):
        suma = sum(cantidad for cantidad in tanda.values())
        return suma <= self.espacio_almacenamiento

    def disponibilidad_bodega(self, tanda):
        suma = sum(cantidad for cantidad in tanda.values())
        return suma < self.espacio_almacenamiento / 5

    def descontar_materia_prima_necesaria(self, ingredientesRequeridos, cantidadProduccion):
        mensaje = ""
        try:
            inventarioIngredientes = self.ingredientes

            for ingrediente, cantidadNecesaria in ingredientesRequeridos.items():
                ingredienteEncontrado = False

                for ingredienteEnInventario in inventarioIngredientes:
                    if ingredienteEnInventario.get_nombre() == ingrediente.get_nombre():
                        ingredienteEncontrado = True

                        if ingredienteEnInventario.getCantidad() >= cantidadNecesaria:
                            ingredienteEnInventario.setCantidad(ingredienteEnInventario.getCantidad() - cantidadNecesaria)
                        else:
                            mensaje += f"No hay suficiente cantidad de {ingrediente.get_nombre()} en la bodega."
                        break

                if not ingredienteEncontrado:
                    mensaje += f"El ingrediente {ingrediente.get_nombre()} no está disponible en la bodega."

            self.ingredientes = inventarioIngredientes
            mensaje += "Se ha actualizado el inventario."
        
        except Exception:
            mensaje += "¡Ups! Algo salió mal."
        
        return mensaje

    def get_espacio_almacenamiento(self):
        return self.espacio_almacenamiento
    
    def set_espacio_almacenamiento(self, espacio_almacenamiento):
        self.espacio_almacenamiento = espacio_almacenamiento
        
    def get_contabilidad_ingredientes(self):
        return self.contabilidad_ingredientes
    
    def set_contabilidad_ingredientes(self, contabilidad_ingredientes):
        self.contabilidad_ingredientes = contabilidad_ingredientes
        
    def get_contabilidad_productos(self):
        return self.contabilidad_productos
    
    def set_contabilidad_productos(self, contabilidad_productos):
        self.contabilidad_productos = contabilidad_productos
        
    def get_productos(self):
        return self.productos
    
    def set_productos(self, productos):
        self.productos = productos
        
    def get_ingredientes(self):
        return self.ingredientes
    
    def set_ingredientes(self, ingredientes):
        self.ingredientes = ingredientes
        
    def get_identificador(self):
        return self.identificador
    
    def set_identificador(self, identificador):
        self.identificador = identificador
        
    
