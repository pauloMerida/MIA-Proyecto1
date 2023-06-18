import os
import shutil
from BitacoraAcciones import *
from analizador import *
from encriptacion import *

ArregloParaBitacora = []

def EjecutarComandos(tabla):

    for i in tabla:
        if i.get("comando") == "configure":
            if i.get("type") == "local":
                    local(tabla,"local",i.get("encrypt_read"),i.get("encrypt_log"),i.get("llave"))
                    CrearArreglo(ArregloBitacora)
                    escribirBitacora(i.get("encrypt_log"),i.get("llave"))
                    ArregloBitacora.clear()

            elif i.get("type") == "cloud":
                    nube(tabla, "cloud", i.get("encrypt_read"), i.get("encrypt_log"), i.get("llave"))
                    CrearArreglo(ArregloBitacora)
                    escribirBitacora(i.get("encrypt_log"), i.get("llave"))
                    ArregloBitacora.clear()

            else:
                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR",
                             "Comando: configure | El parametro " + i.get("type") + " no existe."))

def local(tabla,modo,encriptado,bitacorae,llave):
    index = 1
    for i in tabla:
        comando = i.get("comando")
        ruta = "C:/Users/Paulo/Documents/Vacas Junio 2023/Lab archivos/Proyectos/Proyecto1/Archivos"

        if comando == "create":
            try:
                HF1 = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF1[1], HF1[0], "Entrada", "Comando: create | Creando: "+i.get("name")+" En ruta: "+ i.get("path")))

                os.makedirs(ruta+ i.get("path"),exist_ok=True)
                f = open( ruta + i.get("path") + i.get("name"),
                    "w")
                f.write(i.get("body"))
                f.close()

                HF2 = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF2[1], HF2[0], "Salida",
                             "Comando: create | " +i.get("name") + " creado exitosamente en ruta: " + i.get("path")))
            except:
                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR",
                             "Comando: create | " + i.get("name") + " no pudo ser creado en ruta: " + i.get("path")))
                print(error)

        elif comando == "delete":
            if "path" and "name" in i:
                HF1 = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF1[1], HF1[0], "Entrada",
                             "Comando: delete | Eliminando: " + i.get("name") + " de ruta: " + i.get("path")))

                try:
                    os.remove(ruta + i.get("path") + i.get("name"))
                    HF2 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF2[1], HF2[0], "Salida",
                                 "Comando: delete | " + i.get("name") + " eliminado exitosamente de ruta: " + i.get("path")))

                except OSError as error:
                    HF = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF[1], HF[0], "ERROR", "Comando: delete | " + i.get("name") + " no pudo ser eliminado de ruta: " + i.get("path")))
                    print(error)
            else:
                try:
                    os.chdir(ruta)
                    shutil.rmtree(i.get("path"))
                except OSError as error:
                    print(error)
                    print("No se eliminó la carpeta")

                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR", "Comando: delete | El parámetro name no esta incluido"))

        elif comando == "copy":
            if os.path.isfile(ruta+i.get("from")):
                HF1 = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF1[1], HF1[0], "Entrada",
                             "Comando: copy | Copiando: " + i.get("from") + " a ruta: " + i.get("to")))
                try:
                    shutil.copy(ruta+i.get("from"), ruta+i.get("to"))
                    HF2 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF2[1], HF2[0], "Salida",
                                 "Comando: copy | " + i.get("from") + " copiado exitosamente a ruta: " + i.get(
                                     "to")))

                except:
                    HF = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF[1], HF[0], "ERROR", "Comando: copy | La ruta " + i.get(
                            "from") + " no pudo copiarse a " + i.get("to")))

            elif  os.path.isdir(ruta+i.get("from")):
                HF1 = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF1[1], HF1[0], "Entrada",
                             "Comando: copy | Copiando: " + i.get("from") + " a ruta: " + i.get("to")))
                try:
                    shutil.copytree(ruta+i.get("from"), ruta+i.get("to"))
                    HF2 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF2[1], HF2[0], "Salida",
                                 "Comando: copy | " + i.get("from") + " copiado exitosamente a ruta: " + i.get(
                                     "to")))
                except FileExistsError:
                    try:
                        shutil.copytree(ruta+i.get("from"), os.path.join(ruta+i.get("to"), os.path.basename(ruta+i.get("from"))))
                        HF2 = HorayFecha()
                        ArregloParaBitacora.append(
                            bitacora(HF2[1], HF2[0], "Salida",
                                     "Comando: copy | " + i.get("from") + " copiado exitosamente a ruta: " + i.get(
                                         "to")))
                    except:
                        HF = HorayFecha()
                        ArregloParaBitacora.append(
                            bitacora(HF[1], HF[0], "ERROR", "Comando: copy | La ruta " + i.get(
                                "from") + " no pudo copiarse a " + i.get("to")))

            else:
                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR", "Comando: copy | La ruta "+i.get("from")+" no se refiere a un archivo o una carpeta."))


        elif comando == "transfer":

            nombre_archivo = os.path.basename(ruta+i.get("from"))

            if modo == i.get("mode"):
                if os.path.exists(ruta + i.get("from")):
                    HF1 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF1[1], HF1[0], "Entrada",
                                 "Comando: transfer | Moviendo: " + i.get("from") + " a ruta: " + i.get("to")))

                    if os.path.exists(ruta+i.get("to")+nombre_archivo):

                        try:
                            if os.path.isfile(ruta+i.get("from")):
                                nombre = nombre_archivo.split(".")
                                with open(ruta+i.get("from"), "r") as archivo_origen:
                                    contenido = archivo_origen.read()
                                with open(ruta+i.get("to+")+"/"+nombre[0]+str(index)+"."+nombre[1], "w") as archivo_destino:
                                    archivo_destino.write(contenido)
                                os.remove(ruta + i.get("from"))
                                index+=1

                                HF2 = HorayFecha()
                                ArregloParaBitacora.append(
                                    bitacora(HF2[1], HF2[0], "Salida",
                                             "Comando: transfer | " + i.get("from") + " movido exitosamente a ruta: " + i.get("to")))
                            elif os.path.isdir(ruta+i.get("from")):
                                if not os.path.exists(ruta+i.get("to")):
                                    os.makedirs(ruta+i.get("to"))


                                contenido_carpeta = os.listdir(ruta+i.get("from"))


                                for item in contenido_carpeta:
                                    ruta_item_origen = os.path.join(ruta+i.get("from"), item)
                                    ruta_item_destino = os.path.join(ruta+i.get("to"), item)
                                    shutil.move(ruta_item_origen, ruta_item_destino)

                        except:
                            HF = HorayFecha()
                            ArregloParaBitacora.append(bitacora(HF[1], HF[0], "ERROR",
                                                                "Comando: transfer | La ruta " + i.get(
                                                                    "from") + " no pudo moverse a "+i.get("to")))

                    else:
                        try:
                            shutil.move(ruta+i.get("from"), ruta+i.get("to"))
                            HF2 = HorayFecha()
                            ArregloParaBitacora.append(
                                bitacora(HF2[1], HF2[0], "Salida",
                                         "Comando: transfer | " + i.get("from") + " movido exitosamente a ruta: " + i.get("to")))
                        except:
                            HF = HorayFecha()
                            ArregloParaBitacora.append(bitacora(HF[1], HF[0], "ERROR",
                                                                "Comando: transfer | La ruta " + i.get(
                                                                    "from") + " no pudo moverse a " + i.get("to")))

                else:
                        HF = HorayFecha()
                        ArregloParaBitacora.append( bitacora(HF[1], HF[0], "ERROR", "Comando: transfer | La ruta " + i.get("from") + " no existe."))
            else:
                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR",
                             "Comando: transfer | El modo " + i.get("mode") + " debe ser igual al del comando configure."))

        elif comando == "rename":
                directorio_padre = os.path.dirname(i.get("path"))
                if os.path.exists(ruta + i.get("path")):
                    HF1 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF1[1], HF1[0], "Entrada",
                                 "Comando: rename | Renombrando: " + i.get("path") + " como: " + i.get("name")))

                    if os.path.exists(ruta + directorio_padre +"/"+ i.get("name")):
                        HF = HorayFecha()
                        ArregloParaBitacora.append(
                            bitacora(HF[1], HF[0], "ERROR",
                                     "Comando: rename | El archivo " + i.get("name") + " ya existe."))
                    else:
                        try:
                            carpeta = os.path.dirname(i.get("path"))
                            nueva_ruta_archivo = os.path.join(carpeta, i.get("name"))
                            os.rename(ruta + i.get("path"), ruta+nueva_ruta_archivo)
                            HF2 = HorayFecha()
                            ArregloParaBitacora.append(
                                bitacora(HF2[1], HF2[0], "Salida",
                                         "Comando: rename | " + i.get("path") + " renombrado exitosamente como " + i.get("name")))
                        except:
                            HF = HorayFecha()
                            ArregloParaBitacora.append(
                                bitacora(HF[1], HF[0], "ERROR",
                                         "Comando: rename | La ruta " + i.get("path") + " no pudo renonmbrase como: "+i.get("name")))

                else:
                    HF = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF[1], HF[0], "ERROR", "Comando: rename | La ruta " + i.get("path") + " no existe."))

        elif comando == "modify":

            if os.path.exists(ruta + i.get("path")):
                HF1 = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF1[1], HF1[0], "Entrada",
                             "Comando: modify | Modificando: " + i.get("path")))

                try:
                    f = open(ruta + i.get("path"), "w")
                    f.write(i.get("body"))
                    f.close()

                    HF2 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF2[1], HF2[0], "Salida",
                                 "Comando: modify | " + i.get("path") + " modificado exitosamente."))
                except:
                    HF = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF[1], HF[0], "ERROR", "Comando: modify | La ruta " + i.get("path") + " no pudo modificarse."))
            else:
                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR", "Comando: modify | La ruta " + i.get("path") + " no existe."))

        elif comando == "add":

            if os.path.exists(ruta + i.get("path")):
                HF1 = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF1[1], HF1[0], "Entrada",
                             "Comando: add | Agregando contenido a: " + i.get("path")))

                try:
                    f = open(ruta + i.get("path"), "a")
                    f.write(i.get("body"))
                    f.close()

                    HF2 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF2[1], HF2[0], "Salida",
                                 "Comando: add | Se agreago contenido a: " + i.get("path") + "  exitosamente."))
                except:
                    HF = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF[1], HF[0], "ERROR", "Comando: add | No se pudo agregar contenido a: " + i.get("path")))

            else:
                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR",
                             "Comando: add | La ruta " + i.get("path") + " no existe."))

        elif comando == "backup":
            print("hola")

        elif comando == "exec":
            HF1 = HorayFecha()
            ArregloParaBitacora.append(
                bitacora(HF1[1], HF1[0], "Entrada",
                         "Comando: exec | Leyendo y ejecutando: " + i.get("path")))
            try:
                CrearArreglo(ArregloBitacora)
                escribirBitacora(bitacorae,llave)
                ArregloBitacora.clear()

                if encriptado == "false":
                    f = open(ruta + i.get("path"), "r")
                    contenido = f.read()
                    f.close()

                    a = analizador()
                    a.analizar(contenido)

                    HF2 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF2[1], HF2[0], "Salida",
                                 "Comando: exec | Se leyo y ejecuto contenido de: " + i.get("path")))
                elif encriptado == "true":
                    f = open(ruta + i.get("path"), "r")
                    contenido = f.read()
                    f.close()

                    contenidodes = desencriptar_contraseña(contenido, llave)
                    a = analizador()
                    a.analizar(contenidodes)

                    HF2 = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF2[1], HF2[0], "Salida",
                                 "Comando: exec | Se leyo y ejecuto contenido de: " + i.get("path")))
                else:
                    HF = HorayFecha()
                    ArregloParaBitacora.append(
                        bitacora(HF[1], HF[0], "ERROR",
                                 "Comando: exec | El parametro para desencriptar " + encriptado + " no existe."))

            except:
                HF = HorayFecha()
                ArregloParaBitacora.append(
                    bitacora(HF[1], HF[0], "ERROR",
                             "Comando: exec | El archivo " + i.get("path") + " no pudo leerse."))


    CrearArreglo(ArregloParaBitacora)
    escribirBitacora(bitacorae, llave)
    ArregloBitacora.clear()

def nube(tabla,modo,encriptado,bitacorae,llave):

    print(llave)