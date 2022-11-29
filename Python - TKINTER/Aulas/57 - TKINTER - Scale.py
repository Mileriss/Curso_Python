from tkinter import *
from tkinter import ttk

def valorEscala():
    print("Valor da escala " + str(scEscala.get())) #Vai receber o valor da escala

#SCALE - É uma barra de rolagem onde você pode definir um numero de inicio e um numero de finalização

app=Tk()
app.title("Scale")
app.geometry("500x300")

lbValor=Label(app, text="Valor")
lbValor.pack()

"""
FROM_ -> É o indicativo de onde vai começar a contagem do Scale
TO -> É o indicativo de onde vai terminar a contagem do scale
ORIENT -> Posição que a barra Scale vai ser posicionada, neste caso na Horizontal (Pode ser vertical tambem)
"""

scEscala=Scale(app, from_=0, to=100, orient=HORIZONTAL)
scEscala.set(50)
scEscala.pack()

btnEscala = Button(app, text="Valor da Escala", command=valorEscala)
btnEscala.pack()

app.mainloop()