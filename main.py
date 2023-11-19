import sys
# Agregar la ruta del directorio 'src' al principio de sys.path
sys.path.insert(0, './src')

from gestor_aplicacion.empresa.envio import Envio
from gestor_aplicacion.empresa.ingrediente import Ingrediente

##from gestor_aplicacion.empresa.administrador import *
##from gestor_aplicacion.producto.producto import *

from gestor_aplicacion.empresa.administrador import Administrador
from gestor_aplicacion.empresa.camion import Camion
from gestor_aplicacion.empresa.bodega import Bodega
from gestor_aplicacion.empresa.caja import Caja
from gestor_aplicacion.producto.producto import Producto
from gestor_aplicacion.producto.torta import Tortas
from gestor_aplicacion.producto.dona import Donas
from gestor_aplicacion.producto.pastel_frito import PastelesFritos
from gestor_aplicacion.producto.galleta import Galleta


scan = input  # En Python, usamos `input` en lugar de `Scanner` para la entrada del usuario

administrador = Administrador.crear_todo()



def imprimir_lista_productos():
    productos = administrador.bodega.productos
    for producto in productos:
        print(str(producto))

def imprimir_separador():
    print("-" * 50)
#------------------------------------------------------------------------------------------------------------------
#Funcionalidad 1
def compra_materia_prima_ui():
    print("Cantidad de ingredientes en bodega:")
    contabilidad_ingredientes = administrador.bodega.mostrar_contabilidad_ingredientes()
    print(contabilidad_ingredientes)

    print("¿Cree necesario comprar ingredientes? (1.Si / 2.No): ")
    respuesta_comprar_ingredientes = int(scan())
    
    if respuesta_comprar_ingredientes == 1:
        print("Cantidad de ingredientes en bodega:")
        contabilidad_ingredientes = administrador.bodega.mostrar_contabilidad_ingredientes()
        print(contabilidad_ingredientes)
        print("crees necesario comprar ingredientes? (1.Si / 2.No): ")
        respuesta_comprar_ingredientes = int(scan())
        if respuesta_comprar_ingredientes == 1:
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
                nombre_ingrediente = Ingrediente.get_ingredientes_disponibles()[opcion - 1].nombre
                print(f"¿Cuántos {nombre_ingrediente} desea pedir?")
                cantidad_pedida = int(scan())
                print(administrador.bodega.pedir_cantidad_ingrediente(opcion, cantidad_pedida, administrador))
            else:
                print("Por ahora no se compra nada.")
#--------------------------------------------------------------------------------------------------------------------
#Funcionalidad 2
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
#--------------------------------------------------------------------------------------------------------------------
#Funcionalidad 3
def cambiar_lista_produccion_diaria_ui():
    print("Producción diaria actual:")
    print(administrador.get_fabrica().listar_lista_de_produccion())

    print("Ingrese el número correspondiente al producto para cambiar la producción:")
    producto_seleccionado = administrador.get_fabrica().producto_para_cambiar_en_lista(int(input()))
    nueva_cantidad = int(input("Ingrese la nueva cantidad de producción para el producto seleccionado:"))

    if administrador.get_bodega().disponibilidad_bodega(administrador.get_fabrica().get_produccion_diaria()):
        administrador.get_fabrica().cambiar_produccion(producto_seleccionado, nueva_cantidad)
        administrador.get_caja().actualizar_costos_produccion(producto_seleccionado, nueva_cantidad)

        print("Listado de producción diaria actualizada:")
        print(administrador.get_fabrica().listar_lista_de_produccion())

        print("Fabricando tanda...")
        resultado_fabricacion = administrador.get_fabrica().fabricar_tanda_productos(nueva_cantidad)

        if resultado_fabricacion == 1:
            print("No hay suficiente cantidad de ingredientes en bodega.")

        elif resultado_fabricacion == 0:
            print("No hay suficiente espacio en bodega para más productos")
            if administrador.get_fabrica().transferir_produccion_otra_bodega(
                administrador.get_fabrica().get_produccion_diaria()
            ):
                print("Se ha transferido la producción de la tanda a otra bodega")
                print(administrador.get_fabrica().gestionar_espacio_bodega(administrador.get_fabrica().get_produccion_diaria()))
                administrador.get_bodega().guardar_en_bodega(administrador.get_fabrica().get_produccion_diaria())
                numero_tanda = Fabrica.get_codigo_tanda_actual()
                print("El codigo de la tanda es " + numero_tanda)
            else:
                print("No hay bodegas disponibles para transferir productos")
        elif resultado_fabricacion == 2:
            print("Tanda creada exitosamente")
            administrador.get_bodega().descontar_materia_prima_necesaria(
                producto_seleccionado.get_ingredientes_necesarios(), nueva_cantidad
            )
            administrador.get_caja().descontar_valor_lista(administrador.get_fabrica().get_produccion_diaria())
            print(administrador.get_fabrica().establecer_tiempo_demora_produccion(nueva_cantidad))
            print(administrador.get_fabrica().gestionar_espacio_bodega(administrador.get_fabrica().get_produccion_diaria()))
            administrador.get_bodega().guardar_en_bodega(administrador.get_fabrica().get_produccion_diaria())
            numero_tanda = Fabrica.get_codigo_tanda_actual()
            print("El codigo de la tanda es " + numero_tanda)
    else:
        print("La nueva lista de Producción Diaria es demasiado grande para la capacidad de la Bodega. Por favor, elija valores menores y tenga en cuenta el espacio que ocupa cada tipo de producto.")

 #----------------------------------------------------------------------------------------------------------------------------           
#FUNCIONALIDAD 4            
def agregar_producto_ui():
    def imprimir_separador():
        print("-" * 50)
    
    
    
    lista_ingredientes = Ingrediente.obtener_lista_ingredientes()
    print(lista_ingredientes)
    imprimir_separador()
    respuesta = int(input("Tu producto va a necesitar un ingrediente que no esté en la lista? (1.Si / 2.No): "))
    
    while respuesta == 1:
        nombre = input("Ingresa el nombre del nuevo Ingrediente: ")
        precio = int(input("Ingresa el precio del nuevo Ingrediente: "))
        identificador = int(input("Ingresa el identificador del nuevo Ingrediente: "))
        espacio = int(input("Ingresa el espacio de almacenamiento del nuevo Ingrediente: "))
        
        nuevo = Ingrediente(nombre, precio, identificador, espacio)
        temporal = administrador.bodega.ingredientes[:]
        temporal.append(nuevo)
        
        bodega_temporal = administrador.bodega
        bodega_temporal.ingredientes = temporal
        
        administrador.bodega = bodega_temporal
        
        respuesta = int(input("Quieres crear otro ingrediente? (1.Si / 2.No): "))
    
    imprimir_separador()
    print("Se han agregado los nuevos ingredientes")
    imprimir_separador()
    
    lista_ingredientes = Ingrediente.obtener_lista_ingredientes()
    print(lista_ingredientes)
    
    ingredientes_y_cantidad = {}
    seleccionar_otro_ingrediente = True
    
    while seleccionar_otro_ingrediente:
        opcion_ingrediente = int(input("Seleccione el número correspondiente al ingrediente que necesita para su producto: "))
        imprimir_separador()
        
        if 1 <= opcion_ingrediente <= len(Ingrediente.ingredientes_disponibles):
            ingrediente_elegido = Ingrediente.ingredientes_disponibles[opcion_ingrediente - 1]
            
            cantidad_ingrediente = int(input(f"Ingrese la cantidad de {ingrediente_elegido.nombre} que necesita: "))
            ingredientes_y_cantidad[ingrediente_elegido] = cantidad_ingrediente
            
            respuesta1 = int(input("¿Desea seleccionar otro ingrediente? (1.Sí / 2.No): "))
            
            if respuesta1 != 1:
                if len(ingredientes_y_cantidad) < 2:
                    imprimir_separador()
                    print("Se requieren mínimo dos ingredientes para la creación de un producto")
                    imprimir_separador()
                else:
                    seleccionar_otro_ingrediente = False
        else:
            print("Opción no válida. Seleccione un número válido.")
    
    print("Seleccione el tipo de producto que desea crear:")
    print("1. Torta")
    print("2. Dona")
    print("3. Pasteles Fritos")
    print("4. Galleta")
    
    tipo_producto = int(input())
    
    producto_creado = None
    
    if tipo_producto == 1:
        producto_creado = Tortas("torta", 5, ingredientes_y_cantidad, 0, "abc123", 3, 6, "chocolate")
        print(f"Producto exitosamente creado: {producto_creado}")
        temp1 = administrador.bodega.productos[:]
        temp1.append(producto_creado)
        bodegatemporal1 = administrador.bodega
        bodegatemporal1.productos = temp1
        administrador.bodega = bodegatemporal1
    elif tipo_producto == 2:
        producto_creado = Donas("dona", 5, ingredientes_y_cantidad, 20, "dfg123", 3, False, "arquipe")
        print(f"Producto exitosamente creado: {producto_creado}")
        temp2 = administrador.bodega.productos[:]
        temp2.append(producto_creado)
        bodegatemporal2 = administrador.bodega
        bodegatemporal2.productos = temp2
        administrador.bodega = bodegatemporal2
    elif tipo_producto == 3:
        producto_creado = PastelesFritos("pastelFrito", 5, ingredientes_y_cantidad, 20, "dfg123", 3, False, "tomate")
        print(f"Producto exitosamente creado: {producto_creado}")
        temp3 = administrador.bodega.productos[:]
        temp3.append(producto_creado)
        bodegatemporal3 = administrador.bodega
        bodegatemporal3.productos = temp3
        administrador.bodega = bodegatemporal3
    elif tipo_producto == 4:
        producto_creado = Galletas("galleta", 5, ingredientes_y_cantidad, 20, "dfg123", 3, False, "vainilla")
        print(f"Producto exitosamente creado: {producto_creado}")
        temp4 = administrador.bodega.productos[:]
        temp4.append(producto_creado)
        bodegatemporal4 = administrador.bodega
        bodegatemporal4.productos = temp4
        administrador.bodega = bodegatemporal4
    else:
        print("Opción no válida.")
        print(f"Producto exitosamente creado: {producto_creado}")
#--------------------------------------------------------------------------------------------------------------------
#Funcionalidad 5
def eliminar_producto_ui():
    print("Actualmente se ofrecen los siguientes productos: ")
    imprimir_lista_productos()
    nombre_producto_eliminar = input("Por favor, escriba el nombre del producto que desea eliminar: ")

    productos = administrador.bodega.productos[:]
    producto_a_eliminar = None
    indice_a_eliminar = -1

    for i, producto in enumerate(productos):
        if producto.nombre.lower() == nombre_producto_eliminar.lower():
            producto_a_eliminar = producto
            indice_a_eliminar = i
            break

    if producto_a_eliminar is not None:
        confirmacion = int(input(f"¿Seguro que desea eliminar el producto '{producto_a_eliminar.nombre}'? (1.Sí / 2.No): "))
        
        if confirmacion == 1:
            productos.pop(indice_a_eliminar)
            print("El producto ha sido eliminado con éxito.")

            bodega_temporal2 = administrador.bodega
            bodega_temporal2.productos = productos

            administrador.bodega = bodega_temporal2
        else:
            print("No se ha eliminado ningún producto.")
    else:
        print("El producto ingresado no se encontró en la lista de productos.")
#--------------------------------------------------------------------------------------------------------------------
#Funcionalidad 6
def asignar_envio_camion_ui():
    try:
        # Mostrar los envíos sin camión asignado
        print("Envíos pendientes de asignación de camión:")
        print(Envio.envios_por_asignar())

        # Preguntar al usuario cuál envío desea asignar
        print("Seleccione el número del envío que desea asignar a un camión: ")
        eleccion = int(input())
        
        if 1 <= eleccion <= len(Envio.lista_envios_no_asignados):
            # El usuario ha seleccionado un envío válido
            envio_asignar = Envio.lista_envios_no_asignados[eleccion - 1]
            envio_asignar.asignado_a_un_camion = True
            print(Camion.camiones_y_capacidad(envio_asignar.peso_total))

            # Preguntar al usuario cuál camión desea usar
            print("Seleccione el número del camión que desea asignar: ")
            eleccion_camion = int(input())
            
            if 1 <= eleccion_camion <= len(Camion.camiones):
                # El usuario ha seleccionado un camión válido
                camion_asignado = Camion.camiones[eleccion_camion - 1]

                # Asignar el camión al envío
                camion_asignado.agregar_envio(envio_asignar)
                envio_asignar.camion_asignado = camion_asignado
                envio_asignar.asignado_a_un_camion = True
                camion_asignado.capacidad -= envio_asignar.peso_total

                Envio.lista_envios_no_asignados.remove(envio_asignar)
                Envio.lista_envios_asignados.append(envio_asignar)

                print(f"Envío asignado exitosamente al camión {camion_asignado.marca} {camion_asignado.modelo} con placa {camion_asignado.placa}")

                # Mostrar productos en bodega no asignados
                print("Productos en bodega no asignados a envíos:")
                print(administrador.bodega.productos_no_asignados_a_envios())

                # Preguntar al usuario si quiere enviar el camión
                print("¿Desea enviar el camión? (1. Sí / 2. No): ")
                opcion_envio = int(input())
                
                if opcion_envio == 1:
                    # Cambiar estado de disponibilidad del camión
                    camion_asignado.disponibilidad = False
                    Camion.camiones.append(camion_asignado)
                    Camion.camiones.remove(camion_asignado)
                    camion_asignado.disponibilidad = False
                    print("El camión ha sido enviado.")
                else:
                    # Preguntar si quiere realizar otro envío
                    print("¿Desea realizar otro envío? (1. Sí / 2. No): ")
                    opcion_otro_envio = int(input())
                    
                    if opcion_otro_envio == 1:
                        asignar_envio_camion_ui()  # Volver a ejecutar la función
                    else:
                        print("Hasta luego.")
            else:
                print("Selección no válida. Por favor, elija un número de camión válido.")
        else:
            print("Selección no válida. Por favor, elija un número de envío válido.")

    except ValueError:
        print("Entrada no válida. Ingrese un número entero válido.")

def cambiar_produccion_ventas_ui():
    print("Descripcion: Cambia automaticamente el nivel de produccion en base a las ventas de un producto y/o el precio de un producto en base a los dias que lleva en bodega")
    print("¿Esta de acuerdo? 1. Si / 2. No")
    opcion = int(input())

    if opcion == 1:
        print("Desea cambiar la produccion de los productos?:")
        cambio_produccion = input().lower() == "si"

        print("Desea cambiar el precio de los productos?:")
        cambio_precio = input().lower() == "si"

        print(administrador.bodega.actualizar_produccion_precio(cambio_produccion, cambio_precio, administrador.fabrica))

        print("Tabla de productos con precios actualizados")
        imprimir_lista_productos()
    elif opcion == 2:
        print("No se ha realizado ningun cambio.")
    else:
        print("No seleccionaste ninguna opcion.")


# Asegúrate de que la función scan() esté definida
def scan():
    return input()

# Bucle principal
while True:
    print("Menú de opciones:")
    print("1. Compra de materia prima")
    print("2. Venta por encargo")
    print("3. Cambiar lista de producción diaria")
    print("4. Agregar Producto") 
    print("5. Eliminar producto")
    print("6. Asignar Envio y Camion")
    print("7. cambiar producción y/o precio de un producto")
    print("8. Salir")
    print("Seleccione una opción (1/2/3/4/5/6/7/8): ")
    opcion = int(scan())

    if opcion == 1:
        compra_materia_prima_ui()   
    elif opcion == 2:
        venta_por_encargo_ui()
    elif opcion == 3:
        cambiar_lista_produccion_diaria_ui()
    elif opcion == 4:
        agregar_producto_ui()
    elif opcion == 5:
        eliminar_producto_ui()
    elif opcion == 6:
        asignar_envio_camion_ui()
    elif opcion == 7:
        cambiar_produccion_ventas_ui()
    elif opcion == 8:
        print("Hasta luego.")
        break
    

    # Asegúrate de que las funciones para las opciones 5, 6, 7 y 8 estén definidas
    
    
    
    