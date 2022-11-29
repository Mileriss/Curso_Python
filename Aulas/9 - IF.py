# IF - é uma estrutura que realiza testes lógicos em blocos de comandos e retorna um resultado verdadeiro
#É possivel utilizar o IF para realizar diversos testes afim de conseguir um resultado especifico

n1 = 10
n2 = 5

if n1 > n2: #TRUE
    print("Verdadeiro") #Resultado caso a condição seja atingida

if n1 < n2: #FALSE
    print("Falso")


operacao=0
soma="+"

if soma == "+":
    operacao=n1+n2


if soma == "-":
    operacao=n1-n2

    
if soma == "*":
    operacao=n1*n2

    
if soma == "/":
    operacao=n1/n2

resultado=("O resultado da operacao eh: " + str(operacao))
print(resultado)
