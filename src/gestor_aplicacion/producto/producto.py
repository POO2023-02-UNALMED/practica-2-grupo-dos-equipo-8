from abc import ABC, abstractmethod
from .i_producto_ingrediente import IProductoIngrediente


class Producto:
    def __init__(self, nombre, ingredientes_necesarios, precio_base, ID, peso):
        espacio_calculado = 0
        for ingrediente, cantidad in ingredientes_necesarios.items():
            peso_ingrediente = ingrediente.espacio_almacenamiento
            espacio_calculado += cantidad * peso_ingrediente
        espacio_aproximado = round(espacio_calculado * 1.1)

        self.nombre = nombre
        self.espacio_almacenamiento = espacio_aproximado
        self.ingredientes_necesarios = ingredientes_necesarios
        self.precio = self.calcularPrecio(precio_base)
        self.ID = ID
        self.peso = peso
        self.diasBodega = 0
        self.asignado_a_envio = False

    def listar_ingredientes_necesarios(self):
        result = ""
        for ingrediente, cantidad in self.ingredientes_necesarios.items():
            result += f"Necesita la cantidad de {cantidad} {ingrediente.nombre}.\n"
        return result

    def calcularPrecio(self, precioBase):
        precio = precioBase if precioBase >= 0 else 0
        for ingrediente, cantidad in self.ingredientes_necesarios.items():
            precio += ingrediente.precio * cantidad
        return precio

    def __str__(self):
        salto_linea = "\n"
        result = "-" * 50 + salto_linea
        result += f"Nombre: {self.get_nombre()}{salto_linea}"
        result += f"Espacio almacenamiento: {self.get_espacio_almacenamiento()}{salto_linea}"
        result += f"ID: {self.get_ID()}{salto_linea}"
        result += "Ingredientes Necesarios: \n"
        ingredientesNecesarios = self.listar_ingredientes_necesarios().split(salto_linea)
        for ingrediente in ingredientesNecesarios:
            result += f"\t{ingrediente}\n"
        result += f"Precio: {self.get_precio()}{salto_linea}"
        result += f"Peso: {self.get_peso()}{salto_linea}"
        result += f"Días en bodega: {self.get_dias_bodega()}{salto_linea}"
        return result

    @abstractmethod
    def lista_caracteristicas(self):
        pass

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_espacio_almacenamiento(self):
        return self.espacioAlmacenamiento
    
    def set_espacio_almacenamiento(self, espacioAlmacenamiento):
        self.espacioAlmacenamiento = espacioAlmacenamiento
        
    def get_ingredientes_necesarios(self):
        return self.ingredientes_necesarios
    
    def set_ingredientes_necesarios(self, ingredientesNecesarios):
        self.ingredientes_necesarios = ingredientesNecesarios
        
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio
        
    def get_ID(self):
        return self.ID
    
    def set_ID(self, ID):
        self.ID = ID
        
    def get_peso(self):
        return self.peso
    
    def set_peso(self, peso):
        self.peso = peso
        
    def get_dias_bodega(self):
        return self.diasBodega
    
    def set_dias_bodega(self, diasBodega):
        self.diasBodega = diasBodega
        
    def is_asignado_a_envio(self):
        return self.asignado_a_envio
    
    def set_asignado_a_envio(self, asignado_a_envio):
        self.asignado_a_envio = asignado_a_envio
        
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
        
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
        
    def get_porciones(self):
        return self.porciones
    
    def set_porciones(self, porciones):
        self.porciones = porciones
    
   
        
        