from tkinter import *
from tkinter import ttk
import os


#Abrindo um arquivo txt em branco e adicionando pelo formulário criado
c=os.path.dirname(__file__)
nomeArquivo=c+"\\Arquivos Criados\\nomes.txt"

def ImportarDados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("Nome...........: %s" %varNome.get())
    arquivo.write("\nTelefone.......: %s" %varTelefone.get())
    arquivo.write("\nEmail..........: %s" %varEmail.get())
    arquivo.write("\nObservacao.....: %s" %varObs.get("1.0",END))
    arquivo.write("\n")
    arquivo.close()


app=Tk()

app.title("Button Widget")
app.geometry("500x300")
app.configure(background="black")

#PRIMEIRO ELEMENTO
#ENTRY - é uma forma de adicionarmos uma Label que permite adicionar valores, como uma linha de formulário
Label(app,text="Nome", background="black",foreground="white",anchor=W).place(x=10,y=10,width=100,height=20)
varNome=Entry(app)
varNome.place(x=10,y=30,width=200,height=20)

#SEGUNDO ELEMENTO
Label(app,text="Telefone", background="black",foreground="white",anchor=W).place(x=10,y=55,width=100,height=20)
varTelefone=Entry(app)
varTelefone.place(x=10,y=75,width=100,height=20)

#TERCEIRO ELEMENTO
Label(app,text="E-mail", background="black",foreground="white",anchor=W).place(x=10,y=100,width=100,height=20)
varEmail=Entry(app)
varEmail.place(x=10,y=120,width=180,height=20)

#QUARTO ELEMENTO
#TEXT - é um bloco que adicionamos para escrever um texto continuo, sem necessariamente a ideia de ter linhas individuais
Label(app,text="Observações", background="black",foreground="white",anchor=W).place(x=10,y=150,width=100,height=20)
varObs=Text(app)
varObs.place(x=10,y=175,width=300,height=80)

Button(app,text="Imprimir",command=ImportarDados).place(x=10,y=270,width=100,height=20)


 

app.mainloop()