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
        self.produccionDiaria = {}
        self.bodega = bodega

    def cambiarProduccion(self, productoSeleccionado, nuevaCantidad):
        if productoSeleccionado:
            cantidadVieja = self.produccionDiaria.get(productoSeleccionado)
            self.produccionDiaria[productoSeleccionado] = nuevaCantidad
            self.actualizarMateriaPrima(nuevaCantidad, productoSeleccionado)
            self.actualizarProduccionDiaria(productoSeleccionado, nuevaCantidad)
            return True
        else:
            return False

    def imprimirCambiosFabrica(self, cantidadVieja, cantidadNueva, productoSeleccionado):
        return f"Ha cambiado su nivel de producción de: {cantidadVieja} a: {cantidadNueva} del producto: {productoSeleccionado}"

    def finalizarProduccion(self, produccionDiaria):
        for producto in self.bodega.getProductos():
            producto.setDiasBodega(producto.getDiasBodega() + 1)
        for producto, cantidad in produccionDiaria.items():
            for i in range(cantidad):
                nombreProducto = producto.getNombre()
                if nombreProducto == "torta":
                    ingredientesTorta = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 1,
                    }
                    nuevoProducto = Tortas(nombreProducto, 5, ingredientesTorta, 20, "abc123", 3, 6, "chocolate")
                    self.bodega.getProductos().append(nuevoProducto)
                    self.bodega.getContabilidadProductos()[nombreProducto] += 1
                    self.actualizarContabilidadIngredientes(ingredientesTorta)
                elif nombreProducto == "pastelFrito":
                    ingredientesPastelFrito = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 1,
                    }
                    nuevoProducto = PastelesFritos(nombreProducto, 5, ingredientesPastelFrito, 20, "dfg123", 3, False, "tomate")
                    self.bodega.getProductos().append(nuevoProducto)
                    self.bodega.getContabilidadProductos()[nombreProducto] += 1
                    self.actualizarContabilidadIngredientes(ingredientesPastelFrito)
                elif nombreProducto == "galleta":
                    ingredientesGalleta = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 3,
                    }
                    nuevoProducto = Galleta(nombreProducto, 5, ingredientesGalleta, 20, "dfg123", 3, False, "vainilla")
                    self.bodega.getProductos().append(nuevoProducto)
                    self.bodega.getContabilidadProductos()[nombreProducto] += 1
                    self.actualizarContabilidadIngredientes(ingredientesGalleta)
                elif nombreProducto == "dona":
                    ingredientesDona = {
                        Ingrediente("harina", 5, 1234, 10): 3,
                        Ingrediente("azucar", 3, 1234, 5): 3,
                    }
                    nuevoProducto = Donas(nombreProducto, 5, ingredientesDona, 20, "dfg123", 3, False, "arquipe")
                    self.bodega.getProductos().append(nuevoProducto)
                    self.bodega.getContabilidadProductos()[nombreProducto] += 1
                    self.actualizarContabilidadIngredientes(ingredientesDona)

    def actualizarContabilidadIngredientes(self, ingredientes):
        for ingrediente in ingredientes.keys():
            if ingrediente.nombre in self.bodega.getContabilidadIngredientes():
                valorARestar = ingredientes[ingrediente]
                valorActual = self.bodega.getContabilidadIngredientes()[ingrediente.nombre]
                self.bodega.getContabilidadIngredientes()[ingrediente.nombre] = valorActual - valorARestar

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

    def actualizarMateriaPrima(self, nuevaCantidad, productoSeleccionado):
        listaMateriaPrimaActual = self.getBodega().getIngredientes()
        ingredientesRequeridos = self.obtenerIngredientesRequeridos()

        for ingrediente, cantidadRequerida in ingredientesRequeridos.items():
            cantidadTotalNecesaria = cantidadRequerida * nuevaCantidad

            for ingredienteActual in listaMateriaPrimaActual:
                if ingredienteActual == ingrediente:
                    cantidadExistente = ingredienteActual.getCantidad()
                    ingredienteActual.setCantidad(cantidadExistente - cantidadTotalNecesaria)

        self.getBodega().setIngredientes(listaMateriaPrimaActual)

    def listarListaDeProduccion(self):
        index = 1
        cadena = ""
        for producto, cantidad in self.produccionDiaria.items():
            cadena += f"{index}. {producto.getNombre()}: {cantidad} - ${producto.getPrecio() * cantidad}\n"

            for ingrediente, cantidad_ingrediente in producto.getIngredientesNecesarios().items():
                cadena += f"\t{ingrediente.nombre} - {cantidad_ingrediente * cantidad}\n"

            index += 1
        return cadena

    def productoParaCambiarEnLista(self, numeroProducto):
        index = 1
        productoSeleccionado = None

        for producto in self.produccionDiaria.keys():
            if index == numeroProducto:
                productoSeleccionado = producto
                break
            index += 1
        return productoSeleccionado

    def actualizarProduccionDiaria(self, productoSeleccionado, nuevaCantidad):
        produccionDiariaActual = self.getProduccionDiaria()
        produccionDiariaActual[productoSeleccionado] = nuevaCantidad
        self.setProduccionDiaria(produccionDiariaActual)

    def fabricarTandaProductos(self, numeroProductosFabricados):
        productosFabricados = {}
        for producto, cantidad in self.getProduccionDiaria().items():
            if cantidad > 0:
                productosFabricados[producto] = cantidad * numeroProductosFabricados
                ingredientesNecesarios = producto.getIngredientesNecesarios()
                ingredientesUsados = {}

                for ingrediente, cantidadNecesaria in ingredientesNecesarios.items():
                    cantidadTotalNecesaria = cantidadNecesaria * numeroProductosFabricados
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

    def validarFabricacion(self, numeroProductosFabricados):
        produccionDiaria = self.getProduccionDiaria()
        espacioDisponibleBodega = self.getEspacioDisponibleBodega()
        totalEspacioNecesario = 0

        for producto, cantidad in produccionDiaria.items():
            if cantidad > 0:
                espacioProducto = producto.getEspacio()
                totalEspacioNecesario += espacioProducto * cantidad * numeroProductosFabricados

        return totalEspacioNecesario <= espacioDisponibleBodega

    def fabricarProductos(self, numeroProductosFabricados):
        if self.validarFabricacion(numeroProductosFabricados):
            productosFabricados = self.fabricarTandaProductos(numeroProductosFabricados)
            self.getRegistroTandas()[self.codigoTandaActual] = "Exitosa"
            self.getProductosGenerados()[self.codigoTandaActual] = productosFabricados
            self.setCodigoTandaActual(self.codigoTandaActual + 1)
            return True
        else:
            self.getRegistroTandas()[self.codigoTandaActual] = "Fallida"
            self.getProductosGenerados()[self.codigoTandaActual] = {}
            self.setCodigoTandaActual(self.codigoTandaActual + 1)
            return False

    def calcularGanancias(self, codigoTanda):
        productosGenerados = self.getProductosGenerados()
        ganancias = 0

        if codigoTanda in productosGenerados:
            productosTanda = productosGenerados[codigoTanda]
            for producto, cantidad in productosTanda.items():
                precio = producto.getPrecio()
                ganancias += precio * cantidad

        return ganancias

    def imprimirProduccionBodega(self):
        productosEnBodega = self.getBodega().getProductos()
        cadena = ""
        for producto in productosEnBodega:
            cadena += f"{producto.getNombre()} - {len(productosEnBodega[producto])} - ${producto.getPrecio()} - {producto.getDiasBodega()} días en bodega\n"

            for ingrediente, cantidad in producto.getIngredientesUsados().items():
                cadena += f"\t{ingrediente.nombre} - {cantidad}\n"

        return cadena
