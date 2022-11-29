from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#TREE VIEW - É uma grade onde contem vários conteudos, muito parecido com uma lista ou com uma tela de banco de dados
#É possivel personalizar ele com funções e etc...

def inserir():
    if vid.get() == "" or vnome.get()=="" or vtelefone.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados: ")
        return
    tv.insert("", "end", values=(vid.get(), vnome.get(),vtelefone.get()))
    vid.delete(0,END)
    vnome.delete(0,END)
    vtelefone.delete(0,END)
    tv.focus()

def deletar():
    try:
        itemselecionado=tv.selection()[0]
        tv.delete(itemselecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione o item que deseja deletar!")


    
def obter():
    try:
        itemselecionado=tv.selection()[0]
        valores=tv.item(itemselecionado, "values")
        print("ID:.........." + valores[0])
        print("Nome.........:" + valores[1])
        print("Telefone.....:" + valores[2])

    except:
        messagebox.showinfo(title="ERRO", message="Selecione o item a ser exibido!")


app=Tk()
app.title("TreeView")
app.geometry("700x400")

lbid=Label(app, text="ID")
vid=Entry(app)

lbnome=Label(app, text="NOME")
vnome=Entry(app)

lbtelefone=Label(app, text="TELEFONE")
vtelefone=Entry(app)


tv=ttk.Treeview(app, column=('id','nome', 'telefone'), show='headings')

tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=200)
tv.column('telefone', minwidth=0, width=100)
tv.heading('id', text="ID")
tv.heading('nome', text='NOME')
tv.heading('telefone', text='TELEFONE')

btn_inserir = Button(app, text="Inserir", command=inserir, background="lightblue")
btn_deletar = Button(app, text="Deletar", command=deletar)
btn_obter = Button(app, text="Obter", command=obter)

lbid.grid(column=0, row=0, sticky='w')
vid.grid(column=0, row=1)

lbnome.grid(column=1, row=0, sticky='w')
vnome.grid(column=1, row=1)

lbtelefone.grid(column=2, row=0, sticky='w')
vtelefone.grid(column=2, row=1)

tv.grid(column=0, row=3, columnspan=3, pady=5)


btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)


#tv.insert("","end", values=(id, nome, telefone))



app.mainloop()
