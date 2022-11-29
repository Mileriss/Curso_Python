from tkinter import *

#LABEL FRAME - Tem a mesma utilidade que o FRAME, as mesmas ações e os mesmos comandos
#A unica diferença entre FRAME e LABELFRAME é uma propriedade dentro do comando TEXT
#Com o LABELFRAME o texto indicado dentro do TEXT fica acoplado dentro do Label

app=Tk()
app.title("LabelFrame")
app.geometry("500x300")

lb_esportes=LabelFrame(app, text="Teste",borderwidth=1, relief="solid")
lb_esportes.place(x=10,y=10,width=300,height=100)


app.mainloop()
