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

    def cambiar_produccion(self, producto_seleccionado, nueva_cantidad):
        if producto_seleccionado:
            cantidad_vieja = self.produccion_diaria.get(producto_seleccionado)
            self.produccion_diaria[producto_seleccionado] = nueva_cantidad
            self.actualizar_materia_prima(nueva_cantidad, producto_seleccionado)
            self.actualizar_produccion_diaria(producto_seleccionado, nueva_cantidad)
            return True
        else:
            return False

    def imprimirCambiosFabrica(self, cantidad_vieja, cantidadNueva, producto_seleccionado):
        return f"Ha cambiado su nivel de producción de: {cantidad_vieja} a: {cantidadNueva} del producto: {producto_seleccionado}"

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
                    nuevo_producto = Tortas(nombreProducto, 5, ingredientesTorta, 20, "abc123", 3, 6, "chocolate")
                    self.bodega.get_productos().append(nuevo_producto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesTorta)
                elif nombreProducto == "pastelFrito":
                    ingredientesPastelFrito = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 1,
                    }
                    nuevo_producto = PastelesFritos(nombreProducto, 5, ingredientesPastelFrito, 20, "dfg123", 3, False, "tomate")
                    self.bodega.get_productos().append(nuevo_producto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesPastelFrito)
                elif nombreProducto == "galleta":
                    ingredientesGalleta = {
                        Ingrediente("harina", 5, 1234, 10): 1,
                        Ingrediente("azucar", 3, 1234, 5): 3,
                    }
                    nuevo_producto = Galleta(nombreProducto, 5, ingredientesGalleta, 20, "dfg123", 3, False, "vainilla")
                    self.bodega.get_productos().append(nuevo_producto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesGalleta)
                elif nombreProducto == "dona":
                    ingredientesDona = {
                        Ingrediente("harina", 5, 1234, 10): 3,
                        Ingrediente("azucar", 3, 1234, 5): 3,
                    }
                    nuevo_producto = Donas(nombreProducto, 5, ingredientesDona, 20, "dfg123", 3, False, "arquipe")
                    self.bodega.get_productos().append(nuevo_producto)
                    self.bodega.get_contabilidad_productos()[nombreProducto] += 1
                    self.actualizar_contabilidad_ingredientes(ingredientesDona)

    def actualizar_contabilidad_ingredientes(self, ingredientes):
        for ingrediente in ingredientes.keys():
            if ingrediente.nombre in self.bodega.get_contabilidad_ingredientes():
                valor_a_restar = ingredientes[ingrediente]
                valor_actual = self.bodega.get_contabilidad_ingredientes()[ingrediente.nombre]
                self.bodega.get_contabilidad_ingredientes()[ingrediente.nombre] = valor_actual - valor_a_restar

    def obtener_ingredientes_requeridos(self):
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
                    cantidad_existente = ingrediente_actual.get_cantidad()
                    ingrediente_actual.set_cantidad(cantidad_existente - cantidad_total_necesaria)

        self.get_bodega().set_ingredientes(lista_materia_prima_actual)

    def listar_lista_de_produccion(self):
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

    def actualizar_produccion_diaria(self, producto_seleccionado, nueva_cantidad):
        produccion_diariaActual = self.get_produccion_diaria()
        produccion_diariaActual[producto_seleccionado] = nueva_cantidad
        self.set_produccion_diaria(produccion_diariaActual)

    def fabricar_tanda_productos(self, numero_productosFabricados):
        productos_fabricados = {}
        for producto, cantidad in self.get_produccion_diaria().items():
            if cantidad > 0:
                productos_fabricados[producto] = cantidad * numero_productosFabricados
                ingredientes_necesarios = producto.get_ingredientes_necesarios()
                ingrendientes_usados = {}

                for ingrediente, cantidad_necesaria in ingredientes_necesarios.items():
                    cantidad_total_necesaria = cantidad_necesaria * numero_productosFabricados
                    cantidad_actual = ingrediente.get_cantidad()

                    if cantidad_total_necesaria > cantidad_actual:
                        cantidadFaltante = cantidad_total_necesaria - cantidad_actual
                        ingrediente.set_cantidad(0)
                        ingrendientes_usados[ingrediente] = cantidad_necesaria - (cantidadFaltante / cantidad_necesaria)
                    else:
                        ingrediente.set_cantidad(cantidad_actual - cantidad_total_necesaria)
                        ingrendientes_usados[ingrediente] = cantidad_necesaria

                producto.set_dias_bodega(0)
                producto.set_ingredientes_necesarios(ingrendientes_usados)

        return productos_fabricados

    def validar_fabricacion(self, numero_productosFabricados):
        produccion_diaria = self.get_produccion_diaria()
        espacioDisponibleBodega = self.get_espacio_disponible_bodega()
        total_espacio_necesario = 0

        for producto, cantidad in produccion_diaria.items():
            if cantidad > 0:
                espacio_producto = producto.getEspacio()
                total_espacio_necesario += espacio_producto * cantidad * numero_productosFabricados

        return total_espacio_necesario <= espacioDisponibleBodega

    def fabricar_productos(self, numero_productosFabricados):
        if self.validar_fabricacion(numero_productosFabricados):
            productos_fabricados = self.fabricar_tanda_productos(numero_productosFabricados)
            self.get_registro_tandas()[self.codigoTandaActual] = "Exitosa"
            self.get_productos_generados()[self.codigoTandaActual] = productos_fabricados
            self.setCodigoTandaActual(self.codigoTandaActual + 1)
            return True
        else:
            self.get_registro_tandas()[self.codigoTandaActual] = "Fallida"
            self.get_productos_generados()[self.codigoTandaActual] = {}
            self.setCodigoTandaActual(self.codigoTandaActual + 1)
            return False

    def calcular_ganancias(self, codigo_tanda):
        productos_generados = self.get_productos_generados()
        ganancias = 0

        if codigo_tanda in productos_generados:
            productos_tanda = productos_generados[codigo_tanda]
            for producto, cantidad in productos_tanda.items():
                precio = producto.get_precio()
                ganancias += precio * cantidad

        return ganancias

    def imprimir_produccion_bodega(self):
        productos_en_bodega = self.get_bodega().get_productos()
        cadena = ""
        for producto in productos_en_bodega:
            cadena += f"{producto.get_nombre()} - {len(productos_en_bodega[producto])} - ${producto.get_precio()} - {producto.getDiasBodega()} días en bodega\n"

            for ingrediente, cantidad in producto.getIngredientesUsados().items():
                cadena += f"\t{ingrediente.nombre} - {cantidad}\n"

        return cadena

    def get_produccion_diaria(self):
        return self.produccion_diaria
    
    def set_produccion_diaria(self, produccion_diaria):
        self.produccion_diaria = produccion_diaria

    def get_bodega(self):
        return self.bodega
    
    def set_bodega(self, bodega):
        self.bodega = bodega

    def get_espacio_disponible_bodega(self):
        return self.bodega.get_espacio_almacenamiento()
    
    def set_espacio_disponible_bodega(self, espacio_disponible_bodega):
        self.bodega.set_espacio_almacenamiento(espacio_disponible_bodega)

    def get_registro_tandas(self):
        return self.bodega.get_registro_tandas()
    
    def set_registro_tandas(self, registro_tandas):
        self.bodega.set_registro_tandas(registro_tandas)

    