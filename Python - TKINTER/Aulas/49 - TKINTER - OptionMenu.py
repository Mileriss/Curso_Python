from tkinter import *

def imprimirEsporte():
    ve=vesporte.get()
    if ve == "F":
        print("Esporte Futebol")
    elif ve == "V":
        print("Esporte Volei")
    elif ve == "B":
        print("Esporte Basquete")
    else:
        print("Nenhum esporte selecionado!")

app = Tk()
app.title("Radio Buttons")
app.geometry("500x300")

listaEsportes=["Futebol","Volei","Basquete"]

vesporte=StringVar()
vesporte.set(listaEsportes[0]) #Valor padrão

bl_esportes=Label(app, text="Esportes")
bl_esportes.pack()

op_esportes=OptionMenu(app, vesporte, *listaEsportes)
op_esportes.pack()

btn_esporte=Button(app, text="Esporte Selecionado", command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()