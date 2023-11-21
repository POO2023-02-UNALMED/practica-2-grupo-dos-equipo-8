from tkinter import *
from error_aplicacion import ErrorAplicacion

class ErrorAdvertencia(ErrorAplicacion):
    def __init__(self, err=""):
        super().__init__("Nueva Advertencia: " + err)
    def display(self):
        print(self.args[0])
        
try:        
    if(__name__ == "__main__"):
        raise ErrorAdvertencia("Lanzamiento")
except (ErrorAdvertencia) as err:
    err.display()