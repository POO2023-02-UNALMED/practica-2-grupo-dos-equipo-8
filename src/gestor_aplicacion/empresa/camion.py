class Camion:
    camiones = []

    def __init__(self, marca, modelo, capacidad, placa):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
        self.placa = placa
        self.envios = []
        self.disponibilidad = True
        Camion.camiones.append(self)

    def agregar_envio(self, envio):
        if envio in self.envios or envio.asignado_a_un_camion:
            return
        self.envios.append(envio)
        self.capacidad -= envio.peso_total
        envio.asignado_a_un_camion = True

    def eliminar_envio(self, envio):
        if envio in self.envios:
            self.envios.remove(envio)
            self.capacidad += envio.peso_total
            envio.asignado_a_un_camion = False

    @classmethod
    def camiones_y_capacidad(cls, peso_envio):
        result = ""
        numeracion = 1

        for camion in cls.camiones:
            if camion.capacidad > peso_envio and camion.disponibilidad:
                result += f"{numeracion}. {camion.marca}, {camion.modelo}, {camion.placa}, {camion.capacidad}\n"
                numeracion += 1

        return result

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def get_placa(self):
        return self.placa

    def get_envios(self):
        return self.envios

    def set_envios(self, envios):
        self.envios = envios

    def get_disponibilidad(self):
        return self.disponibilidad

    def set_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad
