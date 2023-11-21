from errores.error_advertencia import ErrorAdvertencia

class ErrorTipo(ErrorAdvertencia):
    def __init__(self):
        super().__init__("Se ha ingresado un tipo no valido")
        
if(__name__ == "__main__"):
    try:
        raise ErrorTipo()
    except ErrorAdvertencia as err:
        err.display()