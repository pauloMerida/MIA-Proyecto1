import os
import shutil
from bitacora import *

ArregloParaBitacora = []

def EjecutarComandos(tabla):

    for i in tabla:
        if i.get("comando") == "configure":
            if i.get("type") == "local":
                    local(tabla,"local")
            elif i.get("type") == "cloud":
                    nube(tabla,"cloud")
            else:
                print("error",)

def local(tabla,modo):
    index = 1
    for i in tabla:
        comando = i.get("comando")
        ruta = "/Users/admin/Downloads/Archivos"

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
                    if os.path.exists(ruta+i.get("to")+nombre_archivo):
                        nombre = nombre_archivo.split(".")
                        with open(ruta+i.get("from"), "r") as archivo_origen:
                            contenido = archivo_origen.read()
                        with open(ruta+i.get("to+")+"/"+nombre[0]+str(index)+"."+nombre[1], "w") as archivo_destino:
                            archivo_destino.write(contenido)
                        os.remove(ruta + i.get("from"))
                    else:
                        shutil.move(ruta+i.get("from"), ruta+i.get("to"))
                else:
                    # hay que poner el error en la bitacora
                    print("La ruta no se refiere a un archivo.")
            else:
                # hay que poner el error en la bitacora
                print("La ruta no se refiere a un archivo.")

        elif comando == "rename":
                directorio_padre = os.path.dirname(i.get("path"))
                if os.path.exists(ruta + i.get("path")):
                    if os.path.exists(ruta + directorio_padre + i.get("name")):
                        # hay que poner el error en la bitacora
                        print("La ruta no se refiere a un archivo.")
                    else:
                        os.rename(ruta + i.get("path"), i.get("name"))
                else:
                    # hay que poner el error en la bitacora
                    print("La ruta no se refiere a un archivo.")

        elif comando == "modify":
            if os.path.exists(ruta + i.get("path")):
                f = open(ruta + i.get("path"), "w")
                f.write(i.get("body"))
                f.close()
            else:
                # hay que poner el error en la bitacora
                print("La ruta no se refiere a un archivo.")

        elif comando == "add":
            if os.path.exists(ruta + i.get("path")):
                f = open(ruta + i.get("path"), "a")
                f.write(i.get("body"))
                f.close()
            else:
                # hay que poner el error en la bitacora
                print("La ruta no se refiere a un archivo.")

        elif comando == "backup":
            print("hola")


