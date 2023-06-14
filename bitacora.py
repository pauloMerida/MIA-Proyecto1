import datetime

from

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

def escribirBitacora(tabla, modo):

    if modo == "false":
        for i in tabla:


    if modo == "true":
        for i in tabla: