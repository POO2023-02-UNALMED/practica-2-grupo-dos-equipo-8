from tkinter import *
ventana_principal=Tk()
ventana_principal.title("DelHorno Administrator")
ventana_principal.geometry("1500x1000")


#Funciones
def salir_principal():
    ventana_principal.destroy()
    interfaz()
def aplicacion():
    pass    
#Menu
menubar = Menu(ventana_principal)

menu_principal = Menu(menubar, tearoff=0)
menu_principal.add_command(label="aplicacion", command=aplicacion)
menu_principal.add_command(label="Salir", command=salir_principal)
menubar.add_cascade(label="Archivo", menu=menu_principal)

ventana_principal.config(menu=menubar)
ventana_principal.mainloop()