import datetime
from login import *

global ArregloBitacora
ArregloBitacora = []

class bitacora:

    def __init__(self,fecha, hora, tipo, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.tipo = tipo
        self.des = descripcion

def HorayFecha():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    fecha_actual = datetime.date.today().strftime("%d/%m/%Y")

    return hora_actual, fecha_actual

def CrearArreglo(tabla):
    for i in tabla:
        ArregloBitacora.append(i)

def escribirBitacora(modo,clave):
    contenido = ""
    ClaveEncriptacion = convertir_a_hexadecimal(clave)

    if modo == "false":
        for i in ArregloBitacora:
            linea = i.fecha + " | " + i.hora + " | Tipo: " + i.tipo + " | " + i.des + "\n"
            contenido += linea

        HF = HorayFecha()
        HF1 = HF[1].split("/")
        HF2 = HF1[2] + "/" + HF1[1] + "/" + HF[0] + "/"

        os.makedirs("/Users/admin/Downloads/Archivos/logs/" + HF2, exist_ok=True)
        f = open("/Users/admin/Downloads/Archivos/logs/" + HF2 + "log_archivos.txt", "a")
        f.write(contenido)
        f.close()
        ArregloBitacora.clear()


    if modo == "true":
        for i in ArregloBitacora:
            linea = i.fecha + " | " + i.hora +" | Tipo: " + i.tipo + " | " + i.des + "\n"
            encriptado = encriptar_contraseña(linea,ClaveEncriptacion)
            contenido += encriptado

        HF = HorayFecha()
        HF1 = HF[1].split("/")
        HF2=HF1[2]+"/"+HF1[1]+"/"+HF[0]+"/"

        os.makedirs("/Users/admin/Downloads/Archivos/logs/" + HF2, exist_ok=True)
        f = open( "/Users/admin/Downloads/Archivos/logs/"+HF2+"log_archivos.txt", "a")
        f.write(contenido)
        f.close()
        ArregloBitacora.clear()

