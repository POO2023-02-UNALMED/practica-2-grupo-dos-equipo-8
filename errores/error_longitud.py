from error_advertencia import ErrorAdvertencia

class ErrorLongitud(ErrorAdvertencia):
    def __init__(self):
        super().__init__("El campo ingresado no puede ser menor de 3 caracteres")
        
if(__name__ == "__main__"):
    try:
        raise ErrorLongitud()
    except ErrorLongitud as err:
        err.display()