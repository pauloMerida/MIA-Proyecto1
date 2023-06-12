import os
import shutil

def EjecutarComandos(tabla):

    d = tabla[0]

    nombre = d.get("comando")
    if nombre == "configure":
        if d.get("type") == "local":
            local(tabla,"local")
        elif d.get("type") == "cloud":
            nube(tabla,"cloud")
    else:
        print("error",)

def local(tabla,modo):
    index = 1
    for i in tabla:
        comando = i.get("comando")
        ruta = "/Users/admin/Downloads/Archivos"

        if comando == "create":
            os.makedirs(ruta+ i.get("path"),exist_ok=True)
            f = open( ruta + i.get("path") + i.get("name"),
                "w")
            f.write(i.get("body"))
            f.close()

        elif comando == "delete":
            if "path" and "name"in i:
                try:
                    os.remove(ruta + i.get("path") + i.get("name"))
                except OSError as error:
                    #hay que poner el error en la bitacora
                    print("error")
            else:
                try:
                    os.chdir(ruta)
                    shutil.rmtree(i.get("path"))
                except OSError as error:
                    #hay que poner el error en la bitacora
                    print("No existe el parametro necesario")

        elif comando == "copy":
            if os.path.isfile(ruta+i.get("from")):
                shutil.copy(ruta+i.get("from"), ruta+i.get("to"))
            elif  os.path.isdir(ruta+i.get("from")):
                try:
                    shutil.copytree(ruta+i.get("from"), ruta+i.get("to"))
                except FileExistsError:
                    shutil.copytree(ruta+i.get("from"), os.path.join(ruta+i.get("to"), os.path.basename(ruta+i.get("from"))))
            else:
                # hay que poner el error en la bitacora
                print("La ruta no se refiere a un archivo.")

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
        elif comando == "modify":
        elif comando == "add":
        elif comando == "backup":


