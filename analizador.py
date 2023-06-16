from InstruccionesComandos import *
from BitacoraAcciones import *

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ñ', 'ñ','á','é','í','ó','ú', 'Á','É','Í','Ó','Ú']
D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
comandos = ["configure","create","delete","copy","transfer","rename","modify","add","backup"]
parametros =["type","encrypt_log","encrypt_read","llave","name","body","path","from","to","mode"]

class analizador:
    def __init__(self):
        self.lexema = ''
        self.estado = 0
        self.instrucciones = []
        self.parametros = []
        self.comando = ""
        self.i = 0

    def x0(self, char):
        if char in L:
            self.lexema += char
            self.estado = 1
        elif char == '\n':
            diccionario = {}
            diccionario["comando"] = self.comando

            for i in range(0, len(self.parametros), 2):
                clave = self.parametros[i]
                valor = self.parametros[i + 1]
                diccionario[clave] = valor
            self.instrucciones.append(diccionario)

            diccionario = {}
            self.comando = ""
            self.parametros = []
            self.estado= 0
        elif char == '-':
            self.estado= 2
        elif char == '>':
            self.estado= 3
        else:
            HF = HorayFecha()
            self.errores.append(bitacora(HF[1],HF[0],"ERROR","Error de escritura en el lexema: "+self.lexema))
            self.lexema = ''
            self.estado = 0

    def x1(self, char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 1
        elif char ==' ':
            if (self.lexema.lower()) in comandos:
                self.comando = self.lexema.lower()
            self.lexema = ''
            self.estado = 0
        else:
            self.comando = "errorcomando"
            HF = HorayFecha()
            self.errores.append(bitacora(HF[1], HF[0], "ERROR", "El comando: " + self.lexema+" no existe."))
            self.lexema = ''
            self.estado = 0

    def x2(self, char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 2
        elif char == '-':
            if (self.lexema.lower()) in parametros:
                self.parametros.append(self.lexema.lower())
            self.lexema = ''
            self.estado = 0
        else:
            self.parametros.append("errorparametro")
            HF = HorayFecha()
            self.errores.append(bitacora(HF[1], HF[0], "ERROR", "El parámetro " + self.lexema+" no existe."))
            self.lexema = ''
            self.estado = 0

    def x3(self,char):
        if char in L:
            self.lexema += char
            self.estado = 3
        elif char in D:
            self.lexema += char
            self.estado = 3
        elif char == "/":
            self.lexema += char
            self.estado = 3
        elif char == '\"' and self.parametros[-1] == "path":
            self.estado = 4
        elif char == '\"' and self.parametros[-1] == "body":
            self.estado = 5
        elif char == ' ':
            self.parametros.append(self.lexema)
            self.lexema = ''
            self.estado = 0
        elif char == '\n':
            self.parametros.append(self.lexema)
            self.lexema = ''
            self.i -= 1
            self.estado = 0
        else:
            self.parametros.append("errorparametro")
            HF = HorayFecha()
            self.errores.append(bitacora(HF[1], HF[0], "ERROR", "Error de escritura en: " + self.lexema))
            self.lexema = ''
            self.estado = 0

    def x4(self,char):
        if char in L:
            self.lexema += char
            self.estado = 4
        elif char in D:
            self.lexema += char
            self.estado = 4
        elif char == '\"':
            self.estado = 3
        elif char == ' ':
            self.estado = 4
        else:
            self.parametros.append("errorparametro")
            HF = HorayFecha()
            self.errores.append(bitacora(HF[1], HF[0], "ERROR", "Error de escritura en: " + self.lexema))
            self.lexema = ''
            self.estado = 0

    def x5(self,char):
        if char in L:
            self.lexema += char
            self.estado = 5
        elif char in D:
            self.lexema += char
            self.estado = 5
        elif char == '\n':
            self.lexema += char
            self.estado = 5
        elif char == '\"':
            self.parametros.append(self.lexema)
            self.lexema = ''
            self.estado = 0
        elif char == ' ':
            self.lexema += char
            self.estado = 5
        else:
            HF = HorayFecha()
            self.errores.append(bitacora(HF[1], HF[0], "ERROR", "Error de escritura en: " + self.lexema))
            self.lexema = ''
            self.estado = 0

    def analizar(self,texto):
        #hay que enviar el archivo en analizar(archivo)
        self.i = 0
        while self.i < len(texto):
            if self.estado == 0:
                self.x0(texto[self.i])
            elif self.estado == 1:
                self.x1(texto[self.i])
            elif self.estado == 2:
                self.x2(texto[self.i])
            elif self.estado == 3:
                self.x3(texto[self.i])
            elif self.estado == 4:
                self.x4(texto[self.i])
            elif self.estado == 5:
                self.x5(texto[self.i])
            self.i += 1

        CrearArreglo(self.errores)
        EjecutarComandos(self.instrucciones)


