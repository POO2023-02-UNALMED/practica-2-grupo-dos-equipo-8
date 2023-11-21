from errores.error_critico import ErrorCritico

class ErrorSerializacion(ErrorCritico):
    def __init__(self):
        super().__init__("Ha ocurrido un error en la serializacion de objetos")
        
if(__name__ == "__main__"):
    try:
        raise ErrorSerializacion()
    except ErrorSerializacion as err:
        err.display()