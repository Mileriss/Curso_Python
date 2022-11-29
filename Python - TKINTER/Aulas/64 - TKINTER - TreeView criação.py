from tkinter import *
from tkinter import ttk

#TREE VIEW - É uma grade onde contem vários conteudos, muito parecido com uma lista ou com uma tela de banco de dados
#É possivel personalizar ele com funções e etc...

app=Tk()
app.title("TreeView")
app.geometry("500x300")

listaNome=[['0','Rafael','1234'],['1','Maria','5678'],['2','Antonia','9101']]

tv=ttk.Treeview(app, column=('id','nome', 'telefone'), show='headings')

tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=200)
tv.column('telefone', minwidth=0, width=100)
tv.heading('id', text="ID")
tv.heading('nome', text='NOME')
tv.heading('telefone', text='TELEFONE')
tv.pack()


for (id, nome, telefone) in listaNome:
    tv.insert("","end", values=(id, nome, telefone))



app.mainloop()