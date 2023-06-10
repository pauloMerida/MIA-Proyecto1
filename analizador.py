L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ñ', 'ñ','á','é','í','ó','ú', 'Á','É','Í','Ó','Ú']
D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
comandos = ["configure","create","delete","copy","transfer","rename","modify","add","backup"]
parametros =["type","encrypt_log","encrypt_read","llave","name","body","path","from","to","mode"]

class analizador:
    def __init__(self):
        self.fila = 1
        self.columna = 0
        self.lexema = ''
        self.estado = 0
        self.instrucciones = []
        self.comando = []
        self.i = 0

    def x0(self, char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 1
        elif char in D:
            self.lexema += char
            self.columna += 1
            self.estado = 2
        elif char in s:
            self.lexema += char
            self.columna += 1
            self.estado = 3
        elif char == '\n':
            self.comando = []
            self.columna = 0
            self.fila += 1
            self.estado= 0
        else:
            self.errores.append(errores( self.lexema, self.columna, self.fila))
            self.lexema = ''
            self.columna += 1
            self.estado = 0

    def x1(self, char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 1
        elif char =='<':
            self.tokens.append(tokens('string', self.lexema, self.fila, self.columna))
            self.lexema = ''
            self.i -= 1
            self.columna += 1
            self.estado = 0
        elif char in D:
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char in s:
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char == ' ':
            self.lexema += char
            self.columna += 1
            self.estado = 1
        elif char == '\t':
            self.lexema += ' '
            self.columna += 4
            self.estado = 1
        elif char == '\n':
            self.lexema += ' '
            self.columna = 0
            self.fila += 1
            self.estado = 1
        else:
            self.errores.append(errores(self.lexema, self.columna, self.fila))
            self.columna += 1
            self.lexema = ''
            self.estado = 0

    def x2(self, char):
            if char in L:
                self.lexema += char
                self.columna += 1
                self.estado = 4
            elif char in D:
                self.lexema += char
                self.columna += 1
                self.estado = 2
            elif char in s:
                self.lexema += char
                self.columna += 1
                self.estado = 4
            elif char == '<':
                self.tokens.append(tokens('Numero', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.i -= 1
                self.columna += 1
                self.estado = 0
            elif char == '.':
                self.lexema += char
                self.columna += 1
                self.estado = 5
            elif char == ' ':
                self.columna += 1
                self.estado = 2
            elif char == '\t':
                self.columna += 4
                self.estado = 2
            elif char == '\n':
                self.columna = 0
                self.fila += 1
                self.estado = 2
            else:
                self.errores.append(errores(self.lexema, self.columna, self.fila))
                self.lexema = ''
                self.columna += 1
                self.estado = 0

    def x3(self, char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char in D:
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char in s:
            self.lexema += char
            self.columna += 1
            self.estado = 3
        elif char == '<':
            self.tokens.append(tokens('signo', self.lexema, self.fila, self.columna))
            self.lexema = ''
            self.columna += 1
            self.estado = 0
        elif char == '.':
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char == ' ':
            self.lexema += char
            self.columna += 1
            self.estado = 3
        elif char == '\t':
            self.lexema += ' '
            self.columna += 4
            self.estado = 3
        elif char == '\n':
            self.lexema += ' '
            self.columna = 0
            self.fila += 1
            self.estado = 3
        else:
            self.errores.append(errores(self.lexema, self.columna, self.fila))
            self.lexema = ''
            self.columna += 1
            self.estado = 0

    def x4(self,char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char in D:
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char in s:
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char == '<':
            self.tokens.append(tokens('Valor', self.lexema, self.fila, self.columna))
            self.lexema = ''
            self.i -= 1
            self.columna += 1
            self.estado = 0
        elif char == '.':
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char == ' ':
            self.lexema += char
            self.columna += 1
            self.estado = 4
        elif char == '\t':
            self.lexema += ' '
            self.columna += 4
            self.estado = 4
        elif char == '\n':
            self.lexema += ' '
            self.columna = 0
            self.fila += 1
            self.estado = 4
        else:
            self.errores.append(errores( self.lexema, self.columna, self.fila))
            self.lexema = ''
            self.columna += 1
            self.estado = 0

    def x5(self, char):
        if char in D:
            self.lexema += char
            self.columna += 1
            self.estado = 6
        elif char == ' ':
            self.columna += 1
            self.estado = 5
        elif char == '\t':
            self.columna += 4
            self.estado = 5
        elif char == '\n':
            self.columna = 0
            self.fila += 1
            self.estado = 5
        else:
            self.errores.append(errores(self.lexema, self.columna, self.fila))
            self.lexema = ''
            self.columna += 1
            self.estado = 0

    def x6(self,char):
        if char in D:
            self.lexema += char
            self.columna += 1
            self.estado = 6
        elif char == '<':
            self.tokens.append(tokens('Numero', self.lexema, self.fila, self.columna))
            self.lexema = ''
            self.columna += 1
            self.estado = 0
        elif char == ' ':
            self.columna += 1
            self.estado = 6
        elif char == '\t':
            self.columna += 1
            self.estado = 6
        elif char == '\n':
            self.columna = 0
            self.fila += 1
            self.estado = 6
        else:
            self.errores.append(errores( self.lexema, self.columna, self.fila))
            self.columna += 1
            self.lexema = ''
            self.estado = 0

    def x7(self, char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 7
        elif char == '=':
            if self.lexema == 'Operacion':
                self.tokens.append(tokens('inicio', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 7
            elif self.lexema in PR:
                self.tokens.append(tokens('PR', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 1
            else:
                self.errores.append(errores(self.lexema, self.columna, self.fila))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
        elif char == '>':
            if self.lexema in Op:
                self.tokens.append(tokens('OP', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
            elif self.lexema == 'Numero':
                self.tokens.append(tokens('PNum1', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
            elif self.lexema in PR:
                self.tokens.append(tokens('PRI', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
            else:
                self.errores.append(errores(self.lexema, self.columna, self.fila))
                self.errores.append(errores(char, self.columna, self.fila))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
        elif char == '/':
            self.columna += 1
            self.estado = 8
        elif char == ' ':
            self.columna += 1
            self.estado = 7
        elif char == '\t':
            self.columna += 1
            self.estado = 7
        elif char == '\n':
            self.columna = 0
            self.fila += 1
            self.estado = 7
        else:
            self.errores.append(errores(self.lexema, self.columna, self.fila))
            self.lexema = ''
            self.estado = 0

    def x8(self,char):
        if char in L:
            self.lexema += char
            self.columna += 1
            self.estado = 8
        elif char == '>':
            if self.lexema == 'Operacion':
                self.tokens.append(tokens('final', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
            elif self.lexema == 'Numero':
                self.tokens.append(tokens('PNum2', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
            elif self.lexema in PR:
                self.tokens.append(tokens('PRF', self.lexema, self.fila, self.columna))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
            else:
                self.errores.append(errores(self.lexema, self.columna, self.fila))
                self.lexema = ''
                self.columna += 1
                self.estado = 0
        elif char == ' ':
            self.columna += 1
            self.estado = 8
        elif char == '\t':
            self.columna += 1
            self.estado = 8
        elif char == '\n':
            self.columna = 0
            self.fila += 1
            self.estado = 8
        else:
            self.errores.append(errores( self.lexema, self.columna, self.fila))
            self.lexema = ''
            self.columna += 1
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
            elif self.estado == 6:
                self.x6(texto[self.i])
            elif self.estado == 7:
                self.x7(texto[self.i])
            elif self.estado == 8:
                self.x8(texto[self.i])
            self.i += 1