#Argumentos de entrada nas funções se refere a quando desejamos indicar diferentes valores para uma função definida
#É possivel utilizar os parametros informados para retornar diferentes resultados, utilizando as mesmas variaveis
#Basta definir as variaveis desejadas no parametro da função e executar indicando parametros diferentes, seja com numeros ou textos

#Diferentes parametros
n1=10
n2=20
def somar(n1,n2): #Parametros que recebem a alteração
    resultado=n1+n2
    print("A soma de {} + {} eh igual a: {}" .format(n1,n2,resultado))
somar(10,10) #Primeira alteração
somar(10,20) #Segunda alteração
somar(10,30) #Terceira alteração
somar(10,40) #Quarta alteração
"\n"

#Argumentos arbitrários
def textos(*txt):
    for t in txt:
        print(t)
textos("Curso"," de ","Python")
"\n"

def numeros(*num):
    nm=0
    for n in num:
        nm+=n
        print("A soma dos numeros sao: " +str(nm))
numeros(5,10,15,20,25,30)
"\n"

#Parametro padrão
def carro(c="Porshe"):
    print("Modelo: " + c)
carro()


