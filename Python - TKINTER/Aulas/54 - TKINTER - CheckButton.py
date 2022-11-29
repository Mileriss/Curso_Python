from tkinter import *

#CHECK BUTTON - É bem parecido com o RADION BUTTON, são multiplas escolhas que o usuário pode selecionar 
#É possivel adicionar funções para cada tipo de escolha 

def Futebol():
    print("Futebol selecionado!")


def Volei():
    print("Volei selecionado!")


def Basquete():
    print("Basquete selecionado!")

app = Tk()
app.title("CheckButtons")
app.geometry("500x300")

futebol=StringVar()
volei=StringVar()
basquete=StringVar()

quadro=Frame(app, borderwidth=1, relief="solid")
quadro.place(x=10,y=10,width=300,height=100)

cb_futebol=Checkbutton(quadro, text="Futebol", variable=futebol, onvalue="s", offvalue="n", command=Futebol)
cb_futebol.pack(side=LEFT)

cb_volei=Checkbutton(quadro, text="volei", variable=volei, onvalue="s", offvalue="n", command=Volei)
cb_volei.pack(side=LEFT)

cb_basquete=Checkbutton(quadro, text="basquete", variable=basquete, onvalue="s", offvalue="n", command=Basquete)
cb_basquete.pack(side=LEFT)


app.mainloop()