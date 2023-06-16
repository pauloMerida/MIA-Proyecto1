import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
from tkinter import messagebox
import shutil
import GoogleDrive as gd
import os,re
#variables globales de los comandos
# comando configure 
configure_type="cloud"
configure_log=False
configure_read=False
configure_key=""
#comando create
create_name=""
create_body=""
create_path=""
#comando delete
delete_path=""
delete_name=""
#comando copy
copy_from=""
copy_to=""
#comando transfer
transfer_from=""
transfer_to=""
transfer_mode="local"
#comando rename
rename_path=""
rename_name=""
#comando modify
modify_path=""
modify_body=""
#comando add
add_path=""
add_body=""
#comando exec
exec_path=""
#ID carpeta archivos Drive
id_folder = '1dtR7fv-l9Bn-XWAwSuC--CO7VSaYxFyo'
#ventana principal TKinter
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
    global configure_type,configure_log,configure_read,configure_key
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    #funcion enviar
    def enviar():
        global configure_key
        configure_key=entrada.get()
        messagebox.showinfo("Configure", "Sistema configurado")
        
        
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
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar, font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)

    def seleccionar_opcion(event):
        global configure_type
        seleccion = cuadro_seleccion.get()

        configure_type=seleccion
       
        

    # Crear el cuadro de selección
    opciones = ['local', 'cloud']
    cuadro_seleccion = ttk.Combobox(ventana_emergente, values=opciones,font=("Arial",14,"bold"))
    cuadro_seleccion.place(x=200,y=50)
    cuadro_seleccion.bind("<<ComboboxSelected>>", seleccionar_opcion)

    def seleccionar_opcion2(event):
        global configure_log
        seleccion = cuadro_seleccion2.get()
        configure_log=seleccion
      
        
        
    # Crear el cuadro de selección
    opciones2 = ['True', 'False']
    cuadro_seleccion2 = ttk.Combobox(ventana_emergente, values=opciones2,font=("Arial",14,"bold"))
    cuadro_seleccion2.place(x=200,y=130)
    cuadro_seleccion2.bind("<<ComboboxSelected>>", seleccionar_opcion2)

    def seleccionar_opcion3(event):
        global configure_read
        seleccion = cuadro_seleccion3.get()
        configure_read=seleccion
        
       
        
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
    #funcion respaldo
    def carpetas_drive():
        pass

    #funcion enviar
    def enviar():
        global configure_type
        global create_name,create_body,create_path
        if configure_type=="local":
            
            create_name=entrada.get()
            create_body=entrada2.get()
            create_path=entrada3.get()

            ruta_total="Archivos"+create_path
            if not os.path.exists(ruta_total):
                # Crear la carpeta si no existe
                os.makedirs(ruta_total)
                
            archivo = open(ruta_total+create_name,'w')
            archivo.write(create_body)
            archivo.close
            messagebox.showinfo("Create", "Archivo creado exitosamente")
        elif configure_type=="cloud":
            
            create_name=entrada.get()
            create_body=entrada2.get()
            create_path="Archivos"+entrada3.get()
            dividido=create_path.split("/")
            ruta_existe=False
            existe=gd.busca_carpeta(create_path)
            ruta_alternativa="Archivos/"
            if existe=="no":
                print("la ruta no existe2")
            elif existe=="error":
                id_actual=""
                for i in range(len(dividido)-1):
                    if i==0:
                        existe=gd.busca_carpeta("Archivos")
                    else:
                        existe=gd.busca_carpeta(ruta_alternativa+dividido[i]+'/')
                    if existe=="error":
                        gd.crear_carpeta(dividido[i],id_actual)
                        ruta_alternativa+=dividido[i]+'/'
                        id_actual=gd.busca_carpeta(ruta_alternativa)
                        
                    elif existe=="error" and i==0:                        
                        gd.crear_carpeta(dividido[i],id_folder)
                        ruta_alternativa+=dividido[i]+'/'
                        id_actual=gd.busca_carpeta(ruta_alternativa)
                        
                    else:
                        if i>0:
                            ruta_alternativa+=dividido[i]+'/'
                            id_actual=existe
                        elif i==0:
                            id_actual=existe
                        
            else:
                ruta_existe=True

            if ruta_existe==True:
                gd.crear_archivo_texto(create_name,create_body,existe)
                messagebox.showinfo("Create", "Archivo creado exitosamente")
                
            else:
                #crear carpeta y despues txt
                existe=gd.busca_carpeta(create_path)
                gd.crear_archivo_texto(create_name,create_body,existe)
                messagebox.showinfo("Create", "Archivo creado exitosamente")               
            
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar,font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)  

def emergente_delete():
    global delete_path,delete_name
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    def enviar():
        global delete_path,delete_name
        if configure_type=="local":
            delete_name=entrada3.get()
            delete_path=entrada.get()
            if delete_name !="":
                ruta_total= "Archivos"+delete_path+delete_name    
            else:
                ruta_total= "Archivos"+delete_path 
            if os.path.exists(ruta_total) and delete_name!="":
                # Eliminar el archivo
                archivo=ruta_total
                os.remove(archivo)
                messagebox.showinfo("Delete", "Archivo eliminado exitosamente")
            elif os.path.exists(ruta_total) and delete_name=="":
                ruta_carpeta=ruta_total[:-1]
                shutil.rmtree(ruta_carpeta)
                messagebox.showinfo("Delete", "Carpeta eliminada correctamente")
            elif not os.path.exists(ruta_total):
                messagebox.showinfo("Delete", "Ruta incorrecta o no existe el archivo")
        else:
            delete_name=entrada3.get()
            delete_path="Archivos"+entrada.get()
            
            id=gd.busca_carpeta(delete_path)
            
            if id=="error":
                messagebox.showinfo("Delete", "Ruta incorrecta o no existe el archivo")
            else:
                if delete_name!="":
                    id_file=  gd.buscar_archivos_en_carpeta(id,delete_name)
                    
            
            if delete_name!="" and id!="error":
                gd.eliminar_archvivo_por_id(id_file)
                messagebox.showinfo("Delete", "Archivo eliminado correctamente.")

            elif delete_name=="" and id!="error":
                gd.eliminar_carpeta_por_id(id)
                messagebox.showinfo("Delete", "Carpeta eliminada correctamente.")


            


    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("delete")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="name",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar, font=("Arial",14,"bold"),background="#5DADE2")
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
    #funcion enviar
    def enviar():
        global copy_from,copy_to
        ruta_respaldo = 'C:/Users/Paulo/Documents/Vacas Junio 2023/Lab archivos/Proyectos/Proyecto1/Respaldo/'
        es_archivo=False
        copy_from=entrada.get()
        ruta="Archivos"+copy_from
        copy_from=ruta
        resultados = re.findall(r'\b\w+\.txt\b', copy_from)  
        for resultado in resultados:            
            es_archivo=True
        if configure_type =="local":
            
                
            copy_to="Archivos"+entrada3.get()
            
            if es_archivo==False:
                try:
                    if os.path.exists(copy_to) and os.path.exists(copy_from):
                        
                        shutil.copytree(copy_from, copy_to,dirs_exist_ok=True)
                        messagebox.showinfo("Copy", "carpeta copiada correctamente")
                    else:
                        messagebox.showinfo("Copy", "La ruta no existe") 
                except:
                    messagebox.showinfo("Copy", "No se pudo copiar la carpeta")
            elif es_archivo==True:
                
                try:
                    if os.path.exists(copy_to) and os.path.exists(copy_from):                
                        shutil.copy2(copy_from, copy_to)
                        messagebox.showinfo("Copy", "archivo copiado correctamente")
                    else:
                        messagebox.showinfo("Copy", "La ruta no existe") 
                except:
                    messagebox.showinfo("Copy", "No se pudo copiar el archivo")
        else:
            copy_to="Archivos"+entrada3.get()
            if es_archivo==True:
                try:
                    existe_origen=False
                    existe_destino=False
                    dividido=copy_from.split("/")
                    parametro=dividido[len(dividido)-1]
                    ruta_carpeta=copy_from.replace(parametro,"")
                    id_folder=gd.busca_carpeta(ruta_carpeta) 
                    if id_folder!="error":
                        existe_origen=True
                    id_file=gd.buscar_archivos_en_carpeta(id_folder,parametro)                
                    id_destino=gd.busca_carpeta(copy_to) 
                    if id_destino!="error":
                        existe_destino=True

                    if existe_destino==True and existe_origen==True:      
                            
                        gd.bajar_archivo_por_id(id_file,ruta_respaldo)
                        gd.subir_archivo(ruta_respaldo+parametro,id_destino)
                        messagebox.showinfo("Copy", "Se copio correctamente el archivo en la nube")
                    else:
                        messagebox.showinfo("Copy", "Ruta erronea de la nube")
                except:
                   messagebox.showinfo("Copy", "Ruta erronea de la nube") 

            else:
                dividido=copy_from.split("/")
                parametro=dividido[len(dividido)-1]
                ruta_carpeta=copy_from.replace(parametro,"")
                id_origen=gd.busca_carpeta(ruta_carpeta) 
                id_destino=gd.busca_carpeta(copy_to) 
                gd.copy_folder(id_origen,id_destino)
                messagebox.showinfo("Copy", "Se copio correctamente la carpeta en la nube")

    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Copy")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="from",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="to",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar, font=("Arial",14,"bold"),background="#5DADE2")
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
    #funcion enviar
    def enviar():
        global transfer_from,transfer_to,transfer_mode
        es_archivo=False
        origen=[]
        destino=[]
        transfer_from="Archivos"+entrada.get()
        transfer_to="Archivos"+entrada3.get()
        
        resultados = re.findall(r'\b\w+\.txt\b', transfer_from)  
        for resultado in resultados:            
            es_archivo=True

        if es_archivo==False:
            try:
                if  os.path.exists(transfer_from):
                    # Renombrar archivos o carpetas con el mismo nombre en el destino
                    contenido = os.listdir(transfer_from)                   
                    for elemento in contenido:
                        origen.append(elemento)
                  
                    contenido = os.listdir(transfer_to)                  
                    for elemento in contenido:
                        destino.append(elemento)                    
                    encontro=False
                    contador=0
                    reiniciar=True
                    for i in range(0,len(origen)):
                        nombre_origen=origen[i]
                        while reiniciar:
                            contador+=1
                            for o in range(0,len(destino)):
                                
                                nombre_destino=destino[o]
                                if nombre_destino==nombre_origen:
                                    encontro=True
                                    nombre_base, extension = os.path.splitext(nombre_origen)
                                    nombre_origen=nombre_base+"(nuevo)"+extension 
                                    break
                            if contador==50:
                                reiniciar=False
                        if encontro==True:
                            original=origen[i]
                            #print("nombre original: "+original+" resultante: "+nombre_origen)
                            if original.endswith(".txt"):
                                ruta_archivo=transfer_from+original 
                                ruta_carpeta_actual = os.path.abspath(ruta_archivo) 
                                ruta_nueva_carpeta = os.path.join(os.path.dirname(ruta_carpeta_actual), nombre_origen)
                                os.rename(ruta_carpeta_actual, ruta_nueva_carpeta)                                                             
                                #print("ruta archivo"+ruta_archivo)
                                #print("se cambio el nombre del archivo")
                            else:

                                ruta=transfer_from+original 
                                ruta_carpeta_actual = os.path.abspath(ruta) 
                                ruta_nueva_carpeta = os.path.join(os.path.dirname(ruta_carpeta_actual), nombre_origen)
                                os.rename(ruta_carpeta_actual, ruta_nueva_carpeta)                             
                                #print("ruta carpeta: "+ruta)
                                #print("se cambio el nombre de la carpeta")
                        encontro=False
                        reiniciar=True
                        contador=0
                    shutil.copytree(transfer_from, transfer_to,dirs_exist_ok=True)                    
                    messagebox.showinfo("Transfer", "carpeta transferida correctamente")
                    shutil.rmtree(transfer_from)
                    origen.clear()
                    destino.clear()
                else:
                    messagebox.showinfo("Transfer", "La ruta no existe") 
            except:
                messagebox.showinfo("Transfer", "No se pudo transferir la carpeta")
        elif es_archivo==True:
           
            try:
                if os.path.exists(transfer_from) and os.path.exists(transfer_to):                
                    
                    repetido=False
                    contenido = os.listdir(transfer_to) 
                    
                    dividido=transfer_from.split('/')
                    archivo= dividido[len(dividido)-1]         
                    for elemento in contenido:
                        if elemento==archivo:
                            repetido=True
                        destino.append(elemento)                    
                    encontro=False
                    contador=0
                    reiniciar=True
                    if repetido==True:
                            while reiniciar:
                                contador+=1
                                for o in range(0,len(destino)):
                                    
                                    nombre_destino=destino[o]
                                    if nombre_destino==archivo:
                                        encontro=True
                                        nombre_base, extension = os.path.splitext(archivo)
                                        nombre_origen=nombre_base+"(nuevo)"+extension 
                                        break
                                if contador==50:
                                    reiniciar=False
                            if encontro==True:
                                    
                                    #print("nombre original: "+original+" resultante: "+nombre_origen)
                                    ruta_archivo=transfer_from
                                    ruta_carpeta_actual = os.path.abspath(ruta_archivo) 
                                    ruta_nueva_carpeta = os.path.join(os.path.dirname(ruta_carpeta_actual), nombre_origen)
                                    os.rename(ruta_carpeta_actual, ruta_nueva_carpeta)   
                                    transfer_from=transfer_from.replace(archivo,nombre_origen)   
                                    shutil.move(transfer_from, transfer_to)    
                                    print("TF"+transfer_from)                                                
                                
                            encontro=False
                            reiniciar=True
                            contador=0
                            origen.clear()
                            destino.clear()
                            messagebox.showinfo("Transfer", "archivo transferido correctamente(igual)")
                    else:
                        shutil.move(transfer_from, transfer_to) 
                        messagebox.showinfo("Transfer", "archivo transferido correctamente")
                    
                else:
                    messagebox.showinfo("Transfer", "La ruta no existe") 
            except:
                messagebox.showinfo("Transfer", "No se pudo transferir el archivo")

        
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
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar, font=("Arial",14,"bold"),background="#5DADE2")
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
    global rename_path,rename_name
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)

    def enviar():
        global rename_path,rename_name
        rename_path="Archivos"+entrada.get()
        rename_name=entrada3.get()
        if os.path.exists(rename_path):
            es_archivo=False
            repetido=False
            resultados = re.findall(r'\b\w+\.txt\b', rename_path)  
            for resultado in resultados:            
                es_archivo=True


            if es_archivo==False:
                dividido=rename_path.split('/')
                parametro=dividido[len(dividido)-1]
                nueva=rename_path.replace(parametro,"")    
                contenido = os.listdir(nueva)                  
                for elemento in contenido:
                    if elemento==rename_name:
                        repetido=True
            else:
                dividido=rename_path.split("/")
                parametro=dividido[len(dividido)-1]
                ruta=rename_path.replace(parametro,"")
                contenido = os.listdir(ruta)                  
                for elemento in contenido:
                    if elemento==rename_name:
                        repetido=True

            if es_archivo==False:
                if repetido==False:
                    ruta_carpeta_actual = os.path.abspath(rename_path)                    
                    ruta_nueva_carpeta = os.path.join(os.path.dirname(ruta_carpeta_actual),rename_name)
                    print("ruta_nueva_carpeta="+ruta_nueva_carpeta)
                    #print("ruta actual"+ruta_carpeta_actual+"**"+"ruta nueva carpeta"+ruta_nueva_carpeta)
                    os.rename(ruta_carpeta_actual, ruta_nueva_carpeta)
                    messagebox.showinfo("Rename", "carpeta renombrada correctamente")
                else:
                    messagebox.showinfo("Rename", "Error el nombre de la carpeta ya existe")
            elif es_archivo==True:
                if repetido==False:
                    ruta_carpeta_actual = os.path.abspath(rename_path)                    
                    ruta_nueva_carpeta = os.path.join(os.path.dirname(ruta_carpeta_actual),rename_name)
                    os.rename(ruta_carpeta_actual, ruta_nueva_carpeta)
                    messagebox.showinfo("Rename", "archivo renombrado correctamente")
                else:
                    messagebox.showinfo("Rename", "Error el nombre del archivo ya existe")
        else:
            messagebox.showinfo("Rename", "Ruta incorrecta")
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Rename")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="name",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar, font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)    

    #cuadro de entrada
    path = tk.StringVar() 

    entrada= tk.Entry(ventana_emergente,textvar=path,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada.place(x=200,y=50)

    name = tk.StringVar() 

    entrada3= tk.Entry(ventana_emergente,textvar=name,width=20, relief="flat",font=("Arial",14,"bold"))
    entrada3.place(x=200,y=130)

def emergente_modify():
    global modify_path,modify_body

    def enviar():
        global modify_path,modify_body
        modify_path="Archivos"+entrada.get()
        modify_body=entrada3.get()
        if os.path.exists(modify_path):
            with open(modify_path, "w") as archivo:
                archivo.write(modify_body)
            messagebox.showinfo("Modify", "Cuerpo cambiado correctamente")
        else:
            messagebox.showinfo("Modify", "Error la ruta no existe")

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
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar, font=("Arial",14,"bold"),background="#5DADE2")
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
    def enviar():
        global add_path,add_body
        add_path="Archivos"+entrada.get()
        add_body=entrada3.get()
        if os.path.exists(add_path):
            with open(add_path, "a") as archivo:
                add_body="\n"+add_body
                archivo.write(add_body)
            messagebox.showinfo("Add", "Cuerpo agregado correctamente")
        else:
            messagebox.showinfo("Add", "Error la ruta no existe")
    # Configurar propiedades de la ventana emergente
    ventana_emergente.title("Add")
    ventana_emergente.geometry("500x400")
    
    # Contenido de la ventana emergente
    label1 = tk.Label(ventana_emergente, text="path",font=("Arial",16,"bold"))
    label1.place(x=30,y=50)

    label2 = tk.Label(ventana_emergente, text="body",font=("Arial",16,"bold"))
    label2.place(x=30,y=130)
   
    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar, font=("Arial",14,"bold"),background="#5DADE2")
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

def backup():
    global id_folder
    if configure_type=="local":
        #hacer backup a la nube
        try:
            ruta_carpeta = 'C:/Users/Paulo/Documents/Vacas Junio 2023/Lab archivos/Proyectos/Proyecto1/Archivos'
            gd.subir_back(ruta_carpeta,id_folder)
            messagebox.showinfo("Drive", "correcto")
        except:
            messagebox.showinfo("Drive", "error")
    else:
        print("haciendo back de nuve a local")

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

boton_back = tk.Button(ventana,text="Backup",cursor="hand2",command=backup, font=("Arial",14,"bold"),background="#5DADE2")
boton_back.place(x=800,y=320)

boton_exec = tk.Button(ventana,text="Exec",cursor="hand2",command=emergente_exec, font=("Arial",14,"bold"),background="#5DADE2")
boton_exec.place(x=1000,y=320)

boton_sesion = tk.Button(ventana,text="Cerrar sesion",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_sesion.place(x=800,y=380)

boton_analizar = tk.Button(ventana,text="Analizar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_analizar.place(x=600,y=635)



ventana.mainloop()