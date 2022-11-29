from tkinter import *
import os #Biblioteca para puxar o arquivo

#Comando para indicar que será puxado um arquivo
pastaApp=os.path.dirname(__file__)

app = Tk()
app.title("PhotoImages")
app.geometry("500x300")

#Caminho que a imagem está localizada
img=PhotoImage(file=pastaApp+"\\Imagens\\logo_python.png")
#Label da imagem
img_logo=Label(app, image=img) 
#Posição da imagem
img_logo.place(x=10,y=10)

app.mainloop()