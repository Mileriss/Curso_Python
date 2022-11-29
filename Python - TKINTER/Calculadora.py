from distutils.cmd import Command
from tkinter import *
from tkinter import messagebox
from turtle import width

app=Tk()
app.title("Calculadora")
app.geometry("500x300")


botao_1 = Button(app, text="1", width=6, height=3)
botao_1.grid(column=0, row=1, padx=1.5, pady=2)

botao_2 = Button(app, text="2", width=6, height=3)
botao_2.grid(column=1, row=1, padx=1.5, pady=2)

botao_3 = Button(app, text="3", width=6, height=3)
botao_3.grid(column=2, row=1, padx=1.5, pady=2)

botao_4 = Button(app, text="4", width=6, height=3)
botao_4.grid(column=0, row=2, padx=1.5, pady=2)

botao_5 = Button(app, text="5", width=6, height=3)
botao_5.grid(column=1, row=2, padx=1.5, pady=2)

botao_6 = Button(app, text="6", width=6, height=3)
botao_6.grid(column=2, row=2, padx=1.5, pady=2)

botao_7 = Button(app, text="7", width=6, height=3)
botao_7.grid(column=0, row=3, padx=1.5, pady=2)

botao_8 = Button(app, text="8", width=6, height=3)
botao_8.grid(column=1, row=3, padx=1.5, pady=2)

botao_9 = Button(app, text="9", width=6, height=3)
botao_9.grid(column=2, row=3, padx=1.5, pady=2)

botao_0 = Button(app, text="0", width=6, height=3)
botao_0.grid(column=1, row=4, padx=1.5, pady=2)

botao_cancelar = Button(app, text="Cancelar", width=6, height=3)
botao_cancelar.grid(column=0, row=4, padx=1.5, pady=2)

botao_enviar = Button(app, text="Enviar", width=6, height=3)
botao_enviar.grid(column=2, row=4, padx=1.5, pady=2)

app.mainloop()