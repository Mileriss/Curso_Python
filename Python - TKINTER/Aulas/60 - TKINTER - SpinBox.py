from tkinter import *

#SPIN BOX - É uma caixinha com determinados valores estabelecidos, no qual é possivel selecionar um valor ou rolar por vários valores
#É possivel indicar de 0 - 10, por exemplo, e criar uma interação para cada valor indicado

def imprimirValores():
    print("O valor atual eh: " + str(sb_valores.get()))

app=Tk()
app.title("SpinBox")
app.geometry("500x300")

sb_valores=Spinbox(app, from_=0, to=10)
#sb_valores=Spinbox(app, values=(1,2,3,4,5))
sb_valores.pack()

btn_valores=Button(app, text="Imprimir valores", command=imprimirValores)
btn_valores.pack()

app.mainloop()
