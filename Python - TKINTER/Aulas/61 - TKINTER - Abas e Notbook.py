from tkinter import *
from tkinter import ttk #Biblioteca que contem o recurso NOTEBOOK

#NOTEBOOK - É uma função que permite a criação de abas na tela
#Dentro dessas abas é permitido colocar todos os comandos que desejar

app=Tk()
app.title("Abas e Notebook")
app.geometry("500x300")

nb=ttk.Notebook(app) #Indicando a função Notebook e atribuindo ao app
nb.place(x=0,y=0,width=500, height=300)

#Os elementos que forem atribuidos ao NOTEBOOK vão ter o notebook como 'pai'
tb1 = Frame(nb) 
nb.add(tb1, text="Curso")
lbl=Label(tb1, text="Curso de Python")
lbl.pack()
btn=Button(tb1, text="Clica aqui!")
btn.pack()


tb2 = Frame(nb)
nb.add(tb2, text="Python")

tb3 = Frame(nb)
nb.add(tb3, text="C#")


app.mainloop()