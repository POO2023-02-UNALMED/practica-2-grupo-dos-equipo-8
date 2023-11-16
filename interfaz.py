from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk



ventana_inicio = Tk()
ventana_inicio.geometry("1500x1000")
ventana_inicio.title("Pasteleria DeliHorno")
icono=PhotoImage(file="icono.png")
ventana_inicio.iconphoto(True,icono)
# Frame de bienvenida
frame_bienvenida = Frame(ventana_inicio, width=100, height=100)
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



def ingresar():
    ventana_inicio.withdraw()
    ventana_principal=Tk()
    ventana_principal.title("DelHorno Administrator")
    ventana_principal.geometry("1500x1000")

    
    #Funciones
    def salir_principal():
        ventana_principal.destroy()
        ventana_inicio.deiconify()
        
        
        
    def aplicacion():
        mensaje = ("¡Bienvenido a Deli Horno!\n\n"
                "Una aplicación de gestión diseñada para panaderías y pastelerías, optimizando la producción, inventario y ventas de productos horneados. Permite gestionar inventarios, tomar pedidos por encargo, ajustar la producción diaria, adaptar precios según tendencias y asignar envíos a camiones de reparto. Utiliza programación orientada a objetos para una operación eficiente y una experiencia de usuario intuitiva. Desde la compra de materias primas hasta la entrega de productos.")
        messagebox.showinfo("Información de la aplicación", mensaje)

    def acercade():
        mensaje = ("¡Conoce a los Creadores de Deli Horno!\n\n"
                "Manuel Zuleta Arango\n"
                "Andres Guarin Salazar\n"
                "Juan Diego Ospina Ocampo\n"
                "Maria Isabel Quiroz")
        messagebox.showinfo("Creadores", mensaje)
        
    menubar = Menu(ventana_principal)

    # Menú Archivo
    menu_archivo = Menu(menubar, tearoff=0)
    menu_archivo.add_command(label="Aplicación", command=aplicacion)
    menu_archivo.add_command(label="Salir", command=salir_principal)

    # Menú Procesos y consultas (añadir comandos si es necesario)
    menu_procesos = Menu(menubar, tearoff=0)

    # Menú Ayuda (añadir comandos si es necesario)
    menu_ayuda = Menu(menubar, tearoff=0)

    # Agregar los menús al menubar
    menubar.add_cascade(label="Archivo", menu=menu_archivo)
    menubar.add_cascade(label="Procesos y consultas", menu=menu_procesos)
    menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
    
    #Menu Procesos y consultas
    menu_procesos.add_command(label="funcionalidad 1")
    menu_procesos.add_command(label="funcionalidad 2")
    menu_procesos.add_command(label="funcionalidad 3")
    menu_procesos.add_command(label="funcionalidad 4")
    menu_procesos.add_command(label="funcionalidad 5")
    
    
    #Menu ayuda
    menu_ayuda.add_command(label="acerca de",command=acercade)

    # Configurar la ventana con el menubar
    ventana_principal.config(menu=menubar)
    ventana_principal.mainloop()

#Frame de inicio
frame_inicio = Frame(ventana_inicio, width=100, height=10,bg="bisque2")
frame_inicio.grid(column=0, row=1, padx=50, pady=10, sticky="nsew")

boton_inicio=Button(frame_inicio, text="INGRESAR",bg="AntiqueWhite2",width=30,height=5,font=("Arial",10,"bold"),bd=5,relief="raised",command=ingresar)
boton_inicio.place(relx=0.1,rely=0.6)

ancho_inicio = 70
alto_inicio = 70
foto_inicio1 = ImageTk.PhotoImage(Image.open("foto_inicio1.png").resize((250, 100)))
foto_inicio2 = ImageTk.PhotoImage(Image.open("foto_inicio2.png").resize((ancho_inicio, alto_inicio)))
foto_inicio3 = ImageTk.PhotoImage(Image.open("foto_inicio3.png").resize((ancho_inicio, alto_inicio)))
foto_inicio4 = ImageTk.PhotoImage(Image.open("foto_inicio4.png").resize((ancho_inicio, alto_inicio)))
foto_inicio5 = ImageTk.PhotoImage(Image.open("foto_inicio5.png").resize((ancho_inicio, alto_inicio)))

label_inicio1 = Label(frame_inicio, image=foto_inicio1)
label_inicio2 = Label(frame_inicio, image=foto_inicio2)
label_inicio3 = Label(frame_inicio, image=foto_inicio3)
label_inicio4 = Label(frame_inicio, image=foto_inicio4)
label_inicio5 = Label(frame_inicio, image=foto_inicio5)
# Mensaje
mensaje = Label(frame_inicio, text="", font=("Arial", 12,"bold"), bg="bisque2",justify="center",wraplength="400")
mensaje.place(relx=0.1, rely=0.3)

def mostrar_mensaje(event):
    label_inicio1.place_forget()
    mensaje.config(text="´´Delicias que endulzan tu día,\nnuestro arte en cada bocado.´´")
#def volver_a_aparecer(event): GENERA UN ERROR #
 #   label_inicio1.place(relx=0.1, rely=0.3)
  #  mensaje.config(text="")
#Cuando entre a la imagen haga un cambio
label_inicio1.bind("<Enter>", mostrar_mensaje)
#label_inicio1.bind("<Leave>", volver_a_aparecer)

label_inicio1.place(relx=0.1, rely=0.3)
label_inicio2.place(relx=0, rely=0)
label_inicio3.place(relx=0.8, rely=0)
label_inicio4.place(relx=0.3, rely=0)
label_inicio5.place(relx=0.5, rely=0)

# Imágenes de Manuel
foto_manuel1 = Image.open("foto1_manuel.png")
foto_manuel2 = Image.open("foto2_manuel.png")
foto_manuel3 = Image.open("foto3_manuel.png")
foto_manuel4 = Image.open("foto4_manuel.png")

# Imagenes Juan

foto_juan1 = Image.open("foto1_juan.png")
foto_juan2 = Image.open("foto2_juan.png")
foto_juan3 = Image.open("foto3_juan.png")
foto_juan4 = Image.open("foto4_juan.png")

#Imagenes Andres

foto_andres1 = Image.open("foto1_andres.png")
foto_andres2 = Image.open("foto2_andres.png")
foto_andres3 = Image.open("foto3_andres.png")
foto_andres4 = Image.open("foto4_andres.png")

#Imagenes Maria
foto_maria1 = Image.open("foto1_maria.png")
foto_maria2 = Image.open("foto2_maria.png")
foto_maria3 = Image.open("foto3_maria.png")
foto_maria4 = Image.open("foto4_maria.png")

# Cambiar el tamaño de las imágenes (ajustar según sea necesario)
ancho = 200
alto = 150
foto_manuel1 = ImageTk.PhotoImage(foto_manuel1.resize((ancho, alto)))
foto_manuel2 = ImageTk.PhotoImage(foto_manuel2.resize((ancho, alto)))
foto_manuel3 = ImageTk.PhotoImage(foto_manuel3.resize((ancho, alto)))
foto_manuel4 = ImageTk.PhotoImage(foto_manuel4.resize((ancho, alto)))

foto_andres1 = ImageTk.PhotoImage(foto_andres1.resize((ancho, alto)))
foto_andres2 = ImageTk.PhotoImage(foto_andres2.resize((ancho, alto)))
foto_andres3 = ImageTk.PhotoImage(foto_andres3.resize((ancho, alto)))
foto_andres4 = ImageTk.PhotoImage(foto_andres4.resize((ancho, alto)))

foto_juan1 = ImageTk.PhotoImage(foto_juan1.resize((ancho, alto)))
foto_juan2 = ImageTk.PhotoImage(foto_juan2.resize((ancho, alto)))
foto_juan3 = ImageTk.PhotoImage(foto_juan3.resize((ancho, alto)))
foto_juan4 = ImageTk.PhotoImage(foto_juan4.resize((ancho, alto)))

foto_maria1 = ImageTk.PhotoImage(foto_maria1.resize((ancho, alto)))
foto_maria2 = ImageTk.PhotoImage(foto_maria2.resize((ancho, alto)))
foto_maria3 = ImageTk.PhotoImage(foto_maria3.resize((ancho, alto)))
foto_maria4 = ImageTk.PhotoImage(foto_maria4.resize((ancho, alto)))

# Datos de las biografías
biografias = [
    {"nombre": "Manuel Zuleta Arango", "correo": "mzueta@unal.edu.co", "cedula": "1001420813",
    "carrera": "Ingeniería de Sistemas", "edad": 21, "semestre": 9},
    {"nombre": "Juan Diego Ospina Ocampo", "correo": "jospinaoc@unal.edu.com", "cedula": "1001755818",
    "carrera": "Ciencias de la computación", "edad": 21, "semestre": 7},
    {"nombre": "Andres Guarin Salazar", "correo": "aguarins@unal.edu.co", "cedula": "1037659069",
    "carrera": "Ciencias de la Computación", "edad": 26, "semestre": 6},
    {"nombre": "Maria Isabel Quiroz", "correo": "mquirozr@unal.edu.co", "cedula": "1010028863",
    "carrera": "Ciencias de la computación", "edad": 22, "semestre": 5}
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
    seccion = LabelFrame(frame, text=nombre, font=("Arial", 25, "bold"), bg="LightPink2", padx=10, pady=5)
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
        
    elif biografia_actual == 1:
        Label(frame_imagenes, image=foto_juan1, bg="cornsilk1").grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_juan2, bg="cornsilk1").grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_juan3, bg="cornsilk1").grid(row=1, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_juan4, bg="cornsilk1").grid(row=1, column=1, padx=10, pady=20, sticky="nsew")
        
        frame_imagenes.grid_rowconfigure(0, weight=1)
        frame_imagenes.grid_rowconfigure(1, weight=1)
        frame_imagenes.grid_columnconfigure(0, weight=1)
        frame_imagenes.grid_columnconfigure(1, weight=1)
    elif biografia_actual == 2:
        Label(frame_imagenes, image=foto_andres1, bg="cornsilk1").grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_andres2, bg="cornsilk1").grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_andres3, bg="cornsilk1").grid(row=1, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_andres4, bg="cornsilk1").grid(row=1, column=1, padx=10, pady=20, sticky="nsew")
        
        frame_imagenes.grid_rowconfigure(0, weight=1)
        frame_imagenes.grid_rowconfigure(1, weight=1)
        frame_imagenes.grid_columnconfigure(0, weight=1)
        frame_imagenes.grid_columnconfigure(1, weight=1)
    elif biografia_actual == 3:
        Label(frame_imagenes, image=foto_maria1, bg="cornsilk1").grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_maria2, bg="cornsilk1").grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_maria3, bg="cornsilk1").grid(row=1, column=0, padx=10, pady=20, sticky="nsew")
        Label(frame_imagenes, image=foto_maria4, bg="cornsilk1").grid(row=1, column=1, padx=10, pady=20, sticky="nsew")
        
        frame_imagenes.grid_rowconfigure(0, weight=1)
        frame_imagenes.grid_rowconfigure(1, weight=1)
        frame_imagenes.grid_columnconfigure(0, weight=1)
        frame_imagenes.grid_columnconfigure(1, weight=1)
# Inicializar con la primera biografía
actualizar_biografia()

# Diseño de Menu
# funciones
# Label para la descripción


def mostrar_descripcion():
    frame_descripcion=Frame(frame_bienvenida).place(relx=0.2,rely=0)
    descripcion = Label(frame_descripcion, text="", font=("Arial", 12), bg="white")
    descripcion.grid(row=0,column=0)
    
    descripcion.config(text="Esta es la mejor app para administración pastelera de Colombia")

def salir():
    ventana_inicio.destroy()

menubar = Menu(ventana_inicio)

menu_principal = Menu(menubar, tearoff=0)
menu_principal.add_command(label="Descripción", command=mostrar_descripcion)
menu_principal.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Inicio", menu=menu_principal)

ventana_inicio.config(menu=menubar)

ventana_inicio.mainloop()

