from errores.error_critico import ErrorCritico

class ErrorEjecucion(ErrorCritico):
    def __init__(self, err = "Ha ocurrido un error en la ejecucion"):
        super().__init__(err)
        
if(__name__ == "__main__"):
    try:
        raise ErrorEjecucion()
    except ErrorEjecucion as err:
        err.display()