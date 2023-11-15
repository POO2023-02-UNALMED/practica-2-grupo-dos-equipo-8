from tkinter import *
from PIL import Image, ImageTk

def ir_a_inicio():
    # Agrega aquí la lógica para ir a la pantalla de inicio
    pass

def mostrar_descripcion():
    descripcion.config(text="Esta es la mejor app para administración pastelera de Colombia")

ventana_inicio = Tk()
ventana_inicio.geometry("1500x1000")

# Frame de bienvenida
frame_bienvenida = Frame(ventana_inicio, bg="brown", width=300, height=300)
frame_bienvenida.grid(column=0, row=0, padx=50, pady=10, sticky="nsew")

imagen_bienvenida = PhotoImage(file="bienvenida.png")
label_imagen = Label(frame_bienvenida, image=imagen_bienvenida)
label_imagen.grid(row=0, column=0, sticky="nsew")

# Frame de biografías
frame_biografias = Frame(ventana_inicio, bg="LightPink2", width=900, height=300)
frame_biografias.grid(column=1, row=0, padx=20, pady=10, sticky="nsew")

# Frame de imágenes
frame_imagenes = Frame(ventana_inicio, bg="cornsilk1", width=300, height=300)
frame_imagenes.grid(column=1, row=1, padx=20, pady=10, sticky="nsew")

# Frame de inicio con botón
frame_inicio = Frame(ventana_inicio, width=300, height=300, bg="AntiqueWhite1")
frame_inicio.grid(column=0, row=1, padx=50, pady=10, sticky="nsew")

boton_inicio = Button(frame_inicio, text="Ingresar", bg="AntiqueWhite2")
boton_inicio.grid(row=3, column=1, sticky="n", padx=125, pady=5)

# Redimensionar imágenes de inicio
foto_inicio1 = Image.open("foto_inicio1.png").resize((150, 150), Image.ANTIALIAS)
foto_inicio2 = Image.open("foto_inicio2.png").resize((150, 150), Image.ANTIALIAS)
foto_inicio3 = Image.open("foto_inicio3.png").resize((150, 150), Image.ANTIALIAS)
foto_inicio4 = Image.open("foto_inicio4.png").resize((150, 150), Image.ANTIALIAS)
foto_inicio5 = Image.open("foto_inicio5.png").resize((150, 150), Image.ANTIALIAS)

# Convertir imágenes a formato Tkinter
foto_inicio1 = ImageTk.PhotoImage(foto_inicio1)
foto_inicio2 = ImageTk.PhotoImage(foto_inicio2)
foto_inicio3 = ImageTk.PhotoImage(foto_inicio3)
foto_inicio4 = ImageTk.PhotoImage(foto_inicio4)
foto_inicio5 = ImageTk.PhotoImage(foto_inicio5)

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
    carrera = biografias[biografia_actual]["carrera"]
    edad = biografias[biografia_actual]["edad"]
    semestre = biografias[biografia_actual]["semestre"]

    for widget in frame_biografias.winfo_children():
        widget.destroy()

    biografia = crear_seccion_biografia(frame_biografias, nombre, correo, cedula, carrera, edad, semestre)
    biografia.place(relx=0.5, rely=0.5, anchor="center")
    biografia.bind("<Button-1>", lambda event: cambiar_biografia())

    # Mostrar las imágenes correspondientes en el frame_imagenes
    mostrar_imagenes()

# Función para crear la sección de biografía para cada creador
def crear_seccion_biografia(frame, nombre, correo, cedula, carrera, edad, semestre):
    seccion = LabelFrame(frame, text=nombre, font=("Arial", 14, "bold"), bg="LightPink2", padx=10, pady=5)
    Label(seccion, text="Correo: ", bg="LightPink2", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
    Label(seccion, text="Cédula: ", bg="LightPink2", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
    Label(seccion, text="Carrera: ", bg="LightPink2", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
    Label(seccion, text="Edad: ", bg="LightPink2", font=("Arial", 12)).grid(row=3, column=0, sticky="w")
    Label(seccion, text="Semestre: ", bg="LightPink2", font=("Arial", 12)).grid(row=4, column=0, sticky="w")
    Label(seccion, text=correo, bg="LightPink2", font=("Arial", 12)).grid(row=0, column=1, sticky="w")
    Label(seccion, text=cedula, bg="LightPink2", font=("Arial", 12)).grid(row=1, column=1, sticky="w")
    Label(seccion, text=carrera, bg="LightPink2", font=("Arial", 12)).grid(row=2, column=1, sticky="w")
    Label(seccion, text=str(edad), bg="LightPink2", font=("Arial", 12)).grid(row=3, column=1, sticky="w")
    Label(seccion, text=str(semestre), bg="LightPink2", font=("Arial", 12)).grid(row=4, column=1, sticky="w")
    return seccion

# Función para mostrar las imágenes en el frame_imagenes
def mostrar_imagenes():
    # Limpiar el frame_imagenes
    for widget in frame_imagenes.winfo_children():
        widget.destroy()

    # Mostrar las imágenes correspondientes
    if biografia_actual == 0:  # Manuel
        Label(frame_imagenes, image=foto_manuel1, bg="cornsilk1").grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_manuel2, bg="cornsilk1").grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_manuel3, bg="cornsilk1").grid(row=1, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_manuel4, bg="cornsilk1").grid(row=1, column=1, padx=10, pady=20, sticky="nsew")

        # Configurar el frame para que las filas y columnas se expandan al centro
        frame_imagenes.grid_rowconfigure(0, weight=1)
        frame_imagenes.grid_rowconfigure(1, weight=1)
        frame_imagenes.grid_columnconfigure(0, weight=1)
        frame_imagenes.grid_columnconfigure(1, weight=1)

# Inicializar con la primera biografía
actualizar_biografia()

# Diseño de Menu
# funciones
# Label para la descripción
descripcion = Label(ventana_inicio, text="", font=("Arial", 12), bg="white")
descripcion.grid(row=2, column=0, columnspan=2, sticky="nsew")

def mostrar_descripcion():
    descripcion.config(text="Esta es la mejor app para administración pastelera de Colombia")

def salir():
    ventana_inicio.destroy()

menubar = Menu(ventana_inicio)

menu_principal = Menu(menubar, tearoff=0)
menu_principal.add_command(label="Inicio", command=ir_a_inicio)
menu_principal.add_command(label="Descripción", command=mostrar_descripcion)
menu_principal.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Menú", menu=menu_principal)

ventana_inicio.config(menu=menubar)

ventana_inicio.mainloop()
