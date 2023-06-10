#Mi rama Meridaimport tkinter as tk
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("500x400+500+50")
ventana.resizable(width=False,height=False)

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
    pass
#botones

boton = tk.Button(ventana,text="Entrar",cursor="hand2",command=logear, font=("Arial",14,"bold"),background="#5DADE2")
boton.place(x=225,y=305)

boton2= tk.Button(ventana,text="cerrar", cursor="hand2",command=cerrar, font=("Arial",14,"bold"),background="#5DADE2")
boton2.place(x=120,y=305)


ventana.mainloop()

