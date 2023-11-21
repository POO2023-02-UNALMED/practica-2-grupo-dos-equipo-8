from tkinter import *
from tkinter import messagebox
from errores.error_aplicacion import ErrorAplicacion

class ErrorAdvertencia(ErrorAplicacion):
    def __init__(self, err=""):
        super().__init__("Nueva Advertencia: " + err)
    def display(self):
        messagebox.showwarning("Error de advertencia",self.args[0])
        print(self.args[0])
        
try:        
    if(__name__ == "__main__"):
        raise ErrorAdvertencia("Lanzamiento")
except (ErrorAdvertencia) as err:
    err.display()