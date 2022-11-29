from tkinter import *
from tkinter.tix import Select

#LIST BOX - É uma lista contendo varias opções para seleção do usuário
#É possivel criar uma lista com opções na qual o usuário terá interação


"""
get(ACTIVE) - Comando indicando a seleção ativa
get()  Comando para selecionar e armazenar o conteudo
END - Comando para indicar que uma ação vai entrar no FINAL
insert - Comando para indicar a inserção de um conteudo
delete - Comando para indicar a exclusão de um conteudo
"""

def imprimirEsporte():
    print("Esporte: " + lb_esportes.get(ACTIVE))

def deletarEsporte():
    lb_esportes.delete(END)


def adicionarEsporte():
    lb_esportes.insert(END,vnovoesporte.get()) 

app=Tk()

app.title("ListBox")
app.geometry("500x300")

listaEsportes=["Futebol","Volei","Basquete"]

lb_esportes=Listbox(app)
for esportes in listaEsportes:
    lb_esportes.insert(END,esportes)
lb_esportes.pack()

btn_esporte=Button(app, text="Imprimir esporte", command=imprimirEsporte)
btn_esporte.pack()

btn_deletarEsporte=Button(app, text="Deletar ultimo da lista", command=deletarEsporte)
btn_deletarEsporte.pack()

vnovoesporte=Entry(app)
vnovoesporte.pack()

btn_inserirEsporte=Button(app, text="Inserir Esporte", command=adicionarEsporte)
btn_inserirEsporte.pack()
app.mainloop()
