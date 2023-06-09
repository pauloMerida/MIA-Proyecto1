import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Consola")
ventana.geometry("1200x700+500+50")
ventana.resizable(width=False,height=False)

#labels
lconsol = tk.Label(ventana,text="Consola:",font=("Arial",18,"bold"))
lconsol.place(x=30,y=40)

#text Area

area_consola = tk.Text(ventana,width=55, height=22)
nueva_fuente = font.Font(size=16)
area_consola.configure(font=nueva_fuente)
area_consola.place(x=30,y=90)



#ventanas emergentes
def emergente_configure():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Configure")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="Type",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="Encrypt_log",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)

    label3 = tk.Label(ventana_emergente, text="Encrypt_reada",font=("Arial",16,"bold"))
    label3.place(x=30,y=210)

    label4 = tk.Label(ventana_emergente, text="llave",font=("Arial",16,"bold"))
    label4.place(x=30,y=290)
    
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)

    def seleccionar_opcion(event):
        seleccion = cuadro_seleccion.get()
        print(f"Opción seleccionada: {seleccion}")

    # Crear el cuadro de selección
    opciones = ['Local', 'Cloud']
    cuadro_seleccion = ttk.Combobox(ventana_emergente, values=opciones,font=("Arial",14,"bold"))
    cuadro_seleccion.place(x=200,y=50)
    cuadro_seleccion.bind("<<ComboboxSelected>>", seleccionar_opcion)

    def seleccionar_opcion2(event):
        seleccion = cuadro_seleccion2.get()
        print(f"Opción seleccionada: {seleccion}")
        
    # Crear el cuadro de selección
    opciones2 = ['True', 'False']
    cuadro_seleccion2 = ttk.Combobox(ventana_emergente, values=opciones2,font=("Arial",14,"bold"))
    cuadro_seleccion2.place(x=200,y=130)
    cuadro_seleccion2.bind("<<ComboboxSelected>>", seleccionar_opcion2)

    def seleccionar_opcion3(event):
        seleccion = cuadro_seleccion3.get()
        print(f"Opción seleccionada: {seleccion}")
        
    # Crear el cuadro de selección
    opciones3 = ['True', 'False']
    cuadro_seleccion3 = ttk.Combobox(ventana_emergente, values=opciones3,font=("Arial",14,"bold"))
    cuadro_seleccion3.place(x=200,y=210)
    cuadro_seleccion3.bind("<<ComboboxSelected>>", seleccionar_opcion3)

    #cuadro de entrada
    llave = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=llave,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=290)

def emergente_create():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Create")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="Name",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="Body",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)

    label3 = tk.Label(ventana_emergente, text="Path",font=("Arial",16,"bold"))
    label3.place(x=30,y=210)    
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    name = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=name,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    body = tk.StringVar() 

    entrada2= tk.Entry(ventana_emergente,textvar=body,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada2.place(x=200,y=130)

    path = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=path,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=210)

def emergente_delete():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("delete")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="name",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    name = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=name,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    path = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=path,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=130)

def emergente_copy():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Copy")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="from",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="to",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    fromm = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=fromm,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    to = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=to,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=130)

def emergente_transfer():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Transfer")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="from",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="to",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)

    label3 = tk.Label(ventana_emergente, text="mode",font=("Arial",16,"bold"))
    label3.place(x=30,y=210)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    def seleccionar_opcion(event):
        seleccion = cuadro_seleccion.get()
        print(f"Opción seleccionada: {seleccion}")

    # Crear el cuadro de selección
    opciones = ['Local', 'Cloud']
    cuadro_seleccion = ttk.Combobox(ventana_emergente, values=opciones,font=("Arial",14,"bold"))
    cuadro_seleccion.place(x=200,y=210)
    cuadro_seleccion.bind("<<ComboboxSelected>>", seleccionar_opcion)

    #cuadro de entrada
    fromm = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=fromm,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    to = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=to,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=130)

def emergente_rename():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Rename")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="name",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    path = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=path,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    name = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=name,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=130)

def emergente_modify():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("modify")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="body",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    path = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=path,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    body = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=body,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=130)

def emergente_add():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Add")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="body",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    path = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=path,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    body = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=body,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=130)

def emergente_exec():
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Exec")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    path = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=path,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

#botones
boton_config = tk.Button(ventana,text="Configure",cursor="hand2",command=emergente_configure, font=("Arial",14,"bold"),background="#5DADE2")
boton_config.place(x=800,y=90)

boton_transfer = tk.Button(ventana,text="Transfer",cursor="hand2",command=emergente_transfer, font=("Arial",14,"bold"),background="#5DADE2")
boton_transfer.place(x=1000,y=90)

boton_create = tk.Button(ventana,text="Create",cursor="hand2",command=emergente_create, font=("Arial",14,"bold"),background="#5DADE2")
boton_create.place(x=800,y=150)

boton_rename = tk.Button(ventana,text="Rename",cursor="hand2",command=emergente_rename, font=("Arial",14,"bold"),background="#5DADE2")
boton_rename.place(x=1000,y=150)

boton_delete = tk.Button(ventana,text="Delete",cursor="hand2", command=emergente_delete, font=("Arial",14,"bold"),background="#5DADE2")
boton_delete.place(x=800,y=210)

boton_modify = tk.Button(ventana,text="Modify",cursor="hand2",command=emergente_modify, font=("Arial",14,"bold"),background="#5DADE2")
boton_modify.place(x=1000,y=210)

boton_copy = tk.Button(ventana,text="Copy",cursor="hand2",command=emergente_copy, font=("Arial",14,"bold"),background="#5DADE2")
boton_copy.place(x=800,y=270)

boton_add = tk.Button(ventana,text="Add",cursor="hand2",command=emergente_add, font=("Arial",14,"bold"),background="#5DADE2")
boton_add.place(x=1000,y=270)

boton_back = tk.Button(ventana,text="Backup",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_back.place(x=800,y=320)

boton_exec = tk.Button(ventana,text="Exec",cursor="hand2",command=emergente_exec, font=("Arial",14,"bold"),background="#5DADE2")
boton_exec.place(x=1000,y=320)

boton_sesion = tk.Button(ventana,text="Cerrar sesion",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_sesion.place(x=800,y=380)

boton_analizar = tk.Button(ventana,text="Analizar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_analizar.place(x=600,y=635)



ventana.mainloop()