from tkinter import *
from tkinter import ttk
import os
import Banco

def GravarDados():
    if tb_nome != "":
        varnome=tb_nome.get()
        vartelefone=tb_telefone.get()
        varemail=tb_email.get()
        varobs=tb_obs.get("1.0",END)
        vquery="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS) VALUES ('"+varnome+"','"+vartelefone+"','"+varemail+"','"+varobs+"')"
        Banco.dml(vquery)
        tb_nome.delete(0,END)
        tb_telefone.delete(0,END)
        tb_email.delete(0,END)
        tb_obs.delete("1.0",END)
        print("Dados gravados!")
    else:
        print("Erro!")

app=Tk()

app.title("Button Widget")
app.geometry("500x300")
app.configure(background="black")

#PRIMEIRO ELEMENTO
#ENTRY - é uma forma de adicionarmos uma Label que permite adicionar valores, como uma linha de formulário
Label(app,text="Nome", background="black",foreground="white",anchor=W).place(x=10,y=10,width=100,height=20)
tb_nome=Entry(app)
tb_nome.place(x=10,y=30,width=200,height=20)

#SEGUNDO ELEMENTO
Label(app,text="Telefone", background="black",foreground="white",anchor=W).place(x=10,y=55,width=100,height=20)
tb_telefone=Entry(app)
tb_telefone.place(x=10,y=75,width=100,height=20)

#TERCEIRO ELEMENTO
Label(app,text="E-mail", background="black",foreground="white",anchor=W).place(x=10,y=100,width=100,height=20)
tb_email=Entry(app)
tb_email.place(x=10,y=120,width=180,height=20)

#QUARTO ELEMENTO
#TEXT - é um bloco que adicionamos para escrever um texto continuo, sem necessariamente a ideia de ter linhas individuais
Label(app,text="Observações", background="black",foreground="white",anchor=W).place(x=10,y=150,width=100,height=20)
tb_obs=Text(app)
tb_obs.place(x=10,y=175,width=300,height=80)

Button(app,text="Imprimir",command=GravarDados).place(x=10,y=270,width=100,height=20)


app.mainloop()