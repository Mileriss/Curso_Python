from tkinter import *

app = Tk()
app.title("Frame")
app.geometry("500x300")

vnum_cstexto=StringVar()

#RELIEF - Formato do blco onde contem o FRAME
#flat, raised, sunken, solid

#FLAT - Forma comum e sem estilos sobrepostos
#RAISED - Forma com as bordas no estilo sobreposto para fora
#SUNKEN - Forma com as bordas no estilo sobreposto para dentro
#SOLID - Forma com as bordas sem estilo, apenas com uma marcação

#Altere o campo relief com o estilo desejado para visualizar o resultado
fr_quadro1=Frame(app, borderwidth=2, relief="sunken")
fr_quadro1.place(x=10, y=10, width=200,height=100)
lb_tipo1=Label(fr_quadro1, text="Tipo FLAT")
lb_tipo1.place(x=10,y=10)
tb_num=Entry(fr_quadro1, textvariable=vnum_cstexto)
vnum_cstexto.set("1")
tb_num.place(x=10,y=30)


app.mainloop()