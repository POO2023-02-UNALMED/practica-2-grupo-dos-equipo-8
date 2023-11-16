from gestor_aplicacion.empresa.caja import Caja
from gestor_aplicacion.empresa.ingrediente import Ingrediente


class Bodega:
    def __init__(self, identificador, contabilidadProductos, espacioAlmacenamiento, contabilidadIngredientes, productos, ingredientes):
        self.identificador = identificador
        self.contabilidadIngredientes = contabilidadProductos
        self.contabilidadIngredientes = contabilidadIngredientes
        self.espacioAlmacenamiento = espacioAlmacenamiento
        self.productos = productos
        self.ingredientes = ingredientes
        
        for producto in productos:
            self.espacioAlmacenamiento -= producto.getEspacioAlmacenamiento()
        for ingrediente in ingredientes:
            self.espacioAlmacenamiento -= ingrediente.getEspacioAlmacenamiento()
    
    def mostrarContabilidadIngredientes(self):
        resultado = "Contabilidad de Ingredientes:\n"
        numeracion = 1
        
        for ingrediente, cantidad in self.contabilidadIngredientes.items():
            resultado += f"{numeracion}. {ingrediente} : {cantidad}\n"
            numeracion += 1
        
        return resultado

    def mostrarProductos(self):
        resultado = ""
        indice = 1
        
        for producto in self.productos:
            resultado += f"{indice}. {producto.getNombre()} - Precio: ${producto.getPrecio()}\n"
            indice += 1
        
        return resultado

    def productosNoAsignadosAEnvios(self):
        resultado = ""
        
        for producto in self.productos:
            if not producto.isAsignadoAEnvio():
                resultado += str(producto) + "\n"
        
        return resultado

    def pedirCantidadIngrediente(self, opcion, cantidadPedida, administrador):
        try:
            ingredienteSeleccionado = Ingrediente.getIngredientesDisponibles()[opcion - 1]
            nombreIngrediente, precioIngrediente = ingredienteSeleccionado.getNombre(), ingredienteSeleccionado.getPrecio()

            if nombreIngrediente not in self.contabilidadIngredientes:
                self.contabilidadIngredientes[nombreIngrediente] = 0

            for _ in range(cantidadPedida):
                nuevoIngrediente = Ingrediente(nombreIngrediente)
                self.ingredientes.append(nuevoIngrediente)
                self.contabilidadIngredientes[nombreIngrediente] += 1

            administrador.getCaja().restarDinero(precioIngrediente * cantidadPedida)
            mensaje = "Se ha realizado el pedido con éxito.\n"
            mensaje += f"Nueva cantidad de {nombreIngrediente}: {self.contabilidadIngredientes[nombreIngrediente]}"
            return mensaje

        except IndexError:
            return "Opción no válida. Seleccione un ingrediente disponible."
        except Exception as e:
            return f"Ha ocurrido un error: {e}. Inténtelo de nuevo más tarde."


    def mostrarIngredientesEscasos(self):
        resultado = "Ingredientes escasos:\n"

        for ingrediente, cantidad in self.contabilidadIngredientes.items():
            if cantidad < 10:
                resultado += f"{ingrediente}: {cantidad}\n"

        return resultado

    def stringProductosOrdenadosPorDiasBodega(self):
        productosOrdenados = self.productosOrdenadosPorDiasBodega()
        resultado = "Estancia de Productos en Bodega (Orden por Días en Bodega):\n"
        
        for producto in productosOrdenados:
            tiempoEnBodega = producto.getDiasBodega()
            nombreProducto = producto.getNombre()
            resultado += f"Producto: {nombreProducto}, Tiempo en Bodega: {tiempoEnBodega} días\n"

        return resultado

    def productosOrdenadosPorDiasBodega(self):
        productosOrdenados = list(self.productos)
        productosOrdenados.sort(key=lambda p: p.getDiasBodega(), reverse=True)
        return productosOrdenados

    def actualizarProduccionPrecio(self, actualizarProduccion=False, actualizarPrecio=False, fabrica=None):
        mensaje = ""
        
        if actualizarProduccion:
            mensaje += self.actualizarProduccionBaseVentas(fabrica) + "\n"

        if actualizarPrecio:
            mensaje += self.actualizarPrecioBaseDiasBodega() + "\n"

        return mensaje

    def actualizarProduccionBaseVentas(self, fabrica):
        try:
            productos = Caja.historialVentasOrganizado()
            produccion = fabrica.getProduccionDiaria()
            productoMayorVendido = productos[0]

            for i in range(len(productos)):
                producto = productos[i]
                if i != 0 and produccion.get(producto):
                    if produccion.get(productoMayorVendido) > produccion.get(producto):
                        produccion[producto] = int(produccion[producto] * 0.85)
                    else:
                        produccion[producto] = int(produccion[producto] * 0.70)
            
            fabrica.setProduccionDiaria(produccion)
            return "Producción actualizada en base a las ventas de los productos."
        
        except Exception:
            return "Ocurrió un error al actualizar la producción."

    def actualizarPrecioBaseDiasBodega(self):
        try:
            productos = self.productosOrdenadosPorDiasBodega()

            for producto in productos:
                if producto.getDiasBodega() >= 5 and producto.getPrecio() > 1:
                    producto.setPrecio(int(producto.getPrecio() * 0.50))

            return "Se ha actualizado correctamente los precios con respecto a sus días en bodega."
        
        except Exception:
            return "Ha ocurrido un error."

    def guardarEnBodega(self, tanda):
        for producto, cantidad in tanda.items():
            nombreProducto = producto.getNombre()
            if nombreProducto in self.contabilidadProductos:
                cantidadActual = self.contabilidadProductos[nombreProducto]
                self.contabilidadProductos[nombreProducto] = cantidadActual + cantidad
            else:
                self.contabilidadProductos[nombreProducto] = cantidad

    def verificarTandaBodega(self, tanda):
        suma = sum(cantidad for cantidad in tanda.values())
        return suma <= self.espacioAlmacenamiento

    def disponibilidadBodega(self, tanda):
        suma = sum(cantidad for cantidad in tanda.values())
        return suma < self.espacioAlmacenamiento / 5

    def descontarMateriaPrimaNecesaria(self, ingredientesRequeridos, cantidadProduccion):
        mensaje = ""
        try:
            inventarioIngredientes = self.ingredientes

            for ingrediente, cantidadNecesaria in ingredientesRequeridos.items():
                ingredienteEncontrado = False

                for ingredienteEnInventario in inventarioIngredientes:
                    if ingredienteEnInventario.getNombre() == ingrediente.getNombre():
                        ingredienteEncontrado = True

                        if ingredienteEnInventario.getCantidad() >= cantidadNecesaria:
                            ingredienteEnInventario.setCantidad(ingredienteEnInventario.getCantidad() - cantidadNecesaria)
                        else:
                            mensaje += f"No hay suficiente cantidad de {ingrediente.getNombre()} en la bodega."
                        break

                if not ingredienteEncontrado:
                    mensaje += f"El ingrediente {ingrediente.getNombre()} no está disponible en la bodega."

            self.ingredientes = inventarioIngredientes
            mensaje += "Se ha actualizado el inventario."
        
        except Exception:
            mensaje += "¡Ups! Algo salió mal."
        
        return mensaje

    def getIdentificador(self):
        return self.identificador

    def setIdentificador(self, identificador):
        self.identificador = identificador

    def getProductos(self):
        return self.productos

    def setProductos(self, productos):
        self.productos = productos

    def getEspacioAlmacenamiento(self):
        return self.espacioAlmacenamiento

    def setEspacioAlmacenamiento(self, espacioAlmacenamiento):
        self.espacioAlmacenamiento = espacioAlmacenamiento

    def getIngredientes(self):
        return self.ingredientes

    def setIngredientes(self, listaMateriaPrimaActual):
        self.ingredientes = listaMateriaPrimaActual

    def getContabilidadProductos(self):
        return self.contabilidadProductos

    def setContabilidadProductos(self, contabilidadProductos):
        self.contabilidadProductos = contabilidadProductos

    def getContabilidadIngredientes(self):
        return self.contabilidadIngredientes

    def setContabilidadIngredientes(self, contabilidadIngredientes):
        self.contabilidadIngredientes = contabilidadIngredientes
