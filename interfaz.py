from tkinter import *

ventana_inicio = Tk()
ventana_inicio.geometry("1500x1000")

# Frame de bienvenida
frame_bienvenida = Frame(ventana_inicio, bg="brown", width=500, height=300)
frame_bienvenida.grid(column=0, row=0, padx=50, pady=10, sticky="nsew")

imagen_bienvenida = PhotoImage(file="bienvenida.png")
label_imagen = Label(frame_bienvenida, image=imagen_bienvenida)
label_imagen.grid(row=0, column=0, sticky="nsew")

# Frame de biografías
frame_biografias = Frame(ventana_inicio, bg="LightPink2", width=1000, height=300)
frame_biografias.grid(column=1, row=0, padx=20, pady=10, sticky="nsew")

# Datos de las biografías
biografias = [
    {"nombre": "Manuel Zuleta Arango", "correo": "mzueta@unal.edu.co", "cedula": "1001420813"},
    {"nombre": "Nombre2 Apellido2", "correo": "correo2@dominio.com", "cedula": "0987654321"},
    {"nombre": "Nombre3 Apellido3", "correo": "correo3@dominio.com", "cedula": "9876543210"},
    {"nombre": "Nombre4 Apellido4", "correo": "correo4@dominio.com", "cedula": "1234567890"}
]

# Variable para rastrear la biografía actual
biografia_actual = 0

# Función para cambiar la biografía
def cambiar_biografia():
    global biografia_actual
    biografia_actual = (biografia_actual + 1) % len(biografias)
    actualizar_biografia()

# Función para actualizar el contenido del frame de biografías
def actualizar_biografia():
    nombre = biografias[biografia_actual]["nombre"]
    correo = biografias[biografia_actual]["correo"]
    cedula = biografias[biografia_actual]["cedula"]

    for widget in frame_biografias.winfo_children():
        widget.destroy()

    biografia = crear_seccion_biografia(frame_biografias, nombre, correo, cedula)
    biografia.place(relx=0.5, rely=0.5, anchor="center")
    biografia.bind("<Button-1>", lambda event: cambiar_biografia())

# Función para crear la sección de biografía para cada creador
contador = 0
def crear_seccion_biografia(frame, nombre, correo, cedula):
    global contador
    seccion = LabelFrame(frame, text=nombre, font=("Arial", 10, "bold"), bg="LightPink2", padx=10, pady=5)
    Label(seccion, text="Correo: ", bg="LightPink2").grid(row=0, column=0, sticky="w")
    Label(seccion, text="Cédula: ", bg="LightPink2").grid(row=1, column=0, sticky="w")
    Label(seccion, text=correo, bg="LightPink2").grid(row=0, column=1, sticky="w")
    Label(seccion, text=cedula, bg="LightPink2").grid(row=1, column=1, sticky="w")
    if contador == 3:
        contador = 0
    return seccion

# Inicializar con la primera biografía
actualizar_biografia()

ventana_inicio.mainloop()
