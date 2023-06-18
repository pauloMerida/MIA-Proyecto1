import tkinter as tk

from tkinter import font
from tkinter import messagebox
from tkinter import ttk
from tkinter import messagebox
import shutil
import GoogleDrive as gd
import os,re
from analizador import analizador
#variables globales de los comandos
# comando configure 
configure_type="local"
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

#Funciones de comandos Local/Cloud tanto para interfaz grafica como para consola.

def funcion_create(create_name,create_body,create_path):
            global configure_type
            if configure_type=="local":
            
                if not os.path.exists(create_path):
                    # Crear la carpeta si no existe
                    os.makedirs(create_path)
                    
                archivo = open(create_path+create_name,'w')
                archivo.write(create_body)
                archivo.close
                messagebox.showinfo("Create", "Archivo creado exitosamente")
            elif configure_type=="cloud":
            
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

def funcion_delete(delete_path,delete_name):
        global configure_type
        if configure_type=="local":            
            if delete_name !="":
                delete_path+=delete_name 
            else:
                pass            
            if os.path.exists(delete_path) and delete_name!="":
                # Eliminar el archivo
                archivo=delete_path
                os.remove(archivo)
                messagebox.showinfo("Delete", "Archivo eliminado exitosamente")
            elif os.path.exists(delete_path) and delete_name=="":
                ruta_carpeta=delete_path[:-1]
                shutil.rmtree(ruta_carpeta)
                messagebox.showinfo("Delete", "Carpeta eliminada correctamente")
            elif not os.path.exists(delete_path):
                messagebox.showinfo("Delete", "Ruta incorrecta o no existe el archivo")
        else:            
            
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

def funcion_copy(copy_from,copy_to):
        global configure_type
        ruta_respaldo = 'C:/Users/Paulo/Documents/Vacas Junio 2023/Lab archivos/Proyectos/Proyecto1/Respaldo/'
        es_archivo=False
       
        resultados = re.findall(r'\b\w+\.txt\b', copy_from)  
        for resultado in resultados:            
            es_archivo=True
        if configure_type =="local":
                        
            if es_archivo==False:
                try:
                    if os.path.exists(copy_to) and os.path.exists(copy_from):
                        
                        shutil.copytree(copy_from,copy_to)
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
               
                id_origen=gd.busca_carpeta(copy_from) 
                id_destino=gd.busca_carpeta(copy_to) 
                if id_origen!="error" and id_destino!="error":
                    gd.copy_folder(id_origen,id_destino)
                    messagebox.showinfo("Copy", "Se copio correctamente la carpeta en la nube")
                else:
                    messagebox.showinfo("Copy", "La ruta es incorrecta") 

def funcion_transfer(transfer_from,transfer_to,transfer_mode):
            
        es_archivo=False
        resultados = re.findall(r'\b\w+\.txt\b', transfer_from)  
        for resultado in resultados:            
            es_archivo=True

        if transfer_mode =="Local":
            
            if es_archivo==False:
                if os.path.exists(transfer_from):
                    #extraer nombre de la carpeta
                    dividido=transfer_from.split("/")
                    nombre_carpeta=dividido[len(dividido)-2]
                    #si no existe la ruta destino la crea
                    if not os.path.exists(transfer_to):
                        os.makedirs(transfer_to)
                        
                    #listar contenido de la carpeta destino y verificar nombres
                    contenido_carpeta = os.listdir(transfer_to)
                    condicion=True
                    repetido=False
                    contador=0
                    if len(contenido_carpeta)>0:
                        while condicion:
                            for elemento in contenido_carpeta:
                                if elemento==nombre_carpeta:
                                    nombre_carpeta+="(c)" 
                                    repetido=True
                                    contador=0
                                contador+=1
                                if contador==len(contenido_carpeta)-1:
                                    condicion=False
                    else:
                        repetido=False
                    #renombrar si la carpeta esta repetida
                    if repetido==True:
                        ruta=transfer_from[:-1]
                        os.rename(ruta, os.path.join(os.path.dirname(ruta), nombre_carpeta))   
                    #mover a nueva ubicación
                    if repetido==False:
                        try:
                            ruta_origen=transfer_from[:-1]
                            ruta_destino=transfer_to[:-1]
                            shutil.move(ruta_origen, ruta_destino)
                            messagebox.showinfo("Transer", "Se movio la carpeta")
                        except:
                            messagebox.showinfo("Transer", "Ocurrio un error al mover la carpeta")
                    else:
                        dividido=transfer_from.split("/")
                        nombre_original=dividido[len(dividido)-2]
                        copia_ruta=transfer_from.replace(nombre_original,nombre_carpeta)
                        ruta_origen=copia_ruta[:-1]
                        ruta_destino=transfer_to[:-1]
                        shutil.move(ruta_origen, ruta_destino)
                        messagebox.showinfo("Transer", "Se movio la carpeta")
                        

                else:
                    messagebox.showinfo("Transer", "La ruta de origen no existe")
            elif es_archivo==True:
                
                #verificar si existe la ruta de origen
                if os.path.exists(transfer_from):
                    #extraer el nombre del archivo
                    dividido=transfer_from.split("/")
                    nombre_archivo=dividido[len(dividido)-1]
                    #si no existe la ruta destino la crea
                    if not os.path.exists(transfer_to):
                        os.makedirs(transfer_to)
                    
                    #listar contenido de la carpeta destino y verificar nombres
                    contenido_carpeta = os.listdir(transfer_to)
                    condicion=True
                    repetido=False
                    contador=0
                    if len(contenido_carpeta)>0:
                        while condicion:
                            for elemento in contenido_carpeta:
                                if elemento==nombre_archivo:
                                    aux=nombre_archivo.replace(".txt","")
                                    aux+="(c)"+".txt" 
                                    nombre_archivo=aux
                                    repetido=True
                                    contador=0
                                contador+=1
                                if contador==len(contenido_carpeta)-1:
                                    condicion=False
                    else:
                        repetido=False

                    #renombrar si el archivo esta repetido
                    if repetido==True:
                        
                        os.rename(transfer_from, os.path.join(os.path.dirname(transfer_from), nombre_archivo))   
                    #mover a nueva ubicación
                    if repetido==False:
                        try:
                            ruta_destino=transfer_to[:-1]
                            shutil.move(transfer_from, ruta_destino)
                            messagebox.showinfo("Transer", "Se movio el archivo")
                        except:
                            messagebox.showinfo("Transer", "Ocurrio un error al mover el archivo")
                    else:
                        dividido=transfer_from.split("/")
                        nombre_original=dividido[len(dividido)-1]
                        copia_ruta=transfer_from.replace(nombre_original,nombre_archivo)
                        ruta_destino=transfer_to[:-1]
                        shutil.move(copia_ruta, ruta_destino)
                        messagebox.showinfo("Transer", "Se movio el archivo")
                else:                    
                    messagebox.showinfo("Transer", "La ruta de origen no existe")
        
        else:
            if es_archivo==True:
                dividido=transfer_from.split('/')
                archivo= dividido[len(dividido)-1]
               
                ruta_total_from=transfer_from.replace(archivo,"")
                valido=gd.busca_carpeta(ruta_total_from) 

                #verifico la ruta de origen
                if valido!="error":  
                    try:
                        #obtengo el id de del archivo
                        id_file=gd.buscar_archivos_en_carpeta(valido,archivo)
                    except:
                        messagebox.showinfo("Transer", "Error en el nombre del txt o en la ruta") 
                else:
                    messagebox.showinfo("Transer", "ruta de origen incorrecta") 


                #verificar si la ruta destino existe
                id_destino=gd.busca_carpeta(transfer_to)
                if valido!="error" and id_destino=="error":
                    #como no existe la ruta destino pero si la de origen creo las carpetas
                    dividido=transfer_to.split("/")
                    ruta=""
                    for i in range(len(dividido)-1):
                        if dividido[i]!="Archivos":
                            
                            carpeta_actual=ruta
                            existe=gd.busca_carpeta(carpeta_actual)
                            if existe=="error":
                                #obtener ruta anterior
                                dividido2=carpeta_actual.split("/")
                                parametro=dividido2[len(dividido2)-2]
                                ruta_anterior= carpeta_actual.replace(parametro,"")
                                aux=ruta_anterior[:-1]
                                ruta_anterior=aux
                                existe=gd.busca_carpeta(ruta_anterior)
                                ruta_anterior+=parametro+'/'
                                ruta_anterior+=dividido[i+1]+'/'
                                ruta=ruta_anterior
                                #crear carpeta
                                gd.crear_carpeta(parametro,existe)
                            else:
                                ruta+=dividido[i+1]+'/'
                        elif dividido[i]=="Archivos":
                            ruta="Archivos"+'/'+dividido[i+1]+'/'

                #verificar nombres repetidos
                dividido=transfer_from.split("/")
                name=dividido[len(dividido)-1]
                id_destino=gd.busca_carpeta(transfer_to)
                repetido=gd.verificar_archivos_carpetas_repetidas(id_destino,name)
                if repetido==True:
                    condicion=True
                    while condicion:
                        aux=name.replace(".txt","")
                        aux+="(c)"+".txt"
                        name=aux
                        condicion=gd.verificar_archivos_carpetas_repetidas(id_destino,name)
                    #renombrar el archivo 
                    gd.renombrar(id_file,name)                    
                try:                        
                    #muevo el archivo
                    gd.mover_archivo(id_file,id_destino)
                    messagebox.showinfo("Transer", "archivo movido")  
                except:
                    messagebox.showinfo("Transer", "Error al mover el archivo, verificar ruta o nombre del txt")


            #es carpeta abajo procedimiento de carpeta
            else:
                
                #obtengo el nombre de la carpeta
                dividido=transfer_from.split("/")
                name_carpet=dividido[len(dividido)-2]
                #verifico rutas de origen y destino
                id_origen=gd.busca_carpeta(transfer_from) 
                id_destino=gd.busca_carpeta(transfer_to)

                if id_origen!="error" and id_destino=="error":
                    #como existe la ruta de origen y no la de destino procedo a crear la de destino
                    dividido=transfer_to.split("/")
                    ruta=""
                    for i in range(len(dividido)-1):
                        if dividido[i]!="Archivos":
                            
                            carpeta_actual=ruta
                            existe=gd.busca_carpeta(carpeta_actual)
                            if existe=="error":
                                #obtener ruta anterior
                                dividido2=carpeta_actual.split("/")
                                parametro=dividido2[len(dividido2)-2]
                                ruta_anterior= carpeta_actual.replace(parametro,"")
                                aux=ruta_anterior[:-1]
                                ruta_anterior=aux
                                existe=gd.busca_carpeta(ruta_anterior)
                                ruta_anterior+=parametro+'/'
                                ruta_anterior+=dividido[i+1]+'/'
                                ruta=ruta_anterior
                                #crear carpeta
                                gd.crear_carpeta(parametro,existe)
                            else:
                                ruta+=dividido[i+1]+'/'
                        elif dividido[i]=="Archivos":
                            ruta="Archivos"+'/'+dividido[i+1]+'/'
                elif id_origen=="error":
                    messagebox.showinfo("Transer", "ruta de origen incorrecta")
                #verificar nombres repetidos
                
                id_destino=gd.busca_carpeta(transfer_to)
                repetido=gd.verificar_archivos_carpetas_repetidas(id_destino,name_carpet)
                if repetido==True:
                    condicion=True
                    while condicion:                        
                        name_carpet+="(c)"
                        condicion=gd.verificar_archivos_carpetas_repetidas(id_destino,name_carpet)
                    #renombrar la carpeta si esta repetido 
                    gd.renombrar(id_origen,name_carpet)                    
                try:                        
                    #muevo el archivo
                    gd.mover_archivo(id_origen,id_destino)
                    messagebox.showinfo("Transer", "carpeta movida")  
                except:
                    messagebox.showinfo("Transer", "Error al mover la carpeta, verificar ruta")
        
def funcion_rename(rename_path,rename_name):
        global configure_type
        if configure_type=="local":

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
        #codigo para cloud
        else:
            #determinar si es archivo o carpeta
            es_archivo=False            
            file_name=""
            carpet_name=""
            ruta_total=""
            resultados = re.findall(r'\b\w+\.txt\b', rename_path)  
            for resultado in resultados:            
                es_archivo=True
            
            #obtener nombre de la carpeta o del archivo
            if es_archivo==True:

                dividido=rename_path.split("/")
                file_name=dividido[len(dividido)-1]                
                ruta_total=rename_path.replace(file_name,"")
                verificar=gd.busca_carpeta(ruta_total)
            else:
                dividido=rename_path.split("/")
                carpet_name=dividido[len(dividido)-2]                
                verificar=gd.busca_carpeta(rename_path)            

             #verificar si la ruta existe
            if verificar!="error":
                #verificar si el nombre esta en uso tanto para archivos como para carpetas
                repetido=gd.verificar_archivos_carpetas_repetidas(verificar,rename_name)
                if repetido==False:
                    #el nombre no esta repetido entonces procedemos a renombrar
                    if es_archivo==True:
                        #renombramos el archivo
                        id_file=gd.buscar_archivos_en_carpeta(verificar,file_name)
                        gd.renombrar(id_file,rename_name)
                        messagebox.showinfo("Rename", "Archivo renombrado") 
                    else:
                        #renombramos la carpeta                        
                        gd.renombrar(verificar,rename_name)
                        messagebox.showinfo("Rename", "Carpeta renombrada") 
                    
                else:
                    messagebox.showinfo("Rename", "Error el nombre ya existe.")  
            else:                
                messagebox.showinfo("Rename", "Ruta incorrecta")

def funcion_modify(modify_path,modify_body):
        global configure_type
        
        if configure_type=="local":

            if os.path.exists(modify_path):
                with open(modify_path, "w") as archivo:
                    archivo.write(modify_body)
                messagebox.showinfo("Modify", "Cuerpo cambiado correctamente")
            else:
                messagebox.showinfo("Modify", "Error la ruta no existe")
        else:
            #codigo para la nube
            dividido=modify_path.split("/")
            file_name=dividido[len(dividido)-1]
            ruta_total=modify_path.replace(file_name,"")
            verificar=gd.busca_carpeta(ruta_total)

            #verificamos si existen las carpetas de la ruta
            if verificar!="error":
                #verificamos si el nombre mandado en la ruta existe en el directorio
                existe=gd.verificar_archivos_carpetas_repetidas(verificar,file_name)
                if existe==True:
                    #como existe tanto las carpetas como el nombre del archivo procedemos a modificar el archivo.
                    id_file=gd.buscar_archivos_en_carpeta(verificar,file_name)
                    gd.eliminar_archvivo_por_id(id_file)
                    gd.crear_archivo_texto(file_name,modify_body,verificar)
                    messagebox.showinfo("Modify", "Archivo modificado")
                else:
                   messagebox.showinfo("Modify", "EL nombre de la ruta es incorrecto") 
            else:
                messagebox.showinfo("Modify", "Error en la ruta")
    
def funcion_add(add_path,add_body):
        global configure_type
        if configure_type=="local":
            if os.path.exists(add_path):
                with open(add_path, "a") as archivo:
                    add_body="\n"+add_body
                    archivo.write(add_body)
                messagebox.showinfo("Add", "Cuerpo agregado correctamente")
            else:
                messagebox.showinfo("Add", "Error la ruta no existe")
        else:
             #codigo para la nube
            dividido=add_path.split("/")
            file_name=dividido[len(dividido)-1]
            ruta_total=add_path.replace(file_name,"")
            verificar=gd.busca_carpeta(ruta_total)

            #verificamos si existen las carpetas de la ruta
            if verificar!="error":
                #verificamos si el nombre mandado en la ruta existe en el directorio
                existe=gd.verificar_archivos_carpetas_repetidas(verificar,file_name)
                if existe==True:
                    #como existe tanto las carpetas como el nombre del archivo procedemos a agregar el nuevo contenido al archivo.
                    id_file=gd.buscar_archivos_en_carpeta(verificar,file_name)                    
                    gd.agregar_contenido_txt(id_file,add_body,file_name)
                    messagebox.showinfo("Add", "Contenido agregado")
                else:
                   messagebox.showinfo("Add", "EL nombre de la ruta es incorrecto") 
            else:
                messagebox.showinfo("Add", "Error en la ruta")

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
    
    #funcion enviar
    def enviar():
       
        global create_name,create_body,create_path,configure_type
        create_name=entrada.get()
        create_body=entrada2.get()
        create_path="Archivos"+entrada3.get()
        funcion_create(create_name,create_body,create_path)

    #boton
    boton_config = tk.Button(ventana_emergente,text="Enviar",cursor="hand2",command=enviar,font=("Arial",14,"bold"),background="#5DADE2")
    boton_config.place(x=250,y=340)  

def emergente_delete():
    global delete_path,delete_name,configure_type
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    def enviar():
        global delete_path,delete_name,configure_type
        delete_name=entrada3.get()
        delete_path="Archivos"+entrada.get()
        funcion_delete(delete_path,delete_name)

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
        global copy_from,copy_to,configure_type
        copy_to="Archivos"+entrada3.get()
        copy_from="Archivos"+entrada.get()
        funcion_copy(copy_from,copy_to)

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
        transfer_from="Archivos"+entrada.get()
        transfer_to="Archivos"+entrada3.get()
        funcion_transfer(transfer_from,transfer_to,transfer_mode)
                 
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
        global transfer_mode
        seleccion = cuadro_seleccion.get()
        transfer_mode=seleccion

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
    global rename_path,rename_name,configure_type
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)

    def enviar():
        global rename_path,rename_name,configure_type
        rename_path="Archivos"+entrada.get()
        rename_name=entrada3.get()
        funcion_rename(rename_path,rename_name)
        

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
    global modify_path,modify_body,configure_type

    def enviar():
        global modify_path,modify_body,configure_type
        modify_path="Archivos"+entrada.get()
        modify_body=entrada3.get()
        funcion_modify(modify_path,modify_body)
    
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
        global add_path,add_body,configure_type
        add_path="Archivos"+entrada.get()
        add_body=entrada3.get()
        funcion_add(add_path,add_body)
        


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
    global id_folder,configure_type
    if configure_type=="local":
        #hacer backup a la nube
        try:
            ruta_carpeta = 'C:/Users/Paulo/Documents/Vacas Junio 2023/Lab archivos/Proyectos/Proyecto1/Archivos'
            try:
                gd.subir_back(ruta_carpeta,id_folder)
                messagebox.showinfo("Drive", "Backup subido correctamente.")
            except:
                messagebox.showinfo("Drive", "Error al subir el backup")
        except:
            messagebox.showinfo("Drive", "error")
    else:
        try:
            ruta_carpeta = 'C:/Users/Paulo/Documents/Vacas Junio 2023/Lab archivos/Proyectos/Proyecto1/Archivos/'
            gd.decargar_backup(id_folder,ruta_carpeta)
            messagebox.showinfo("Drive", "Backup descargado correctamente.")
        except:
            messagebox.showinfo("Drive", "error")


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
boton_analizar.configure(command=lambda: Analizar_Codigo())

a = analizador()
def Analizar_Codigo():
    editado = area_consola.get(1.0, tk.END)
    analizador.analizar(editado)
    messagebox.showinfo('Resultados', '¡Los datos han sido analizados exitosamente!')

ventana.mainloop()