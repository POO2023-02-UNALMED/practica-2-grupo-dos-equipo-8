from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import sys
# Agregar la ruta del directorio 'src' al principio de sys.path
sys.path.insert(0, './src')

from gestor_aplicacion.empresa.envio import Envio
from gestor_aplicacion.empresa.ingrediente import Ingrediente

##from gestor_aplicacion.empresa.administrador import *
##from gestor_aplicacion.producto.producto import *

from gestor_aplicacion.empresa.administrador import Administrador
from gestor_aplicacion.empresa.camion import Camion
from gestor_aplicacion.empresa.bodega import Bodega
from gestor_aplicacion.empresa.caja import Caja
from gestor_aplicacion.producto.producto import Producto
from gestor_aplicacion.producto.torta import Tortas
from gestor_aplicacion.producto.dona import Donas
from gestor_aplicacion.producto.pastel_frito import PastelesFritos
from gestor_aplicacion.producto.galleta import Galleta

administrador = Administrador.crear_todo()


ventana_inicio = Tk()
ventana_inicio.geometry("1500x1000")
ventana_inicio.title("Pasteleria DeliHorno")
icono=PhotoImage(file="assets/icono.png")
ventana_inicio.iconphoto(True,icono)
# Frame de bienvenida
frame_bienvenida = Frame(ventana_inicio, width=100, height=100)
frame_bienvenida.grid(column=0, row=0, padx=50, pady=10, sticky="nsew")

imagen_bienvenida = PhotoImage(file="assets/bienvenida.png")
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

    #Clase FieldFrame   
    class FieldFrame(Frame):
        def __init__(self,criterio,criterios,valor_inicial,permitir_cambios,funcionalidad):
            
            #Permite que se hagan cambios en el combo box
            self.permitir_cambios=permitir_cambios
            #Elementos del combo box a elegir
            self.criterio=criterio
            #Pregunta al usuario
            self.label_petición=Label(frame_dialogo,text=criterio)
            #Combo box
            self.combo_box=ttk.Combobox(frame_dialogo,values=criterios)
            #valor inicial del combo box
            self.combo_box.set(valor_inicial)
            
            
            #Posición de los elementos
            self.label_petición.grid(row=0,column=0,padx=10,pady=50)
            self.combo_box.grid(row=0,column=1,padx=10,pady=50)
            boton_confirmación=Button(frame_dialogo,text="Enviar")
            boton_confirmación.grid(row=0,column=2,padx=10,pady=50)

            #Función del boton de confirmación
            if funcionalidad=="funcionalidad1":
                etapa=0
                seleccion=None
                def enviar():
                    nonlocal etapa, seleccion
                    if etapa==0:
                        if self.combo_box.get()=="1":
                            self.label_petición.config(text="""Aquí puede ver los ingredientes escasos,
                                                    ¿Está seguro de que necesita comprar ingredientes? (1.Si / 2.No): """)
                            label_informacion.config(text=administrador.bodega.mostrar_ingredientes_escasos(),borderwidth=2,relief="solid")
                            etapa+=1
                        if self.combo_box.get()=="2":
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                    
                    elif etapa==1:
                        if self.combo_box.get()=="1":
                            self.label_petición.config(text="Seleccione el ingrediente que desea pedir:")
                            self.combo_box.config(values=list(range(1, len(Ingrediente.ingredientes_disponibles) + 1)))
                            label_informacion.config(text=Ingrediente.obtener_lista_ingredientes(),borderwidth=2,relief="solid")
                            etapa+=1
                        if self.combo_box.get()=="2":
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                    elif etapa==2:
                        seleccion=self.combo_box.get()
                        nombre_seleccionado=Ingrediente.ingredientes_disponibles[int(seleccion)-1].nombre
                        self.combo_box.destroy()
                        self.label_petición.config(text="Ingrese la cantidad que desea pedir de "+nombre_seleccionado+":")
                        self.nuevo_valor=Entry(frame_dialogo)
                        self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                        etapa+=1
                    elif etapa==3:
                        cantidad=self.nuevo_valor.get()
                        etapa+=1
                    else:
                        pass
                
                boton_confirmación.config(command=enviar)
            
            elif funcionalidad=="funcionalidad2":
                etapa=0
                codigo=None
                primera_vez=True
                # Crear una lista para almacenar los productos seleccionados
                productos_seleccionados = []

                 # Variable para controlar si el cliente quiere seleccionar más productos
                seleccionar_otro_producto = True
                def enviar():
                    nonlocal etapa, codigo, primera_vez
                    if etapa==0:
                        if self.combo_box.get()=="1":
                            self.combo_box.destroy()
                            self.label_petición.config(text="Ingrese un código de envío (número entero):")
                            self.nuevo_valor=Entry(frame_dialogo)
                            self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                            etapa+=1
                        elif self.combo_box.get()=="2":
                            self.label_petición.config(text="Hasta luego, hablanos cuando estes listo para realizar una venta por encargo, selecciona otra funcionalidad para hacer otros cambios")
                            self.combo_box.state(["disabled"])
                            label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                    elif etapa==1:
                        
                        if primera_vez==True:
                            codigo=self.nuevo_valor.get()
                            self.nuevo_valor.destroy()
                            self.label_petición.config(text="Elija un producto ingresando el número correspondiente:")
                            self.nuevo_combo_box=ttk.Combobox(frame_dialogo,values=list(range(1, len(administrador.bodega.productos) + 1)))
                            self.nuevo_combo_box.grid(row=0,column=1,padx=10,pady=50)
                            label_informacion.config(text=administrador.bodega.mostrar_productos(),borderwidth=2,relief="solid")
                            
                            primera_vez=False
                        elif primera_vez==False:
                            self.label_petición.config(text="Elija un producto ingresando el número correspondiente:")
                            label_informacion.config(text=administrador.bodega.mostrar_productos(),borderwidth=2,relief="solid")
                            self.nuevo_combo_box.config(values=list(range(1, len(administrador.bodega.productos) + 1)))
                            self.nuevo_combo_box.state(["!disabled"])
                        etapa+=1
                    elif etapa==2:
                        seleccion=self.nuevo_combo_box.get()
                        producto_elegido=administrador.bodega.productos[int(seleccion)-1]
                        if seleccion not in productos_seleccionados:
                            productos_seleccionados.append(producto_elegido)
                            self.label_petición.config(text=f"Has elegido el producto: {producto_elegido.nombre}"+"\n¿Desea seleccionar otro producto? (1.Si / 2.No):")
                            self.nuevo_combo_box.config(values=["1","2"])
                            etapa+=1
                        else:
                            self.label_petición.config(text="El producto ya ha sido seleccionado, por favor elija otro")
                            self.nuevo_combo_box.config(values=list(range(1, len(administrador.bodega.productos) + 1)))

                    elif etapa==3:
                        if self.nuevo_combo_box.get()=="1":
                            etapa=1
                            self.label_petición.config(text="Me alegra que quieras seleccionar otro producto, por favor derle click en enviar para confirmar")
                            self.nuevo_combo_box.state(["disabled"])

                        elif self.nuevo_combo_box.get()=="2":
                            nuevo_envio=Envio(int(codigo),productos_seleccionados,administrador.caja,administrador.bodega)
                            self.nuevo_combo_box.destroy()
                            self.label_petición.destroy()
                            boton_confirmación.destroy()
                            label_informacion.config(text=f"Se ha creado un nuevo envío con código {nuevo_envio.codigo_de_envio} y los productos seleccionados.",borderwidth=2,relief="solid")
                            
                boton_confirmación.config(command=enviar)


            elif funcionalidad=="funcionalidad3":
                pass

            elif funcionalidad=="funcionalidad4":
                etapa=0
                nombre=None
                precio=None
                identificador=None
                espacio_de_almacenamiento=None
                cantidades=[]
                ingredientes=[]
                ingredientes_y_cantidad={}
                self.nuevo_combo_box=ttk.Combobox(frame_dialogo,values=["1","2","3","4"])
                ingrediente_elegido=None
                def enviar():
                    nonlocal etapa, nombre,precio,identificador,espacio_de_almacenamiento,cantidades,ingredientes,ingredientes_y_cantidad,ingrediente_elegido
                    if etapa==0:
                        if self.nuevo_combo_box.get()=="1":
                            self.nuevo_valor.destroy()
                            self.label_petición.config(text="Ingrese el nombre del nuevo ingrediente: ")
                            self.combo_box.destroy()
                            self.nuevo_valor=Entry(frame_dialogo)
                            self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                            etapa+=1
                        elif self.combo_box.get()=="1":
                            self.label_petición.config(text="Ingrese el nombre del nuevo ingrediente:")
                            self.combo_box.destroy()
                            self.nuevo_valor=Entry(frame_dialogo)
                            self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                            etapa+=1
                        elif self.combo_box.get()=="2":
                            self.label_petición.config(text="Oprima enviar para confirmar")
                            self.combo_box.state(["disabled"])
                            etapa=6
                        
                    elif etapa==1:
                        nombre=self.nuevo_valor.get()
                        self.nuevo_valor.destroy()
                        self.label_petición.config(text="Ingrese el precio del nuevo producto:")
                        self.nuevo_valor=Entry(frame_dialogo)
                        self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                        etapa+=1
                        
                    elif etapa==2:
                        precio=self.nuevo_valor.get()
                        self.nuevo_valor.destroy()
                        self.label_petición.config(text="Ingrese el identificador del nuevo producto:")
                        self.nuevo_valor=Entry(frame_dialogo)
                        self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                        etapa+=1
                    
                    elif etapa==3:
                        identificador=self.nuevo_valor.get()
                        self.nuevo_valor.destroy()
                        self.label_petición.config(text="Ingrese el espacio de almacenamiento del nuevo producto:")
                        self.nuevo_valor=Entry(frame_dialogo)
                        self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                        etapa+=1
                        
                    elif etapa==4:
                        espacio_de_almacenamiento=self.nuevo_valor.get()
                        self.nuevo_valor.destroy()
                        self.label_petición.config(text="Quieres crear otro ingrediente? (1.Si / 2.No): ")
                        self.nuevo_combo_box=ttk.Combobox(frame_dialogo,values=["1","2"])
                        self.nuevo_combo_box.grid(row=0,column=1,padx=10,pady=50)
                        etapa+=1
                        
                    elif etapa==5:
                        if self.nuevo_combo_box.get()=="1":
                            nuevo_ingrediente=Ingrediente(nombre,int(precio),identificador,espacio_de_almacenamiento)
                            temporal = administrador.bodega.ingredientes[:]
                            temporal.append(nuevo_ingrediente)
                            self.label_petición.config(text="Se ha creado un nuevo ingrediente y se crara uno nuevo, por favor derle click en enviar para confirmar")
                            self.nuevo_combo_box.state(["disabled"])
                            etapa=0
                        elif self.nuevo_combo_box.get()=="2":
                            nuevo_ingrediente=Ingrediente(nombre,int(precio),identificador,espacio_de_almacenamiento)
                            temporal = administrador.bodega.ingredientes[:]
                            temporal.append(nuevo_ingrediente)
                            self.label_petición.config(text="Se ha creado un nuevo ingrediente, por favor derle click en enviar para confirmar")
                            self.nuevo_combo_box.state(["disabled"])
                            etapa+=1
                    elif etapa==6:
                        self.label_petición.config(text="Seleccione el número correspondiente al ingrediente que necesita para su producto:")
                        self.nuevo_combo_box.config(values=list(range(1, len(administrador.bodega.ingredientes) + 1)))
                        label_informacion.config(text=Ingrediente.obtener_lista_ingredientes(),borderwidth=2,relief="solid")
                        self.combo_box.destroy()
                        self.nuevo_combo_box=ttk.Combobox(frame_dialogo,values=list(range(1, len(administrador.bodega.ingredientes) + 1)))
                        self.nuevo_combo_box.grid(row=0,column=1,padx=10,pady=50)
                        etapa+=1
                        
                    elif etapa==7:
                        ingrediente_elegido=administrador.bodega.ingredientes[int(self.nuevo_combo_box.get())-1]
                        ingredientes.append(ingrediente_elegido)
                        self.label_petición.config(text="Ingrese la cantidad que necesita de este ingrediente:")
                        self.nuevo_valor=Entry(frame_dialogo)
                        self.nuevo_valor.grid(row=0,column=1,padx=10,pady=50)
                        self.nuevo_combo_box.destroy()
                        etapa+=1
                        
                    elif etapa==8:
                        cantidad=self.nuevo_valor.get()
                        cantidades.append(cantidad)
                        ingredientes_y_cantidad[ingrediente_elegido]=int(cantidad)
                        self.nuevo_valor.destroy()
                        self.label_petición.config(text="Quieres agregar otro ingrediente? (1.Si / 2.No): ")
                        self.nuevo_combo_box=ttk.Combobox(frame_dialogo,values=["1","2"])
                        self.nuevo_combo_box.grid(row=0,column=1,padx=10,pady=50)
                        etapa+=1
                    
                    elif etapa==9:
                        if self.nuevo_combo_box.get()=="1":
                            self.label_petición.config(text="Click para confirmar")
                            self.nuevo_combo_box.state(["disabled"])
                            etapa=6
                        elif self.nuevo_combo_box.get()=="2":
                            if len(ingredientes)<2:
                                self.label_petición.config(text="Se necesitan al menos 2 ingredientes para crear un producto, por favor derle click en enviar para confirmar")
                                self.nuevo_combo_box.state(["disabled"])
                                etapa=6
                            elif len(ingredientes)>=2:
                                self.label_petición.config(text="Seleccione el tipo de producto que desea crear:")
                                self.nuevo_combo_box.config(values=["1","2","3","4"])
                                label_informacion.config(text="1. Torta\n2. Dona\n3. Pastel frito\n4. Galleta",borderwidth=2,relief="solid")
                                etapa+=1
                    elif etapa==10:
                        tipo_de_producto=self.nuevo_combo_box.get()
                        if tipo_de_producto=="1":
                            nuevo_producto=Tortas("torta",5 ,ingredientes_y_cantidad,0,"abc123",3,6,"chocolate")
                            self.label_petición.config(text=f"Producto exitosamente creado: {nuevo_producto.nombre}, por favor derle click en enviar para confirmar")
                            self.nuevo_combo_box.state(["disabled"])
                            temp1 = administrador.bodega.productos[:]
                            temp1.append(nuevo_producto)
                            bodegatemporal1 = administrador.bodega
                            bodegatemporal1.productos = temp1
                            administrador.bodega = bodegatemporal1
                            etapa+=1
                        elif tipo_de_producto=="2":
                            nuevo_producto=Donas("dona", 5, ingredientes_y_cantidad, 20, "dfg123", 3, False, "arquipe")
                            self.label_petición.config(text=f"Producto exitosamente creado: {nuevo_producto.nombre}, por favor derle click en enviar para confirmar")
                            self.nuevo_combo_box.state(["disabled"])
                            temp1 = administrador.bodega.productos[:]
                            temp1.append(nuevo_producto)
                            bodegatemporal1 = administrador.bodega
                            bodegatemporal1.productos = temp1
                            administrador.bodega = bodegatemporal1
                            etapa+=1
                        elif tipo_de_producto=="3":
                            nuevo_producto=PastelesFritos("pastelFrito", 5, ingredientes_y_cantidad, 20, "dfg123", 3, False, "tomate")
                            self.label_petición.config(text=f"Producto exitosamente creado: {nuevo_producto.nombre}, por favor derle click en enviar para confirmar")
                            temp1 = administrador.bodega.productos[:]
                            temp1.append(nuevo_producto)
                            bodegatemporal1 = administrador.bodega
                            bodegatemporal1.productos = temp1
                            administrador.bodega = bodegatemporal1
                            self.nuevo_combo_box.state(["disabled"])
                            etapa+=1
                        elif tipo_de_producto=="4":
                            nuevo_producto=Galleta("galleta", 5, ingredientes_y_cantidad, 20, "dfg123", 3, False, "vainilla")
                            self.label_petición.config(text=f"Producto exitosamente creado: {nuevo_producto.nombre}, por favor derle click en enviar para confirmar")
                            self.nuevo_combo_box.state(["disabled"])
                            temp1.append(nuevo_producto)
                            bodegatemporal1 = administrador.bodega
                            bodegatemporal1.productos = temp1
                            administrador.bodega = bodegatemporal1
                            self.nuevo_combo_box.state(["disabled"])
                            etapa+=1
                    elif etapa==11:
                        self.label_petición.destroy()
                        self.combo_box.destroy()
                        boton_confirmación.destroy()
                        self.nuevo_combo_box.destroy()
                        label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                        etapa+=1
                        
                    elif etapa==12:
                        pass
                            
                            
                            
                        
                        
                
                
                
                boton_confirmación.config(command=enviar)
                

            elif funcionalidad=="funcionalidad5":
                etapa=0
                producto_elegido=None
                def enviar():
                    nonlocal etapa,producto_elegido
                    if etapa==0:
                        producto_elegido=administrador.bodega.productos[int(self.combo_box.get())-1]
                        self.label_petición.config(text=f"¿Seguro que desea eliminar el producto {producto_elegido.nombre}? (1.Sí / 2.No):" )
                        self.combo_box.config(values=["1","2"])
                        label_informacion.config(text=administrador.bodega.mostrar_productos(),borderwidth=2,relief="solid")
                        etapa+=1
                    elif etapa==1:
                        if self.combo_box.get()=="1":
                            administrador.bodega.productos.remove(producto_elegido)
                            self.label_petición.config(text=f"Se ha eliminado el producto {producto_elegido.nombre}, por favor derle click en enviar para confirmar")
                            label_informacion.config(text=administrador.bodega.mostrar_productos(),borderwidth=2,relief="solid")
                            self.combo_box.state(["disabled"])
                            etapa+=1
                        elif self.combo_box.get()=="2":
                            self.label_petición.config(text="No se elimino ningun producto, Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                            etapa+=1
                    elif etapa==2:
                        self.label_petición.destroy()
                        self.combo_box.destroy()
                        boton_confirmación.destroy()
                        label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                        etapa+=1
                        
                    elif etapa==3:
                        pass
                            
                        
                                           
                
                
                
                boton_confirmación.config(command=enviar)
                

            elif funcionalidad=="funcionalidad6":
                etapa=0
                envio_seleccionado=None
                camion_seleccionado=None
                def enviar():
                    nonlocal etapa, envio_seleccionado, camion_seleccionado
                    if etapa==-1:
                        self.combo_box.state(["!disabled"])
                        self.label_petición.config(text="Seleccione el número del envío que desea asignar a un camión:")
                        self.combo_box.config(values=list(range(1, len(Envio.lista_envios_no_asignados) + 1)))
                        label_informacion.config(text=Envio.envios_por_asignar(),borderwidth=2,relief="solid")
                        etapa+=1

                    elif etapa==0:
                        envio_seleccionado=Envio.lista_envios_no_asignados[int(self.combo_box.get())-1]
                        envio_seleccionado.asignado_a_un_camion=True
                        self.label_petición.config(text="Seleccione el camión que desea asignar:")
                        label_informacion.config(text=Camion.camiones_y_capacidad(envio_seleccionado.peso_total),borderwidth=2,relief="solid")
                        self.combo_box.config(values=list(range(1, len(administrador.camiones) + 1)))
                        etapa+=1
                    elif etapa==1:
                        camion_seleccionado=administrador.camiones[int(self.combo_box.get())-1]
                        camion_seleccionado.agregar_envio(envio_seleccionado)
                        envio_seleccionado.camion_asignado=camion_seleccionado
                        envio_seleccionado.asignado_a_un_camion=True
                        camion_seleccionado.capacidad-=envio_seleccionado.peso_total
                        Envio.lista_envios_no_asignados.remove(envio_seleccionado)
                        Envio.lista_envios_asignados.append(envio_seleccionado)
                        label_informacion.config(text=f"Se ha asignado el envío {envio_seleccionado.codigo_de_envio} al camión{camion_seleccionado.marca} {camion_seleccionado.modelo} {camion_seleccionado.placa}",borderwidth=2,relief="solid")
                        self.label_petición.config(text="¿Desea enviar el camión? (1. Sí / 2. No):")
                        self.combo_box.config(values=["1","2"])
                        etapa+=1

                    elif etapa==2:
                        if self.combo_box.get()=="1":
                            camion_seleccionado.disponibilidad=False
                            label_informacion.config(text=f"Se ha enviado el camión {camion_seleccionado.marca} {camion_seleccionado.modelo} {camion_seleccionado.placa}",borderwidth=2,relief="solid")
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            pass
                        elif self.combo_box.get()=="2":
                            self.label_petición.config(text="¿Desea realizar otro envío? (1. Sí / 2. No):")
                            self.combo_box.config(values=["1","2"])
                            label_informacion.config(text="")
                            etapa+=1

                    elif etapa==3:
                        if self.combo_box.get()=="1":
                            self.label_petición.config(text="Estamos muy felices de que quieras realizar otro envío, por favor derle click en enviar para confirmar")
                            self.combo_box.state(["disabled"])
                            etapa=-1
                        elif self.combo_box.get()=="2":
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                            etapa+=1
                            
                    elif etapa==4:
                        self.label_petición.destroy()
                        self.combo_box.destroy()
                        boton_confirmación.destroy()    
                boton_confirmación.config(command=enviar)
                        
            elif funcionalidad=="funcionalidad7":
                etapa=0
                respuesta1=None
                respuesta2=None
                def enviar():
                    nonlocal etapa, respuesta1, respuesta2
                    if etapa==0:
                        if self.combo_box.get()=="1":
                            self.label_petición.config(text="Desea cambiar la produccion de los productos?:")
                            self.combo_box.config(values=["sí","no"])
                            etapa+=1
                        elif self.combo_box.get()=="2":
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                    elif etapa==1:
                        respuesta1=self.combo_box.get()
                        if self.combo_box.get()=="sí":
                            label_informacion.config(text="Se ha cambiado la produccion de los productos")
                            self.label_petición.config(text="Desea cambiar el precio de los productos?:")
                            self.combo_box.config(values=["sí","no"])
                            etapa+=1
                        elif self.combo_box.get()=="no":
                            self.label_petición.config(text="Desea cambiar el precio de los productos?:")
                            label_informacion.config(text="No se ha cambiado la produccion de los productos")
                            self.combo_box.config(values=["sí","no"])
                            etapa+=2
                    elif etapa==2:
                        respuesta2=self.combo_box.get()
                        if self.combo_box.get()=="sí":
                            label_informacion.config(text="Se ha cambiado el precio de los productos")
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            etapa+=1
                        elif self.combo_box.get()=="no":
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            label_informacion.config(text=administrador.bodega.actualizar_produccion_precio(respuesta1,respuesta2,administrador.fabrica),borderwidth=2,relief="solid")
                            etapa+=1
                    elif etapa==3:
                        if self.combo_box.get()=="sí":
                            label_informacion.config(text=administrador.bodega.actualizar_produccion_precio(respuesta1,respuesta2,administrador.fabrica),borderwidth=2,relief="solid")
                            self.label_petición.config(text="Hasta luego, seleccione otra funcionalidad si así lo desea")
                            self.combo_box.state(["disabled"])
                            etapa+=1
                            
                    elif etapa==4:
                        self.label_petición.destroy()
                        self.combo_box.destroy()
                        boton_confirmación.destroy()
                        label_informacion.config(text="Esperamos vuelvas pronto",borderwidth=2,relief="solid")
                    
                        


                            
                            
                            


                    
                        
                    









                boton_confirmación.config(command=enviar)

            

            
    
    #Funcioon para error al ejecutar varias veces
    def cerrarVentana():
        ventana_inicio.destroy()
        ventana_principal.destroy()
    #Asociamos la funcion anterior a la "X"
    ventana_principal.protocol("WM_DELETE_WINDOW",cerrarVentana)

    #Funciones
    def salir_principal():
        ventana_principal.destroy()
        ventana_inicio.deiconify()


    # Ajustamos la grilla de la ventana principal
    ventana_principal.grid_rowconfigure(0, weight=1)
    ventana_principal.grid_columnconfigure(0, weight=1)

    #Frame del nombre
    frame_nombre = Frame(ventana_principal) 
    frame_nombre.grid(row=0,column=0,pady=5,padx=5)

    # Creamos el label y lo centramos en el frame_nombre
    label_nombre = Label(frame_nombre, text="",font=("Arial",15,"bold"))
    label_nombre.grid(row=0, column=0)  # Centrado en el frame_nombre

    #Frame de descripción
    frame_descripción = Frame(ventana_principal) 
    frame_descripción.grid(row=1,column=0,pady=100,padx=5)

    # Creamos el label y lo centramos en el frame_nombre
    label_descripción = Label(frame_descripción, text="",font=("Arial",12,"bold"))
    label_descripción.grid(row=0, column=0)  # Centrado en el frame_descripción

    #Frame de dialogo
    frame_dialogo = Frame(ventana_principal,relief="solid",borderwidth=2) 
    frame_dialogo.grid(row=2,column=0,pady=0,padx=0)

    #Frame_informacion estará a la derecha de frame_dialogo
    frame_inofrmacion=Frame(frame_dialogo)
    frame_inofrmacion.grid(row=0,column=1,pady=200,padx=0)

    label_informacion=Label(frame_dialogo,text="",font=("Arial",12,"bold"))
    label_informacion.grid(row=0,column=0)  # Centrado en el frame_informacion12,"bold"))
    label_informacion.grid(row=0,column=3,pady=50,padx=0)
    
   
    
    
    
    
    

    def funcionalidad1():
        
        label_nombre.config(text="Compra de materia prima",borderwidth=2,relief="solid")
        label_descripción.config(text=(
            "La materia prima es escencial para la producción díaria y el funcionamiento de la empresa, para esto se verificará la disponibilidad en la bodega" 
            +"\n  las cantidades necesarias, verifica fondos y de todo estar bien realiza la compra"),borderwidth=2,relief="solid")
        label_informacion.config(text=administrador.bodega.mostrar_contabilidad_ingredientes(),borderwidth=2,relief="solid")
        FieldFrame("¿Cree necesario comprar ingredientes? (1.Si / 2.No): ",[1,2],"valor predeterminado",True,"funcionalidad1")
        

        

    
    def funcionalidad2():
        label_nombre.config(text="Venta por encargo",borderwidth=2,relief="solid")
        label_descripción.config(text=("Para definir ventas por encargo, se debe tener en cuenta que una venta por encargo es creada por el administrado"
                                 +"\n segun una peticion previa del cliente , los productos serán encargados a bodega y los asignará a un envio especifico"),borderwidth=2,relief="solid")
        FieldFrame("¿Estas listo para realizar una venta por encargo? (1.Si / 2.No): ",[1,2],"valor predeterminado",True,"funcionalidad2")

        
    
    def funcionalidad3():
        label_nombre.config(text="Cambiar lista de producción diaría",borderwidth=2,relief="solid")
        label_descripción.config(text=( "permite al administrador actualizar la producción diaria de productos. Tras ingresar la cantidad deseada,"+
                                       "\n se verifica si la bodega tiene espacio suficiente. Se ajustan los requerimientos de producción y precios,"+
                                       "\n luego se inicia una tanda de producción identificada por un código. Si hay espacio, se añaden los productos."+
                                       "\n Si la bodega está llena, se detiene la producción y se sugiere enviarlos a otra bodega con capacidad."+
                                       "\n Esto asegura que la producción se ajuste al espacio disponible y evita interrupciones."),borderwidth=2,relief="solid")
        label_informacion.config(text="La encargada de esta funcionalidad tuvo problemas familiares, por favor tener consideración",borderwidth=2,relief="solid")
    
    def funcionalidad4():
        label_nombre.config(text="Agregar producto",borderwidth=2,relief="solid")
        label_descripción.config(text=( "La opción permite agregar ingredientes, elegir ingredientes existentes, y crear un nuevo producto con ellos."+
                                       "\n Si se agregan ingredientes nuevos, se detalla su información; luego se eligen y cuantifican al menos 2 ingredientes existentes."+
                                       "\n Tras esta selección, se define el nuevo producto con su información detallada."),borderwidth=2,relief="solid")
        label_informacion.config(text="Estos son los ingredientes disponibles:\n"+Ingrediente.obtener_lista_ingredientes(),borderwidth=2,relief="solid")
        FieldFrame("Tu producto va a necesitar un ingrediente que no esté en la lista? (1.Si / 2.No):",[1,2],"valor predeterminado",True,"funcionalidad4")
        
    def funcionalidad5():
        label_nombre.config(text="Eliminar producto",borderwidth=2,relief="solid")
        label_descripción.config(text=( "La máquina muestra los productos disponibles con sus detalles. El cliente escribe el nombre del producto a eliminar y confirma la acción."+
                                       "\n ¨¨No¨¨ cancela la solicitud, mientras que ¨¨Sí¨¨ elimina el producto."+
                                       "\n Si el nombre numero no coincide, se muestra un mensaje de error y "
                                       "finaliza el proceso de eliminación del producto."),borderwidth=2,relief="solid")
        label_informacion.config(text="Estos son los productos disponibles:\n"+administrador.bodega.mostrar_productos(),borderwidth=2,relief="solid")
        FieldFrame("Por favor, escriba el numero del producto que desea eliminar: ",list(range(1, len(administrador.bodega.productos) + 1)),"valor predeterminado",True,"funcionalidad5")
    def funcionalidad6():
        label_nombre.config(text="Asignar envio y/o camion",borderwidth=2,relief="solid")
        label_descripción.config(text=( "El administrador asigna un envío a un camión disponible verificando su capacidad."+
                                       "\n Se muestran envíos pendientes y camiones con espacio suficiente."+
                                       "\n Tras elegir un camión, se reduce su capacidad según el envío asignado, dejando espacio"+
                                       "\n adicional si se decide no ocupar todo. El camión se despacha y el envío se elimina de la lista."),borderwidth=2,relief="solid")
        label_informacion.config(text="Estos son los envios pendientes por asignación:\n"+Envio.envios_por_asignar(),borderwidth=2,relief="solid")                   
        FieldFrame("Seleccione el número del envío que desea asignar a un camión:",list(range(1, len(Envio.lista_envios_no_asignados) + 1)),"valor predeterminado",True,"funcionalidad6")
        
    def funcionalidad7():
        label_nombre.config(text="Cambiar la producción y/o ventas",borderwidth=2,relief="solid")
        label_descripción.config(text=( "El administrador visualiza la producción y puede ajustar precios y producción de productos."+
                                       "\n Puede reducir un 50% el precio de un artículo menos vendido y modificar la producción en un 15% menos si tiene baja venta o un 30% menos si tiene alta venta,"+
                                       "\n basado en su historial. Estos cambios se reflejan en la base de datos al confirmar la modificación."),borderwidth=2,relief="solid")
        label_informacion.config(text="Cambia automaticamente el nivel de produccion en base a las ventas de un producto\n y/o el precio de un producto en base a los dias que lleva en bodega",
                                 borderwidth=2,relief="solid")
        FieldFrame("¿Esta de acuerdo? 1. Si / 2. No",["1","2"],"valor predeterminado",True,"funcionalidad7")
        
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
    menu_procesos.add_command(label="funcionalidad 1",command=funcionalidad1)
    menu_procesos.add_command(label="funcionalidad 2",command=funcionalidad2)
    menu_procesos.add_command(label="funcionalidad 3",command=funcionalidad3)
    menu_procesos.add_command(label="funcionalidad 4",command=funcionalidad4)
    menu_procesos.add_command(label="funcionalidad 5",command=funcionalidad5)
    menu_procesos.add_command(label="funcionalidad 6",command=funcionalidad6)
    menu_procesos.add_command(label="funcionalidad 7",command=funcionalidad7)
    
    
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
foto_inicio1 = ImageTk.PhotoImage(Image.open("assets/foto_inicio1.png").resize((250, 100)))
foto_inicio2 = ImageTk.PhotoImage(Image.open("assets/foto_inicio2.png").resize((ancho_inicio, alto_inicio)))
foto_inicio3 = ImageTk.PhotoImage(Image.open("assets/foto_inicio3.png").resize((ancho_inicio, alto_inicio)))
foto_inicio4 = ImageTk.PhotoImage(Image.open("assets/foto_inicio4.png").resize((ancho_inicio, alto_inicio)))
foto_inicio5 = ImageTk.PhotoImage(Image.open("assets/foto_inicio5.png").resize((ancho_inicio, alto_inicio)))

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
def volver_a_aparecer(event): 
    label_inicio1.place(relx=0.1, rely=0.3)
    mensaje.config(text="")
#Cuando entre a la imagen haga un cambio
frame_inicio.bind("<Enter>", mostrar_mensaje)
frame_inicio.bind("<Leave>", volver_a_aparecer)

label_inicio1.place(relx=0.1, rely=0.3)
label_inicio2.place(relx=0, rely=0)
label_inicio3.place(relx=0.8, rely=0)
label_inicio4.place(relx=0.3, rely=0)
label_inicio5.place(relx=0.5, rely=0)

# Imágenes de Manuel
foto_manuel1 = Image.open("assets/foto1_manuel.png")
foto_manuel2 = Image.open("assets/foto2_manuel.png")
foto_manuel3 = Image.open("assets/foto3_manuel.png")
foto_manuel4 = Image.open("assets/foto4_manuel.png")

# Imagenes Juan

foto_juan1 = Image.open("assets/foto1_juan.png")
foto_juan2 = Image.open("assets/foto2_juan.png")
foto_juan3 = Image.open("assets/foto3_juan.png")
foto_juan4 = Image.open("assets/foto4_juan.png")

#Imagenes Andres

foto_andres1 = Image.open("assets/foto1_andres.png")
foto_andres2 = Image.open("assets/foto2_andres.png")
foto_andres3 = Image.open("assets/foto3_andres.png")
foto_andres4 = Image.open("assets/foto4_andres.png")

#Imagenes Maria
foto_maria1 = Image.open("assets/foto1_maria.png")
foto_maria2 = Image.open("assets/foto2_maria.png")
foto_maria3 = Image.open("assets/foto3_maria.png")
foto_maria4 = Image.open("assets/foto4_maria.png")

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
    frame_biografias.bind("<Button-1>", lambda event: cambiar_biografia())
    

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
    seccion.bind("<Button-1>", lambda event: cambiar_biografia())

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

