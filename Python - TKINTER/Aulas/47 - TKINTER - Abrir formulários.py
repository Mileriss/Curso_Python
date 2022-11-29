from tkinter import *
import os

#Para Abrir novos formulários é necessário utilizar a função de indicar arquivos e selecionar uma função que irá chamar os arquivos
#Neste caso estamos utilizando outro formulário TKINTER para ser aberto quando clicamos em 'NOVO' na barra 'Contatos'


pastaApp = os.path.dirname(__file__) #Comando utilizado para chamar um arquivo de outro local do PC

def novoFormulario(): #Função criada para chamar o arquivo
    exec(open(pastaApp+"\\43 - TKINTER - Entry e Text.py").read()) #Comandos para realizar o caminho e abrir o arquivo

"""
EXEC -> Comando para 'executar' uma função
OPEN -> Comando para abrir um determinado arquivo
pastaAPP -> Variavek que contem o caminho do diretorio
\\nome_do_diretorrio.py -> Nome do arquivo que desejamos exibir
.READ() -> Comando para realizar a abertura do arquivo indicado

"""



def semComando():
    print("Clicou!")
    
app = Tk()
app.title("Barra de menu")
app.geometry("500x300")
app.configure(background="#dde")


#Local que vai armazenar as informações da barra de menus
barra_menu=Menu(app)

#Barra de contatos
menuContatos=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Contatos", menu=menuContatos)
menuContatos.add_command(label="Novo",command=novoFormulario)
menuContatos.add_command(label="Pesquisar",command=semComando)
menuContatos.add_command(label="Deletar",command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar",command=semComando)

#Barra de Agenda
menuAgenda=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Agenda", menu=menuAgenda)
menuAgenda.add_command(label="Buscar",command=semComando)
menuAgenda.add_command(label="Adicionar",command=semComando)
menuAgenda.add_command(label="Deletar",command=semComando)
menuAgenda.add_separator()
menuAgenda.add_command(label="Fechar",command=semComando)

#Barra de Telefone
menuTelefone=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Telefone", menu=menuTelefone)
menuTelefone.add_command(label="Discar",command=semComando)
menuTelefone.add_command(label="Apagar",command=semComando)
menuTelefone.add_separator()
menuTelefone.add_command(label="Fechar",command=semComando)

#Barra de SOS
menuSOS=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="SOS", menu=menuSOS)
menuSOS.add_command(label="190",command=semComando)
menuSOS.add_command(label="192",command=semComando)
menuSOS.add_command(label="193",command=semComando)
menuSOS.add_separator()
menuSOS.add_command(label="Fechar",command=semComando)


app.config(menu=barra_menu)
app.mainloop()