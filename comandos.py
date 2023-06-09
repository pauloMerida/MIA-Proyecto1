import tkinter as tk
from tkinter import font
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Consola")
ventana.geometry("1200x700+500+50")
ventana.resizable(width=False,height=False)

#labels
lconsol = tk.Label(ventana,text="Consola:",font=("Arial",18,"bold"))
lconsol.place(x=30,y=40)

#text Area

area_consola = tk.Text(ventana,width=55, height=22)
nueva_fuente = font.Font(size=16)
area_consola.configure(font=nueva_fuente)
area_consola.place(x=30,y=90)

#botones

boton_config = tk.Button(ventana,text="Configure",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_config.place(x=800,y=90)

boton_transfer = tk.Button(ventana,text="Transfer",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_transfer.place(x=1000,y=90)

boton_create = tk.Button(ventana,text="Create",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_create.place(x=800,y=150)

boton_rename = tk.Button(ventana,text="Rename",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_rename.place(x=1000,y=150)

boton_delete = tk.Button(ventana,text="Delete",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_delete.place(x=800,y=210)

boton_modify = tk.Button(ventana,text="Modify",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_modify.place(x=1000,y=210)

boton_copy = tk.Button(ventana,text="Copy",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_copy.place(x=800,y=270)

boton_add = tk.Button(ventana,text="Add",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_add.place(x=1000,y=270)

boton_back = tk.Button(ventana,text="Backup",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_back.place(x=800,y=320)

boton_exec = tk.Button(ventana,text="Exec",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_exec.place(x=1000,y=320)

boton_sesion = tk.Button(ventana,text="Cerrar sesion",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_sesion.place(x=800,y=380)

boton_analizar = tk.Button(ventana,text="Analizar",cursor="hand2", font=("Arial",14,"bold"),background="#5DADE2")
boton_analizar.place(x=600,y=635)



ventana.mainloop()