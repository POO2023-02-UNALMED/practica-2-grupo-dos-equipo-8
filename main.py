import sys
# Agregar la ruta del directorio 'src' al principio de sys.path
sys.path.insert(0, './src') 

from gestor_aplicacion.empresa.envio import Envio
from gestor_aplicacion.empresa.ingrediente import Ingrediente

##from gestor_aplicacion.empresa.administrador import *
##from gestor_aplicacion.producto.producto import *

from gestor_aplicacion.empresa.administrador import Administrador
from gestor_aplicacion.producto.producto import Producto


scan = input  # En Python, usamos `input` en lugar de `Scanner` para la entrada del usuario
administrador = Administrador.inicializar()




def imprimir_lista_productos():
    productos = administrador.bodega.productos
    for producto in productos:
        print(str(producto))

def imprimir_separador():
    print("-" * 50)

def compra_materia_prima_ui():
    print("Cantidad de ingredientes en bodega:")
    contabilidad_ingredientes = administrador.bodega.mostrar_contabilidad_ingredientes()
    print(contabilidad_ingredientes)

    print("¿Cree necesario comprar ingredientes? (1.Si / 2.No): ")
    respuesta_comprar_ingredientes = int(scan())
    
    if respuesta_comprar_ingredientes == 1:
        # Mostrar los ingredientes escasos y preguntar si están seguros de que no necesitan comprar.
        ingredientes_escasos = administrador.bodega.mostrar_ingredientes_escasos()
        print(ingredientes_escasos)

        print("Aquí puede ver los ingredientes escasos, ¿Está seguro de que necesita comprar ingredientes? (1.Si / 2.No): ")
        respuesta_ingredientes_escasos = int(scan())

        if respuesta_ingredientes_escasos == 1:
            print("Seleccione el ingrediente que desea pedir:")
            print(Ingrediente.obtener_lista_ingredientes())
            opcion = int(scan())

            if opcion < 1 or opcion > len(Ingrediente.get_ingredientes_disponibles()):
                print("Opción no válida. Seleccione un número válido.")
                return

            # Solicitar la cantidad deseada
            nombre_ingrediente = Ingrediente.get_ingredientes_disponibles()[opcion - 1].nombre
            print(f"¿Cuántos {nombre_ingrediente} desea pedir?")
            cantidad_pedida = int(scan())

            print(administrador.bodega.pedir_cantidad_ingrediente(opcion, cantidad_pedida, administrador))

        else:
            print("Por ahora no se compra nada.")
    elif respuesta_comprar_ingredientes == 2:
        print("Por ahora no se compra nada.")
    else:
        print("Opción no válida.")

def venta_por_encargo_ui():
    # Pedir al usuario que ingrese un código de envío
    print("Ingrese un código de envío (número entero): ")
    codigo_envio = int(scan())

    # Crear una lista para almacenar los productos seleccionados
    productos_seleccionados = []

    # Variable para controlar si el cliente quiere seleccionar más productos
    seleccionar_otro_producto = True

    while seleccionar_otro_producto:
        # Mostrar la lista de productos disponibles
        print(administrador.bodega.mostrar_productos())

        # Pedir al cliente que elija un producto
        print("Elija un producto ingresando el número correspondiente: ")
        opcion_producto = int(scan())

        # Validar si la opción elegida es válida
        if opcion_producto >= 1 and opcion_producto <= len(administrador.bodega.productos):
            producto_elegido = administrador.bodega.productos[opcion_producto - 1]

            # Verificar si el producto ya fue seleccionado previamente
            if producto_elegido in productos_seleccionados:
                print("Ya ha seleccionado ese producto. Por favor, elija otro.")
            else:
                # Agregar el producto a la lista de productos seleccionados
                productos_seleccionados.append(producto_elegido)
                print(f"Has elegido el producto: {producto_elegido.nombre}")

            # Preguntar si desea seleccionar otro producto
            print("¿Desea elegir otro producto? (1.Sí / 2.No): ")
            respuesta = int(scan())
            seleccionar_otro_producto = (respuesta == 1)
        else:
            print("Opción no válida. Seleccione un número válido.")

    # Crear un envío con el código ingresado, la lista de productos seleccionados, la caja y la bodega
    nuevo_envio = Envio(codigo_envio, productos_seleccionados, administrador.caja, administrador.bodega)

    # Mensaje de confirmación
    print(f"Se ha creado un nuevo envío con código {nuevo_envio.codigo_de_envio} y los productos seleccionados.")

def cambiar_lista_produccion_diaria_ui():
    # Pedir al usuario que ingrese una nueva lista de producción diaria
    print("Ingrese una nueva lista de producción diaria (Ejemplo: 2 5 3 4): ")
    nueva_lista_produccion = input().split()
    
    # Validar que la nueva lista tenga la misma cantidad de elementos que la lista actual
    if len(nueva_lista_produccion) != len(administrador.bodega.lista_produccion_diaria):
        print("La nueva lista debe contener la misma cantidad de elementos que la lista actual.")
    else:
        try:
            # Convertir los elementos de la nueva lista a enteros
            nueva_lista_produccion = [int(produccion) for produccion in nueva_lista_produccion]

            # Actualizar la lista de producción diaria
            administrador.bodega.lista_produccion_diaria = nueva_lista_produccion

            print("La lista de producción diaria se ha actualizado correctamente.")
        except ValueError:
            print("Asegúrese de ingresar números enteros separados por espacios.")

# Bucle principal
while True:
    print("Menú de opciones:")
    print("1. Imprimir lista de productos")
    print("2. Compra de materia prima")
    print("3. Venta por encargo")
    print("4. Cambiar lista de producción diaria")
    print("5. Salir")
    print("Seleccione una opción (1/2/3/4/5): ")
    opcion = int(scan())

    if opcion == 1:
        imprimir_lista_productos()
    elif opcion == 2:
        compra_materia_prima_ui()
    elif opcion == 3:
        venta_por_encargo_ui()
    elif opcion == 4:
        cambiar_lista_produccion_diaria_ui()
    elif opcion == 5:
        print("Gracias por usar el sistema. Hasta luego.")
        break
    else:
        print("Opción no válida. Seleccione un número válido.")
