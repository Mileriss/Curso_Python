#Para obter retorno de valores nas funções, nós podemos utilizar listas e indicar os valores desejados
#Após criar a lista, utilizados uma condição FOR para percorrer os valores da função e posteriormente exibir o resultado

valores=[5,10,15,20,25,30]
def somar(num):
    resultado=0
    for n in num:
        resultado+=n
    return resultado
print(str(valores) + ": soma = " + str(somar(valores)))