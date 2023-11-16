from tkinter import *

class FieldFrame(Frame):
    def __init__(self, ventana_principal, funcionalidad):
        if funcionalidad=="funcionalidad 1":
             # Creamos un frame secundario dentro del Frame principal
            frame_nombre = Frame(ventana_principal, background="black", borderwidth=2,relief="solid")
            frame_nombre.pack(pady=50)

            # Ajustamos la grilla del frame_nombre
            frame_nombre.grid_rowconfigure(0, weight=1)
            frame_nombre.grid_columnconfigure(0, weight=1)

            # Creamos el label y lo centramos en el frame_nombre
            label_nombre = Label(frame_nombre, text="Compra de Materia prima",font=("Arial",25,"bold"))
            label_nombre.grid(row=0, column=0, sticky="n")  # Sticky north (arriba)

        elif funcionalidad=="funcionalidad 2":
             # Creamos un frame secundario dentro del Frame principal
            frame_nombre = Frame(ventana_principal, background="black", borderwidth=2,relief="solid")
            frame_nombre.pack(pady=50)

            # Ajustamos la grilla del frame_nombre
            frame_nombre.grid_rowconfigure(0, weight=1)
            frame_nombre.grid_columnconfigure(0, weight=1)

            # Creamos el label y lo centramos en el frame_nombre
            label_nombre = Label(frame_nombre, text="Venta por encargo",font=("Arial",25,"bold"))
            label_nombre.grid(row=0, column=0, sticky="n")  # Sticky north (arriba)

        elif funcionalidad=="funcionalidad 3":
             # Creamos un frame secundario dentro del Frame principal
            frame_nombre = Frame(ventana_principal, background="black", borderwidth=2,relief="solid")
            frame_nombre.pack(pady=50)

            # Ajustamos la grilla del frame_nombre
            frame_nombre.grid_rowconfigure(0, weight=1)
            frame_nombre.grid_columnconfigure(0, weight=1)

            # Creamos el label y lo centramos en el frame_nombre
            label_nombre = Label(frame_nombre, text="Cambiar la lista de producción díaria",font=("Arial",25,"bold"))
            label_nombre.grid(row=0, column=0, sticky="n")  # Sticky north (arriba)

        elif funcionalidad=="funcionalidad 4":
             # Creamos un frame secundario dentro del Frame principal
            frame_nombre = Frame(ventana_principal, background="black", borderwidth=2,relief="solid")
            frame_nombre.pack(pady=50)

            # Ajustamos la grilla del frame_nombre
            frame_nombre.grid_rowconfigure(0, weight=1)
            frame_nombre.grid_columnconfigure(0, weight=1)

            # Creamos el label y lo centramos en el frame_nombre
            label_nombre = Label(frame_nombre, text="Agregar un producto",font=("Arial",25,"bold"))
            label_nombre.grid(row=0, column=0, sticky="n")  # Sticky north (arriba)

        elif funcionalidad=="funcionalidad 5":
             # Creamos un frame secundario dentro del Frame principal
            frame_nombre = Frame(ventana_principal, background="black", borderwidth=2,relief="solid")
            frame_nombre.pack(pady=50)

            # Ajustamos la grilla del frame_nombre
            frame_nombre.grid_rowconfigure(0, weight=1)
            frame_nombre.grid_columnconfigure(0, weight=1)

            # Creamos el label y lo centramos en el frame_nombre
            label_nombre = Label(frame_nombre, text="Eliminar un producto",font=("Arial",25,"bold"))
            label_nombre.grid(row=0, column=0, sticky="n")  # Sticky north (arriba)

        elif funcionalidad=="funcionalidad 6":
             # Creamos un frame secundario dentro del Frame principal
            frame_nombre = Frame(ventana_principal, background="black", borderwidth=2,relief="solid")
            frame_nombre.pack(pady=50)

            # Ajustamos la grilla del frame_nombre
            frame_nombre.grid_rowconfigure(0, weight=1)
            frame_nombre.grid_columnconfigure(0, weight=1)

            # Creamos el label y lo centramos en el frame_nombre
            label_nombre = Label(frame_nombre, text="Asignar Envio y camión",font=("Arial",25,"bold"))
            label_nombre.grid(row=0, column=0, sticky="n")  # Sticky north (arriba)

        elif funcionalidad=="funcionalidad 7":
             # Creamos un frame secundario dentro del Frame principal
            frame_nombre = Frame(ventana_principal, background="black", borderwidth=2,relief="solid")
            frame_nombre.pack(pady=50)

            # Ajustamos la grilla del frame_nombre
            frame_nombre.grid_rowconfigure(0, weight=1)
            frame_nombre.grid_columnconfigure(0, weight=1)

            # Creamos el label y lo centramos en el frame_nombre
            label_nombre = Label(frame_nombre, text=" Cambiar la produccion y/o ventas",font=("Arial",25,"bold"))
            label_nombre.grid(row=0, column=0, sticky="n")  # Sticky north (arriba)