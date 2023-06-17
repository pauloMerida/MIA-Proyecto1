from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.files import FileNotUploadedError
import os

directorio_credenciales ='credentials_module.json'

def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file']=directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales

def crear_archivo_texto(nombre_archivo,contenido,id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'title': nombre_archivo,\
                                       'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    archivo.SetContentString(contenido)
    archivo.Upload()
    

# SUBIR UN ARCHIVO A DRIVE
def subir_archivo(ruta_archivo,id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    archivo['title'] = ruta_archivo.split("/")[-1]
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()

# DESCARGAR UN ARCHIVO DE DRIVE POR ID
def bajar_archivo_por_id(id_drive,ruta_descarga):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_drive}) 
    nombre_archivo = archivo['title']
    archivo.GetContentFile(ruta_descarga + nombre_archivo)

# BUSCAR ARCHIVOS
def busca(query):
    resultado = []
    credenciales = login()
    # Archivos con el nombre 'mooncode': title = 'mooncode'
    # Archivos que contengan 'mooncode' y 'mooncoders': title contains 'mooncode' and title contains 'mooncoders'
    # Archivos que NO contengan 'mooncode': not title contains 'mooncode'
    # Archivos que contengan 'mooncode' dentro del archivo: fullText contains 'mooncode'
    # Archivos en el basurero: trashed=true
    # Archivos que se llamen 'mooncode' y no esten en el basurero: title = 'mooncode' and trashed = false
    lista_archivos = credenciales.ListFile({'q': query}).GetList()
    for f in lista_archivos:
        # ID Drive
        print('ID Drive:',f['id'])
        id_archivo='ID Drive:',f['id']
        # Link de visualizacion embebido
        print('Link de visualizacion embebido:',f['embedLink'])
        # Link de descarga
        print('Link de descarga:',f['downloadUrl'])
        # Nombre del archivo
        print('Nombre del archivo:',f['title'])
        # Tipo de archivo
        print('Tipo de archivo:',f['mimeType'])
        # Esta en el basurero
        print('Esta en el basurero:',f['labels']['trashed'])
        # Fecha de creacion
        print('Fecha de creacion:',f['createdDate'])
        # Fecha de ultima modificacion
        print('Fecha de ultima modificacion:',f['modifiedDate'])
        # Version
        print('Version:',f['version'])
        # Tamanio
        print('Tamanio:',f['fileSize'])
        resultado.append(f)
    
    return id_archivo

#BUSCAR ARCHIVOS DE UNA CARPETA EN ESPECIFICO
def buscar_archivos_en_carpeta(id_folder,file_name):
    credenciales = login()
    file_list = credenciales.ListFile({'q': "'{}' in parents and trashed=false".format(id_folder)}).GetList()

    for file in file_list:
        if file['title']==file_name:            
            id_file=file['id']
    
    return id_file
        
#ELIMINAR ARCHIVO MEDIANTE EL ID
def eliminar_archvivo_por_id(file_id):
    credenciales = login()
    credenciales.CreateFile({'id': file_id}).Delete()

#COPIAR ARCHIVO 
def copiar_archivo(id_archivo, id_carpeta_destino,id_origen):
    credenciales = login()
 
#COPIAR CARPETA
def copiar_carpeta(id_carpeta, id_carpeta_destino):
    credenciales = login()
    # Crear objeto de archivo y configurar identificación y carpeta destino
    file = credenciales.CreateFile({'id': id_carpeta})

    # Copiar la carpeta en la carpeta destino
    copied_file = credenciales.CreateFile({'title': file['title'],'mimeType': 'application/vnd.google-apps.folder', 'parents': [{'id': id_carpeta_destino}]})
    copied_file.metadata_update = {'copyRequiresWriterPermission': True}
    copied_file.Upload()

def copy_folder(source_folder_id, destination_folder_id):
    try:
        credenciales = login()
        source_folder = credenciales.CreateFile({'id': source_folder_id})
        source_folder.FetchMetadata(fields='title')
        
        copied_folder = credenciales.CreateFile({
            'title': source_folder['title'],
            'parents': [{'id': destination_folder_id}],
            'mimeType': 'application/vnd.google-apps.folder'
        })
        copied_folder.Upload()
        
        # Copiar los archivos y subcarpetas de la carpeta
        file_list = credenciales.ListFile({'q': f"'{source_folder_id}' in parents and trashed=false"}).GetList()
        for file in file_list:
            if file['mimeType'] == 'application/vnd.google-apps.folder':
                copy_folder(file['id'], copied_folder['id'])
            else:
                copied_file = credenciales.CreateFile({'title': file['title'], 'parents': [{'id': copied_folder['id']}]})
                contenido = file.GetContentString()
                copied_file.SetContentString(contenido)
                copied_file.Upload()
                '''archivo = credenciales.CreateFile({'title': nombre_archivo,\
                                       'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
                     archivo.SetContentString(contenido)'''
    except:
        pass
#ELIMINAR CARPETA MEDIANTE EL ID
def eliminar_carpeta_por_id(folder_id):
    credenciales = login()
    credenciales.CreateFile({'id': folder_id}).Delete()

# DESCARGAR UN ARCHIVO DE DRIVE POR NOMBRE
def bajar_acrchivo_por_nombre(nombre_archivo,ruta_descarga):
    credenciales = login()
    lista_archivos = credenciales.ListFile({'q': "title = '" + nombre_archivo + "'"}).GetList()
    if not lista_archivos:
        print('No se encontro el archivo: ' + nombre_archivo)
    archivo = credenciales.CreateFile({'id': lista_archivos[0]['id']}) 
    archivo.GetContentFile(ruta_descarga + nombre_archivo)

# BORRAR/RECUPERAR ARCHIVOS
def borrar_recuperar(id_archivo):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_archivo})
    # MOVER A BASURERO
    archivo.Trash()
    # SACAR DE BASURERO
    #archivo.UnTrash()
    # ELIMINAR PERMANENTEMENTE
    #archivo.Delete()

# CREAR CARPETA
def crear_carpeta(nombre_carpeta,id_folder):
    credenciales = login()
    folder = credenciales.CreateFile({'title': nombre_carpeta, 
                               'mimeType': 'application/vnd.google-apps.folder',
                               'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    folder.Upload()

# MOVER ARCHIVO
def mover_archivo(id_archivo,id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_archivo})
    propiedades_ocultas = archivo['parents']
    archivo['parents'] = [{'isRoot': False, 
                           'kind': 'drive#parentReference', 
                           'id': id_folder, 
                           'selfLink': 'https://www.googleapis.com/drive/v2/files/' + id_archivo + '/parents/' + id_folder,
                           'parentLink': 'https://www.googleapis.com/drive/v2/files/' + id_folder}]
    archivo.Upload(param={'supportsTeamDrives': True})

raiz=False
def subir_back(folder_path, parent_id='1dtR7fv-l9Bn-XWAwSuC--CO7VSaYxFyo'):
    try:

        credenciales = login()
        folder_name = os.path.basename(folder_path)
        folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
        if folder_name!="Archivos":
            if parent_id:
                folder_metadata['parents'] = [{'id': parent_id}]
            folder = credenciales.CreateFile(folder_metadata)
            folder.Upload()            

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):               

                if folder_name!="Archivos":
                    file_metadata = {'title': file_name, 'parents': [{'id': folder['id'] }]}
                else:
                    file_metadata = {'title': file_name, 'parents': [{'id': '1dtR7fv-l9Bn-XWAwSuC--CO7VSaYxFyo' }]}
                file = credenciales.CreateFile(file_metadata)
                file.SetContentFile(file_path)
                file.Upload()
                
            elif os.path.isdir(file_path):
                if folder_name!="Archivos":
                    subir_back(file_path, parent_id=folder['id'])
                else:
                    subir_back(file_path, parent_id='1dtR7fv-l9Bn-XWAwSuC--CO7VSaYxFyo')
    except:
        print("paso algo")

def busca_carpeta(ruta_carpeta):
    credenciales=login()

    try:
        segmentos = ruta_carpeta.split("/")
        carpeta_padre = "root"
        for segmento in segmentos:
            if segmento != "":
                query = f"'{carpeta_padre}' in parents and title = '{segmento}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
                archivo = credenciales.ListFile({'q': query}).GetList()[0]
                carpeta_padre = archivo['id']

        if carpeta_padre=="root":
            return "no"
        else:
            return carpeta_padre
    except:
        return "error"

def verificar_archivos_carpetas_repetidas(folder_id,name):
    credenciales=login()
    file_list = credenciales.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    list=[]
    parametro=False
    for file in file_list:       
        if name==file['title']:
            parametro=True        
    return parametro

def renombrar(file_id,new_name):
    credenciales=login()   
    file = credenciales.CreateFile({'id': file_id})
    file.FetchMetadata()
    # Cambiar el nombre del archivo
    file['title'] = new_name
    file.Upload()
if __name__ == "__main__":
    ruta_archivo = '/home/falv/Escritorio/fondo.jpg'
    id_folder = '1dtR7fv-l9Bn-XWAwSuC--CO7VSaYxFyo'
    id_drive = '1JWQD7oEImq9xwMoqKCxbSDy90o-3iplF'
    ruta_descarga = 'C:/Users/Paulo/Downloads/T1_202002042.pdf'
    #C:\Users\Paulo\Desktop
    #C:\Users\Paulo\Downloads
    #crear_archivo_texto('nuevo.txt','dia 15 a ver si sirve',id_folder)
    #subir_archivo(ruta_descarga,id_folder)
    #bajar_archivo_por_id(id_drive,ruta_descarga)
    #busca("title = 'mooncode.png'")
    #bajar_acrchivo_por_nombre('WhatsApp Image 2020-11-01 at 9.55.34 PM (1).jpeg',ruta_descarga)
    #borrar_recuperar('1lHBMFjdyKfAYRa4M57biDZCiDwFhAYTy')
    #crear_carpeta('hola_folder',id_folder)
    #mover_archivo('1PmdkaivVUZKkDwFapSWrXNf6n6pO_YK-','1uSMaBaoLOt7F7VJiCZkrO4ckvj6ANecQ')