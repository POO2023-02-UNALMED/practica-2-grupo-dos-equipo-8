from tkinter import *
from error_aplicacion import ErrorAplicacion

class ErrorCritico(ErrorAplicacion):
    def __init__(self, err=""):
        super().__init__("Detectado Error Critico: " + err)
    def display(self):
        print(self.args[0])
        
try:        
    if(__name__ == "__main__"):
        raise ErrorCritico("Lanzamiento")
except (ErrorCritico) as err:
    err.display()