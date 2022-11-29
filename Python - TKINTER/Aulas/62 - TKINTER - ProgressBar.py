from tkinter import *
from tkinter import ttk #Biblioteca que contem o progress bar

def valbarra(m):
    cont=0
    etapas=m/100
    while cont < etapas:
        cont=cont+1
        i=0
        while i < 60000:
            i=i+1
        varBarra.set(cont)
        app.update()



app=Tk()
app.title("ProgressBar")
app.geometry("500x300")

varBarra=DoubleVar() #Variavel para a Barra de progresso
varBarra.set(0) #Padrão da barra começa em 0


#Função para realizar o uso da Progressbar
pb=ttk.Progressbar(app, variable=varBarra, maximum=100) #Maximo da barra vai até 100
pb.place(x=0,y=0,width=500,height=40)

btn=Button(app,text="Definir barra", command=lambda: valbarra(10000))
btn.place(x=0,y=0,width=100,height=40)

app.mainloop()
