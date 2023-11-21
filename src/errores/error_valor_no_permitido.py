from errores.error_advertencia import ErrorAdvertencia

class ErrorValorNoPermitido(ErrorAdvertencia):
    def __init__(self):
        super().__init__("Seleccionaste un valor no permitido")
        
if(__name__ == "__main__"):
    try:
        raise ErrorValorNoPermitido()
    except ErrorAdvertencia as err:
        err.display()