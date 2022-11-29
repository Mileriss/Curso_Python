#IF - Inicia uma estrutura de testes lógicos
#ELIF - Adiciona mais testes a essa estrutura, permitindo diversas condições
#ELSE - Finaliza a estrutura caso a condição não seja atingida no IF e ELIF
#AND - Permite realizar 2 verificações em uma operação (Se o valor for x AND valor for y)
#OR - Permite criar 2 condições para verificação. (Se o valor for x OR valor for y)

n1 = 10
n2 = 5
soma="+"
subt="-"
mult="*"
div="/"
operacao=0


if soma == "+":
    operacao=n1+n2
    resultado=("O resultado da operacao eh: " + str(operacao))
elif subt == "-":
    operacao=n1-n2
    resultado=("O resultado da operacao eh: " + str(operacao))
elif soma == "*":
    operacao=n1*n2
    resultado=("O resultado da operacao eh: " + str(operacao))
elif soma == "/":
    operacao=n1/n2
    resultado=("O resultado da operacao eh: " + str(operacao))
else:
    print("Nenhuma condicao foi atingida!")


role="praia"
clima="sol"
role2="casa"
clima2="chuva"

#AND
if role == "praia" and clima == "sol":
    print("Condicao AND foi atingida")
elif role2 == "casa" and clima2 == "chuva":
    print("Condicao AND nao foi atingida")
else:
    print("Nenhuma condicao foi atingida")

#OR
if role2 == "casa" or clima2 == "chuva":
    print("Condicao OR atingida")
elif role == "praia" or clima == "sol":
    print("Condicao OR nao foi atingida")
else:
    print("Nenhuma condicao foi atingida")


#AND e OR
camisa=100
dinheiro=200
camisa2=300
dinheiro2=500

if camisa == 100 and (dinheiro > 100 or dinheiro < 200):
    print("Condicao AND e OR foi atingida")
elif camisa2 == 300 or (dinheiro2 > 100 and dinheiro2 < 600):
    print("Condicao OR e AND foi atingida")
else:
    print("Nenhuma condicao foi atingida")

