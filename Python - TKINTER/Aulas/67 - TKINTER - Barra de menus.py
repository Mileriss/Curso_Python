from tkinter import *
#from tkinter import ttk

def semComando():
    print("Nada")

app=Tk()
app.title("Barra de menus")
app.geometry("500x300")

barradeMenu=Menu(app)
menuContato=Menu(barradeMenu, tearoff=0)
menuContato.add_command(label="Novo", command=semComando)
menuContato.add_command(label="Pesquisar", command=semComando)
menuContato.add_command(label="Deletar", command=semComando)
menuContato.add_separator()
menuContato.add_command(label="Fechar", command=semComando)
barradeMenu.add_cascade(label="Contatos", menu=menuContato)

app.config(menu=barradeMenu)


app.mainloop()