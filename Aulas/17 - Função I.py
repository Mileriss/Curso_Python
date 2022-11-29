#FUNÇÃO - são trechos / blocos de código que criamos para utilizarmo posteriormente no programa
#Esse trecho de código não é exibido no programa caso não seja "chamado" pelo programador

n1=10
n2=5
def somar():
    resultado=n1+n2
    print("A soma de n1 e n2 eh igual a: {} \n" .format(resultado))
somar()

def subtrair():
    resultado=n1-n2
    print("A subtracao de n1 e n2 eh igual a: {} \n" .format(resultado))
subtrair()

def multiplicacao():
    resultado=n1*n2
    print("A multiplicacao de n1 e n2 eh igual a: {} \n" .format(resultado))
multiplicacao()

def divisao():
    resultado=n1/n2
    print("A divisao de n1 e n2 eh igual a: {} \n" .format(resultado))
divisao()

def calculos():
    somar()
    subtrair()
    multiplicacao()
    divisao()
calculos()



