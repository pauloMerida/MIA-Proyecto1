
#Mi rama Meridaimport tkinter as tk
import tkinter as tk
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from encriptacion import *
import binascii
import re

#contra
#gatoperro
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("500x400+500+50")
ventana.resizable(width=False,height=False)
usuarios=[]
contras=[]

archivo = open('usuarios.txt', 'r')
lineas = archivo.readlines()
archivo.close()

usuario=True
for linea in lineas:
    if usuario==True:
        usuarios.append(linea)        
        usuario=False
    else:
        contras.append(linea)        
        usuario=True


# Ejemplo de uso
#key = 'miaproyecto12345'
#hex_data = '686BBE3F53BF138427FFC03A64340A0C'

#clave_hexadecimal = convertir_a_hexadecimal(key)
key="6d696170726f796563746f3132333435"

#contrasena_encriptada = encriptar_contraseña("junio1234", key)
#contrasena_desencriptada = desencriptar_contraseña(hex_data, key)
#print("contra desencriptada: "+contrasena_desencriptada)
#print("contra encriptada: "+contrasena_encriptada)


#Inputs
user = tk.StringVar()
contra = tk.StringVar()

entrada= tk.Entry(ventana,textvar=user,width=40, relief="flat")
entrada.place(x=150,y=144)

entrada2= tk.Entry(ventana,textvar=contra,width=40, relief="flat",show="*")
entrada2.place(x=150,y=225)

#labels
luser= tk.Label(ventana,text="Usuario:",font=("Arial",14,"bold"))
luser.place(x=25,y=144)

lpas=tk.Label(ventana, text="Contraseña:",font=("Arial",14,"bold"))
lpas.place(x=25,y=225)


#funciones
def cerrar():
    ventana.destroy()

def logear():
    key="6d696170726f796563746f3132333435"
    usuario=entrada.get().strip()
    passw=entrada2.get().strip()
    print(passw)
    encontrado=False
    for i in range(len(usuarios)):
        pass_temporal= str(contras[i]).strip()
        user_temporal=str(usuarios[i]).strip()        
        passtemp = desencriptar_contraseña(pass_temporal,key)
        print(passtemp)
        if (passtemp==passw and user_temporal== usuario) or  (usuario=="admin" and passw=="admin"):
            print("credenciales correctas")
            ventana.withdraw()
            from comandos import ventana  as vent
            
            
            
            encontrado=True
    if encontrado==False:
        print("Datos erroneos")
       
#botones

boton = tk.Button(ventana,text="Entrar",cursor="hand2",command=logear, font=("Arial",14,"bold"),background="#5DADE2")
boton.place(x=225,y=305)

boton2= tk.Button(ventana,text="cerrar", cursor="hand2",command=cerrar, font=("Arial",14,"bold"),background="#5DADE2")
boton2.place(x=120,y=305)


ventana.mainloop()
