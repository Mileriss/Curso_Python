from tkinter import *
import os

#RADIO BUTTON - São botões para realizar escolhas dentro do sistema, ou seja, uma lista de multipla escolha.
#Com o Radio Button é possivel indicar algumas escolhas para o usuario e cada uma com uma função especifica

app = Tk()
app.title("Radio Buttons")
app.geometry("500x300")

"""
StringVar -> Comando para realizar operações com Variaveis do tipo STR
.GET() -> Comando para armazenar a ação que o usuário realizou no programa
.PACK() -> Comando para armazenar todos os parametros passados em uma variavel
RadioButton -> Comando indicativo do tipo de conteudo que desejamos indicar
"""


vesporte=StringVar()

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

bl_esportes=Label(app, text="Esportes")
bl_esportes.pack()

rb_futebol=Radiobutton(app,text="Futebol", value="F", variable=vesporte)
rb_futebol.pack()

rb_volei=Radiobutton(app,text="Volei", value="V", variable=vesporte)
rb_volei.pack()

rb_basquete=Radiobutton(app,text="Basquete", value="B", variable=vesporte)
rb_basquete.pack()

btn_esporte=Button(app, text="Esporte Selecionado", command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()