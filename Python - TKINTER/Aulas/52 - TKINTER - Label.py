from tkinter import *

app = Tk()
app.title("Frame")
app.geometry("500x300")

#LABEL - É um elemento que inserimos na interface que contem algum tipo de texto ou formatação
#Pode ser utilizado como uma caixa para indicar diversas opções


#TEXT - Onde vai conter o texto da Label
#BACKGROUND - Cor de fundo da label
#FOREGROUND - Cor de 'frente' da label
#WIDTH - Largura 
#HEIGHT - Altura
#FONT - Estilo de fonte e tamanho da fonte

lb_teste=Label(app, text="Teste de Label",
                background="black", foreground="gray",
                width=15, height=5,
                font=("Arial", 15))
lb_teste.pack(side=LEFT, fill=X, expand=TRUE)

#SIDE - Local que o Label vai ficar localizado
#FILL - Preenchimento da Label (X ou Y)
#X - Horizontal
#Y - Vertical
#EXPAND - Expansão da Label

app.mainloop()