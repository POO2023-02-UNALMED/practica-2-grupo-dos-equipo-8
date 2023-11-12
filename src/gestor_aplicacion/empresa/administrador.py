import pickle

from src.gestor_aplicacion.empresa import caja
from src.gestor_aplicacion.empresa.camion import Camion
from src.gestor_aplicacion.empresa.envio import Envio
from src.gestor_aplicacion.empresa.fabrica import Fabrica
from src.gestor_aplicacion.empresa.ingrediente import Ingrediente
from src.gestor_aplicacion.empresa.bodega import Bodega



class Administrador:
    def __init__(self, bodega, caja, camiones, fabrica):
        self.bodega = bodega
        self.caja = caja
        self.camiones = camiones
        self.fabrica = fabrica

    @staticmethod
    def finalizarSesion(administrador):
        # Serializar objetos y guardar en archivos
        with open('administrador.pickle', 'wb') as file:
            pickle.dump(administrador, file)
        with open('bodega.pickle', 'wb') as file:
            pickle.dump(administrador.bodega, file)
        with open('envios.pickle', 'wb') as file:
            pickle.dump(Envio.getListaEnvios(), file)
        with open('ingredientes.pickle', 'wb') as file:
            pickle.dump(Ingrediente.getIngredientesDisponibles(), file)
        with open('camiones.pickle', 'wb') as file:
            pickle.dump(Camion.getCamiones(), file)

    @staticmethod
    def inicializar():
        try:
            with open('administrador.pickle', 'rb') as file:
                administrador = pickle.load(file)
            bodega = administrador.bodega
            Envio.setListaEnvios(Deserializador.deserializarEnvios())
            Ingrediente.setIngredientesDisponibles(Deserializador.deserializarIngredientes())
            Camion.setCamiones(Deserializador.deserializarCamiones())
            return administrador
        except FileNotFoundError:
            administrador = Administrador.crearTodo()
            return administrador

    @staticmethod
    def crearTodo():
        # Creación de objetos y datos iniciales
        # ...

        bodega = Bodega("ABC123", productosInicialesBodega1, 1000, ingredientesInicialeBodega, productosIniciales, ingredientesIniciales)
        fabrica = Fabrica("CBS321", "CRR52#75", bodega)
        # Inicialización de otros objetos y datos
        # ...

        administrador = Administrador(bodega, caja, Camion.getCamiones(), fabrica)
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
