from ctypes import sizeof
from tkinter import *
from tkinter import ttk
from tkinter import font

#GRID - É uma forma de organizar os elementos da tela utilizando linhas e colunas
#É seguido um padrão onde as colunas e linhas são sempre do mesmo tamanho e os elementos são ordenados de forma mais pratica

"""
Sticky = É uma forma de mover os elementos, utilizando como parametro as localizações abaixo
#n-(topo), s-(Baixo), e-(Direita), w-(Esquerda)

COLUMN = Coluna que vai ser indicado o elemento
ROW = Linha onde o elemento vai ser indicado
COLUMNSPAN = Junção de colunas que possibilita a organização de labels ou outros elementos 
ROWSPAN = Junção de linhas que possibilita a organização de labels ou outros elementos 
PADX = Espaço indicado entre os elementos (HORIZONTAL)
PADY = Espaço indicado entre os elementos (VERTICAL)
"""

app = Tk()
app.title("GRID")
app.geometry("500x300")

lb_titulo=Label(app, text="TITULO DE TESTE")
lb_titulo.grid(column=0, row=0, pady=20)

lb_nome=Label(app, text="Digite o seu nome: ")
et_nome=Entry(app)
lb_nome.grid(column=0,row=1, sticky='e', padx=10, pady=5) 
btn=Button(app, text="Teste")
btn.grid(column=1, row=1)


lb_idade=Label(app, text="Digite a sua idade: ")
et_idade=Entry(app)
lb_idade.grid(column=0,row=2,sticky="w", padx=10, pady=5) 
btn2=Button(app, text="Teste")
btn2.grid(column=1, row=2)


app.mainloop()