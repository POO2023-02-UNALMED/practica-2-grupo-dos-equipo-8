from gestor_aplicacion.empresa.ingrediente import Ingrediente
from gestor_aplicacion.producto.galleta import Galleta
from gestor_aplicacion.producto.pastel_frito import PastelesFritos
from gestor_aplicacion.producto.torta import Tortas
from gestor_aplicacion.producto.dona import Donas

""" import gestor_aplicacion.empresa.ingrediente
import gestor_aplicacion.producto.galleta
import gestor_aplicacion.producto.pastel_frito
import gestor_aplicacion.producto.torta """

class Fabrica:
    def __init__(self, NIT, direccion, bodega):
        self.NIT = NIT
        self.direccion = direccion
        self.produccion_diaria = {}
        self.bodega = bodega

    def cambiarProduccion(self, producto_seleccionado, nuevaCantidad):
        if producto_seleccionado:
            cantidadVieja = self.produccion_diaria.get(producto_seleccionado)
            self.produccion_diaria[producto_seleccionado] = nuevaCantidad
            self.actualizarMateriaPrima(nuevaCantidad, producto_seleccionado)
            self.actualizar_produccion_diaria(producto_seleccionado, nuevaCantidad)
            return True
        else:
            return False

    def imprimirCambiosFabrica(self, cantidadVieja, cantidadNueva, producto_seleccionado):
        return f"Ha cambiado su nivel de producción de: {cantidadVieja} a: {cantidadNueva} del producto: {producto_seleccionado}"

    def finalizarProduccion(self, produccion_diaria):
        for producto in self.bodega.get_productos():
            producto.set_dias_bodega(producto.get_dias_bodega() + 1)
        for producto, cantidad in produccion_diaria.items():
            for i in range(cantidad):
                nombreProducto = producto.get_nombre()
                if nombreProducto == "torta":
                    ingredientesTorta = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 1,
                    }
                    nuevoProducto = Tortas(nombreProducto, 5, ingredientesTorta, 20, "abc123", 3, 6, "chocolate")
                    self.bodega.get_productos().append(nuevoProducto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesTorta)
                elif nombreProducto == "pastelFrito":
                    ingredientesPastelFrito = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 1,
                    }
                    nuevoProducto = PastelesFritos(nombreProducto, 5, ingredientesPastelFrito, 20, "dfg123", 3, False, "tomate")
                    self.bodega.get_productos().append(nuevoProducto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesPastelFrito)
                elif nombreProducto == "galleta":
                    ingredientesGalleta = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 3,
                    }
                    nuevoProducto = Galleta(nombreProducto, 5, ingredientesGalleta, 20, "dfg123", 3, False, "vainilla")
                    self.bodega.get_productos().append(nuevoProducto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesGalleta)
                elif nombreProducto == "dona":
                    ingredientesDona = {
                        Ingrediente("harina", 5, 1234, 10): 3,
                        Ingrediente("azucar", 3, 1234, 5): 3,
                    }
                    nuevoProducto = Donas(nombreProducto, 5, ingredientesDona, 20, "dfg123", 3, False, "arquipe")
                    self.bodega.get_productos().append(nuevoProducto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesDona)

    def actualizar_contabilidad_ingredientes(self, ingredientes):
        for ingrediente in ingredientes.keys():
            if ingrediente.nombre in self.bodega.get_contabilidad_ingredientes():
                valorARestar = ingredientes[ingrediente]
                valorActual = self.bodega.get_contabilidad_ingredientes()[ingrediente.nombre]
                self.bodega.get_contabilidad_ingredientes()[ingrediente.nombre] = valorActual - valorARestar

    def obtenerIngredientesRequeridos(self):
        ingredientesRequeridos = {}

        """
        Realizar consultas a bases de datos o utilizar estructuras de datos
        predefinidas para mapear los ingredientes requeridos para cada producto

        Ejemplo de lógica:
        if nombreProducto == "Producto1":
            ingredientesRequeridos[Ingrediente("Ingrediente1")] = 5
            ingredientesRequeridos[Ingrediente("Ingrediente2")] = 3
        elif nombreProducto == "Producto2":
            ingredientesRequeridos[Ingrediente("Ingrediente3")] = 4
            ingredientesRequeridos[Ingrediente("Ingrediente4")] = 2
        """
        return ingredientesRequeridos

    def actualizar_materia_prima(self, nueva_cantidad, producto_seleecionado):
        lista_materia_prima_actual = self.get_bodega().get_ingredientes()
        ingredientes_requeridos = self.obtener_ingredientes_requeridos()

        for ingrediente, cantidad_requerida in ingredientes_requeridos.items():
            cantidad_total_necesaria = cantidad_requerida * nueva_cantidad

            for ingrediente_actual in lista_materia_prima_actual:
                if ingrediente_actual == ingrediente:
                    cantidadExistente = ingrediente_actual.getCantidad()
                    ingrediente_actual.setCantidad(cantidad_existente - cantidad_total_necesaria)

        self.getBodega().setIngredientes(lista_materia_prima_actual)

    def listarListaDeProduccion(self):
        index = 1
        cadena = ""
        for producto, cantidad in self.produccion_diaria.items():
            cadena += f"{index}. {producto.get_nombre()}: {cantidad} - ${producto.get_precio() * cantidad}\n"

            for ingrediente, cantidad_ingrediente in producto.get_ingredientes_necesarios().items():
                cadena += f"\t{ingrediente.nombre} - {cantidad_ingrediente * cantidad}\n"

            index += 1
        return cadena

    def producto_para_cambiar_en_lista(self, numero_producto):
        index = 1
        producto_seleccionado = None

        for producto in self.produccion_diaria.keys():
            if index == numero_producto:
                producto_seleccionado = producto
                break
            index += 1
        return producto_seleccionado

    def actualizar_produccion_diaria(self, producto_seleccionado, nuevaCantidad):
        produccion_diariaActual = self.getproduccion_diaria()
        produccion_diariaActual[producto_seleccionado] = nuevaCantidad
        self.setproduccion_diaria(produccion_diariaActual)

    def fabricarTandaProductos(self, numero_productosFabricados):
        productosFabricados = {}
        for producto, cantidad in self.getproduccion_diaria().items():
            if cantidad > 0:
                productosFabricados[producto] = cantidad * numero_productosFabricados
                ingredientesNecesarios = producto.get_ingredientes_necesarios()
                ingredientesUsados = {}

                for ingrediente, cantidadNecesaria in ingredientesNecesarios.items():
                    cantidadTotalNecesaria = cantidadNecesaria * numero_productosFabricados
                    cantidadActual = ingrediente.getCantidad()

                    if cantidadTotalNecesaria > cantidadActual:
                        cantidadFaltante = cantidadTotalNecesaria - cantidadActual
                        ingrediente.setCantidad(0)
                        ingredientesUsados[ingrediente] = cantidadNecesaria - (cantidadFaltante / cantidadNecesaria)
                    else:
                        ingrediente.setCantidad(cantidadActual - cantidadTotalNecesaria)
                        ingredientesUsados[ingrediente] = cantidadNecesaria

                producto.setDiasBodega(0)
                producto.setIngredientesUsados(ingredientesUsados)

        return productosFabricados

    def validarFabricacion(self, numero_productosFabricados):
        produccion_diaria = self.getproduccion_diaria()
        espacioDisponibleBodega = self.getEspacioDisponibleBodega()
        totalEspacioNecesario = 0

        for producto, cantidad in produccion_diaria.items():
            if cantidad > 0:
                espacioProducto = producto.getEspacio()
                totalEspacioNecesario += espacioProducto * cantidad * numero_productosFabricados

        return totalEspacioNecesario <= espacioDisponibleBodega

    def fabricarProductos(self, numero_productosFabricados):
        if self.validarFabricacion(numero_productosFabricados):
            productosFabricados = self.fabricarTandaProductos(numero_productosFabricados)
            self.getRegistroTandas()[self.codigoTandaActual] = "Exitosa"
            self.get_productosGenerados()[self.codigoTandaActual] = productosFabricados
            self.setCodigoTandaActual(self.codigoTandaActual + 1)
            return True
        else:
            self.getRegistroTandas()[self.codigoTandaActual] = "Fallida"
            self.get_productosGenerados()[self.codigoTandaActual] = {}
            self.setCodigoTandaActual(self.codigoTandaActual + 1)
            return False

    def calcularGanancias(self, codigoTanda):
        productosGenerados = self.get_productosGenerados()
        ganancias = 0

        if codigoTanda in productosGenerados:
            productosTanda = productosGenerados[codigoTanda]
            for producto, cantidad in productosTanda.items():
                precio = producto.get_precio()
                ganancias += precio * cantidad

        return ganancias

    def imprimir_produccion_bodega(self):
        productos_en_bodega = self.getBodega().get_productos()
        cadena = ""
        for producto in productos_en_bodega:
            cadena += f"{producto.get_nombre()} - {len(productos_en_bodega[producto])} - ${producto.get_precio()} - {producto.getDiasBodega()} días en bodega\n"

            for ingrediente, cantidad in producto.getIngredientesUsados().items():
                cadena += f"\t{ingrediente.nombre} - {cantidad}\n"

        return cadena
