import pickle
from base_datos.deserializador import deserializar
from base_datos.serializador import serializar
from gestor_aplicacion.empresa.caja import Caja
from gestor_aplicacion.empresa.camion import Camion
from gestor_aplicacion.empresa.envio import Envio
from gestor_aplicacion.empresa.fabrica import Fabrica
from gestor_aplicacion.empresa.ingrediente import Ingrediente
from gestor_aplicacion.empresa.bodega import Bodega
from gestor_aplicacion.producto.torta import Tortas
from gestor_aplicacion.producto.pastel_frito import PastelesFritos
from gestor_aplicacion.producto.dona import Donas
from gestor_aplicacion.producto.galleta import Galleta as Galletas
from errores.error_serializacion import ErrorSerializacion

class Administrador:
    def __init__(self, bodega, caja, camiones, fabrica):
        self.bodega = bodega
        self.caja = caja
        self.camiones = camiones
        self.fabrica = fabrica

    @staticmethod
    def finalizarSesion(administrador):
        try:
            # Serializar objetos y guardar en archivos
            serializar('administrador', administrador)
            serializar('bodega', administrador.bodega)
            serializar('envios', Envio.get_lista_envios())
            serializar('ingredientes', Ingrediente.get_ingredientes_disponibles())
            serializar('camiones', Camion.get_camiones())
        except Exception as e:
            print(e)
            raise ErrorSerializacion()

    @staticmethod
    def inicializar():
        try:
            administrador = deserializar("administrador")
            if administrador == None: 
                raise FileNotFoundError()
            Envio.set_lista_envios(deserializar("envios"))
            Ingrediente.set_ingredientes_disponibles(deserializar("ingredientes"))
            Camion.set_camiones(deserializar("camiones"))
            return administrador
        except FileNotFoundError:
            administrador = Administrador.crear_todo()
            return administrador
        except Exception as e:
            raise ErrorSerializacion()

    @staticmethod
    def crear_todo():
        #Listas de productos iniciales
        ingredientes_iniciales_bodega = {}  
        ingredientes_iniciales = []  

        productos_iniciales_bodega = {}  
        productos_iniciales = []  

        productos_iniciales_bodega_1 = {}  
        productos_iniciales = []  

        #-----------------------------------------------------------------------------
        # Crear una torta y agregar ingredientes a la bodega existente
        ingredientes_torta = {}  

        # Crear instancias de los ingredientes
        harina = Ingrediente("harina", 5, 1234, 10)
        azucar = Ingrediente("azucar", 3, 1234, 5)

        # Agregar los ingredientes al diccionario de ingredientes de la torta
        ingredientes_torta[harina] = 1
        ingredientes_torta[azucar] = 1

        # Crear la torta con los ingredientes
        torta = Tortas("torta", 5, ingredientes_torta, 0, "abc123", 3, 6, "chocolate")

        # Agregar la torta a la lista de productos iniciales
        productos_iniciales.append(torta)

        # Agregar la torta al diccionario de productos iniciales en la otra bodega
        productos_iniciales_bodega_1[torta.nombre] = 1
        #-----------------------------------------------------------------------------------------------------------------------

        # Crear un pastel frito y agregar ingredientes a las estructuras existentes

        ingredientes_pasteles_fritos = {}  # Diccionario para los ingredientes del pastel frito

        # Crear instancias de los ingredientes
        harina2 = Ingrediente("harina", 5, 1234, 10)
        azucar2 = Ingrediente("azucar", 3, 1234, 5)

        # Agregar los ingredientes al diccionario de ingredientes de pasteles fritos
        ingredientes_pasteles_fritos[harina2] = 2  # Agrega 2 unidades de harina al pastel frito
        ingredientes_pasteles_fritos[azucar2] = 1  # Agrega 1 unidad de azucar al pastel frito

        # Crear el pastel frito con los ingredientes
        pastel_frito = PastelesFritos("pastelFrito", 5, ingredientes_pasteles_fritos, 20, "dfg123", 3, False, "tomate")

        # Agregar el pastel frito a la lista de productos iniciales
        productos_iniciales.append(pastel_frito)

        # Agregar el pastel frito al diccionario de productos iniciales en la otra bodega
        productos_iniciales_bodega_1[pastel_frito.nombre] = 1

        #------------------------------------------------------------------------------------------------------------------------------------
        # Crear unas galletas y agregar ingredientes a las estructuras existentes

        ingredientes_galletas = {}  # Diccionario para los ingredientes de las galletas

        # Crear instancias de los ingredientes
        harina3 = Ingrediente("harina", 5, 1234, 10)
        azucar3 = Ingrediente("azucar", 3, 1234, 5)

        # Agregar los ingredientes al diccionario de ingredientes de las galletas
        ingredientes_galletas[harina3] = 2  # Agrega 2 unidades de harina a las galletas
        ingredientes_galletas[azucar3] = 1  # Agrega 1 unidad de azucar a las galletas

        # Crear las galletas con los ingredientes
        galletas = Galletas("galleta", 5, ingredientes_galletas, 20, "dfg123", 3, False, "vainilla")

        # Agregar las galletas a la lista de productos iniciales
        productos_iniciales.append(galletas)

        # Agregar las galletas al diccionario de productos iniciales en la otra bodega
        productos_iniciales_bodega_1[galletas.nombre] = 1

        #---------------------------------------------------------------------------------------------------------------------------------
        # Crear una dona y agregar ingredientes a las estructuras existentes

        ingredientes_donas = {}  # Diccionario para los ingredientes de las donas

        # Crear instancias de los ingredientes
        harina4 = Ingrediente("harina", 5, 1234, 10)
        azucar4 = Ingrediente("azucar", 3, 1234, 5)

        # Agregar los ingredientes al diccionario de ingredientes de las donas
        ingredientes_donas[harina4] = 2  # Agrega 2 unidades de harina a las donas
        ingredientes_donas[azucar4] = 1  # Agrega 1 unidad de azucar a las donas

        # Crear la dona con los ingredientes
        dona = Donas("dona", 5, ingredientes_donas, 20, "dfg123", 3, False, "arequipe")

        # Agregar la dona a la lista de productos iniciales
        productos_iniciales.append(dona)

        # Agregar la dona al diccionario de productos iniciales en la otra bodega
        productos_iniciales_bodega_1[dona.nombre] = 1
        #----------------------------------------------------------------------------------------------------------------------------------------
        # Bucle para agregar ingredientes iniciales a la lista existente
        for i in range(1, 11):
            ingrediente1 = Ingrediente("harina", 2, i, 1)
            ingredientes_iniciales.append(ingrediente1)
            ingrediente2 = Ingrediente("azucar", 1, i + 10, 1)
            ingredientes_iniciales.append(ingrediente2)
            ingrediente3 = Ingrediente("huevos", 3, i + 20, 2)
            ingredientes_iniciales.append(ingrediente3)
            ingrediente4 = Ingrediente("levadura", 2, i + 30, 1)
            ingredientes_iniciales.append(ingrediente4)
            ingrediente5 = Ingrediente("mantequilla", 4, i + 40, 2)
            ingredientes_iniciales.append(ingrediente5)
        for ingrediente in ingredientes_iniciales:
            ingredientes_iniciales_bodega[ingrediente.nombre] = 25



        bodega = Bodega("ABC123", productos_iniciales_bodega_1, 1000, ingredientes_iniciales_bodega, productos_iniciales, ingredientes_iniciales)
        fabrica = Fabrica("CBS321", "CRR52#75", bodega)
                # Configurar una producción diaria inicial
        produccion_diaria = {
            torta: 1,
            pastel_frito: 1,
            dona: 1,
            galletas: 1
        }

        # Establecer la producción diaria en la fábrica
        fabrica.produccion_diaria = produccion_diaria

        # Finalizar la producción dos veces
        fabrica.finalizarProduccion(produccion_diaria)
        fabrica.finalizarProduccion(produccion_diaria)
        caja=Caja(10000)

        
        
        marcas = [
            "CamionetaMax", "SuperTruck", "RapidCargo", "MegaHauler", "PowerMover",
            "CargoKing", "TurboTransit", "Speedster", "CargoMaster", "SwiftHaul"
        ]

        modelos = [
            "X1", "A2", "Pro100", "MegaTruck", "UltraCargo",
            "SpeedyXpress", "Transporter3000", "SuperLoad", "CargoBeast", "QuickHauler"
        ]

        placas = [
            "ABC-123", "DEF-456", "GHI-789", "JKL-012", "MNO-345",
            "PQR-678", "STU-901", "VWX-234", "YZA-567", "BCD-890"
        ]

        # Creamos 10 camiones
        camiones = []
        for i in range(10):
            marca = marcas[i]
            modelo = modelos[i]
            capacidad = 1500  # Capacidad ficticia
            placa = placas[i]

            camion = Camion(marca, modelo, capacidad, placa)
            camiones.append(camion)

        # Creamos 5 Envíos
        envios = []
        for i in range(1, 6):
            # Suponiendo que bodega y caja están ya definidos en tu código
            productos_envio = [bodega.productos[0]]  # Agregamos el primer producto de la bodega al envío
            envio = Envio(i, productos_envio, caja, bodega)
            envios.append(envio)
            Envio.lista_envios_no_asignados = envios
        
        
        
        administrador = Administrador(bodega, caja,camiones, fabrica)
        return administrador

    @staticmethod
    def esString(input):
        return input.isalpha()

    @staticmethod
    def asignacionDeCarroDeVenta(bodega):
        try:
            # Mostrar envíos sin camión asignado
            print("Envíos pendientes de asignación de camión:")
            print(Envio.enviosPorAsignar())

            eleccion = int(input("Seleccione el número del envío que desea asignar a un camión: "))
            if 1 <= eleccion <= len(Envio.getListaEnvios()):
                envioAsignar = Envio.getListaEnvios()[eleccion - 1]
                envioAsignar.setAsignadoAUnCamion(True)
                print(Camion.camionesYCapacidad(envioAsignar.getPesoTotal()))

                eleccionCamion = int(input("Seleccione el número del camión que desea asignar: "))
                if 1 <= eleccionCamion <= len(Camion.getCamiones()):
                    camionAsignado = Camion.getCamiones()[eleccionCamion - 1]
                    camionAsignado.agregarEnvio(envioAsignar)
                    envioAsignar.setCamionAsignado(camionAsignado)
                    envioAsignar.setAsignadoAUnCamion(True)
                    camionAsignado.setCapacidad(camionAsignado.getCapacidad() - envioAsignar.getPesoTotal())

                    Envio.getListaEnvios().remove(envioAsignar)
                    Envio.getListaEnviosAsignados().append(envioAsignar)

                    print(f"Envío asignado exitosamente al camión {camionAsignado.getMarca()} {camionAsignado.getModelo()} con placa {camionAsignado.getPlaca()}")

                    print("Productos en bodega no asignados a envíos:")
                    print(bodega.productosNoAsignadosAEnvios())

                    opcionEnvio = int(input("¿Desea enviar el camión? (1. Sí / 2. No): "))
                    if opcionEnvio == 1:
                        camionAsignado.setDisponibilidad(False)
                        Camion.getCamiones().append(camionAsignado)
                        Camion.getCamiones().remove(camionAsignado)
                        camionAsignado.setDisponibilidad(False)
                        print("El camión ha sido enviado.")
                    else:
                        opcionOtroEnvio = int(input("¿Desea realizar otro envío? (1. Sí / 2. No): "))
                        if opcionOtroEnvio == 1:
                            Administrador.asignacionDeCarroDeVenta(bodega)
                        else:
                            print("Hasta luego.")
                else:
                    print("Selección no válida. Por favor, elija un número de camión válido.")
            else:
                print("Selección no válida. Por favor, elija un número de envío válido.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero válido")
            
            
    #Getters y Setters 
    def get_bodega(self):
        return self.bodega
    
    def set_bodega(self, bodega):
        self.bodega = bodega
        
    def get_caja(self):
        return self.caja
    
    def set_caja(self, caja):
        self.caja = caja
    
    def get_camiones(self):
        return self.camiones
    
    def set_camiones(self, camiones):
        self.camiones = camiones
        
    def get_fabrica(self):
        return self.fabrica
    
    def set_fabrica(self, fabrica):
        self.fabrica = fabrica
            
            
