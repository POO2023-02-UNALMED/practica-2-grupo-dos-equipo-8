class ErrorAplicacion(Exception):
    def __init__(self, err=""):
        super().__init__("Manejo de errores de la Aplicacion\n" + err)