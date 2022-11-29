from tkinter import *
from tkinter import messagebox

#MESSAGE BOX - São caixas de mensagem que exibem uma mensagem para o usuário
#Essas mensagens podem conter alguma informação, uma tomada de decisão, um erro, um alerta e etc...

app = Tk()
app.title("MessageBox")
app.geometry("500x300")

"""
TIPOS DE CAIXAS DE MENSAGEM
"""

#Caixa de mensagem do tipo INFO
#INFO - Tipo de mensagem que vai conter e exibir uma informação, tanto positiva como negativa
messagebox.showinfo(title="Caixa de teste", message="Teste INFO!")

#Caixa de mensagem do tipo WARNING
#WARNING - Tipo de mensagem que vai conter uma informação de alerta para o usuário
messagebox.showwarning(title="Caixa de teste", message="Teste de WARNING!")

#Caixa de mensagem do tipo ERROR
#ERROR - Tipo de mensagem que vai exibir um erro para o usuário
messagebox.showerror(title="Caixa de teste", message="Teste de ERROR!")



"""
CAIXAS DE MENSAGEM COM INTERAÇÕES
"""

#ASKYESNO / ASKQUESTION - SIM e NÃO (True e False)
messagebox.askyesno("Sim ou Não","Deseja sair?")

#ASKOKCANCEL - OK e CANCELAR (True e False)
messagebox.askokcancel("Sim ou Não","Deseja sair?")

#ASKRETRYCANCEL - REPETIR E CANCELAR (True e False)
messagebox.askretrycancel("Sim ou Não","Deseja sair?")

#ASKYESNOCANCEL -  SIM, NÃO e CANCELAR (True, False e None)
messagebox.ask("Sim ou Não","Deseja sair?")




app.mainloop()
