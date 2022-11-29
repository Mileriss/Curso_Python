from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk #Biblioteca com elementos ComboBox

#COMBO BOX - é uma caixa de seleção que permite que o usuário selecione a opção desejada
#É possivel inserir diversas opções e cada uma contendo uma função

def Esporte():
    vesporte=cb_esportes.get()
    print("Esporte selecionado: " + vesporte)

app = Tk()
app.title("ComboBox")
app.geometry("500x300")

listaEsportes=["Futebol","Volei","Basquete"]

lb_esportes=Label(app, text="Esportes")
lb_esportes.pack()

cb_esportes=ttk.Combobox(app, values=listaEsportes)
cb_esportes.set("Futebol")
cb_esportes.pack()

btn_esportes=Button(app, text="Esporte selecionado: ", command=Esporte)
btn_esportes.pack()

app.mainloop()