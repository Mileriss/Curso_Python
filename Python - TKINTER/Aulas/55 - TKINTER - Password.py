from distutils.cmd import Command
from tkinter import *

#PASSWORD - É uma opção dentro da função ENTRY que permite esconder a senha que o usuário inserir
#É possivel colocar qualquer letra ou simbolo no campo de senhas

def imprimirSenha():
    print("Senha digitada:"+vsenha.get()) #GET - pega o valor que foi digitado na variavel

app=Tk()
app.title("Password")
app.geometry("500x300")

#Variavel do tipo String
vsenha=StringVar() 

#SHOW - Local que vai ser exibida a senha do usuário
psenha=Entry(app, textvariable=vsenha, show="*")
psenha.pack()

mostrarSenha=Button(app, text="Imprimir Senha", command=imprimirSenha)
mostrarSenha.pack()

app.mainloop()