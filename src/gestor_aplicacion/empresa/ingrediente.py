import sys
sys.path.append('C:/Users/manue/Desktop/Poo/practica-2-grupo-dos-equipo-8/src/gestor_aplicacion')

from producto.i_producto_ingrediente import IProductoIngrediente



class Ingrediente(IProductoIngrediente):

    cantidad = 0

    def __init__(self, nombre, precioBase, identificador, espacioAlmacenamiento):
        self.nombre = nombre
        self.precio = self.calcularPrecio(precioBase)
        self.identificador = identificador
        self.espacioAlmacenamiento = espacioAlmacenamiento

        # Verifica si ingredientesDisponibles es None y, si lo es, inicializa la lista
        if Ingrediente.ingredientesDisponibles is None:
            Ingrediente.ingredientesDisponibles = []

        # Este boolean se usará para saber si un ingrediente se crea dos veces que solo aparezca una vez en la lista
        ingredienteDuplicado = False

        # Itera sobre la lista de ingredientes disponibles para buscar duplicados
        for ingrediente in Ingrediente.ingredientesDisponibles:
            if ingrediente.getNombre() == self.nombre:
                # Ya existe un ingrediente con el mismo nombre
                ingredienteDuplicado = True
                break

        # Si no se encontró un ingrediente duplicado, agrega el nuevo ingrediente
        if not ingredienteDuplicado:
            Ingrediente.ingredientesDisponibles.append(self)

    # Sobrecarga necesaria para hacer el pedido de insumos en bodega
    def __init__(self, nombre):
        self.nombre = nombre

        # Establecer valores predeterminados según el nombre del ingrediente
        if nombre.lower() == "harina":
            self.precio = self.calcularPrecio(2)  # Precio base para harina
            self.identificador = 1  # Identificador para harina
            self.espacioAlmacenamiento = 10  # Espacio de almacenamiento para harina
        elif nombre.lower() == "huevos":
            self.precio = self.calcularPrecio(1)  # Precio base para huevos
            self.identificador = 2  # Identificador para huevos
            self.espacioAlmacenamiento = 5  # Espacio de almacenamiento para huevos
        elif nombre.lower() == "azucar":
            self.precio = self.calcularPrecio(3)  # Precio base para azúcar
            self.identificador = 3  # Identificador para azúcar
            self.espacioAlmacenamiento = 8  # Espacio de almacenamiento para azúcar
        elif nombre.lower() == "leche":
            self.precio = self.calcularPrecio(4)  # Precio base para leche
            self.identificador = 4  # Identificador para leche
            self.espacioAlmacenamiento = 7  # Espacio de almacenamiento para leche
        else:
            # Establecer valores predeterminados genéricos
            self.precio = self.calcularPrecio(1)
            self.identificador = 5
            self.espacioAlmacenamiento = 5

        # Verificar si ingredientesDisponibles es None y, si lo es, inicializar la lista
        if Ingrediente.ingredientesDisponibles is None:
            Ingrediente.ingredientesDisponibles = []

        # Usar un boolean para verificar duplicados
        ingredienteDuplicado = False

        # Iterar sobre la lista de ingredientes disponibles para buscar duplicados
        for ingrediente in Ingrediente.ingredientesDisponibles:
            if ingrediente.getNombre() == self.nombre:
                # Ya existe un ingrediente con el mismo nombre
                ingredienteDuplicado = True
                break

        # Si no se encontró un ingrediente duplicado, agregar el nuevo ingrediente
        if not ingredienteDuplicado:
            Ingrediente.ingredientesDisponibles.append(self)

    # Método que retorna una cadena con la lista de ingredientes disponibles
    @staticmethod
    def obtenerListaIngredientes():
        resultado = "Lista de ingredientes disponibles:\n\n"
        numeracion = 1

        for ingrediente in Ingrediente.ingredientesDisponibles:
            resultado += str(numeracion) + ". " + ingrediente.getNombre() + " - precio: $" + str(ingrediente.getPrecio()) + " - Espacio de almacenamiento: " + str(ingrediente.getEspacioAlmacenamiento()) + "\n"
            numeracion += 1

        return resultado

    # Método que retorna un int con el precio total de un ingrediente con IVA incluido, recibiendo como parámetro un coste base
    def calcularPrecio(self, precioBase):
        p = precioBase
