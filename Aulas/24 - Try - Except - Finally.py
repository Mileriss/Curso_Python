# TRY - EXCEPT - é um tratamento de erros que podemos colocar no nosso código caso haja alguma excessão na execução
# Ao invés de exibir a mensagem padrão de erri de um navegador, nós podemos criar mensagens especificas

from logging import exception, raiseExceptions


x=10
try: #bloco para indicar a operação
    print(x)
except: #Indica algo, caso ocorra uma excessão no TRY
    print("X nao esta definido")
else: #Indica o contrario do resultado de EXCEPT
    print("X foi definido com o valor: " + str(x))
finally: #Indica a ultima etapa de erro, caso tenha ou não excessões, essa condição será exibida
    print("O erro foi ajustado!")

#Gerar excessões
num = 10
if num < 1: #Caso a variavel seja menor que 1, o programa vai gerar uma excessão
    raise exception("Valor nao permitido") #Excessão definida caso a condição acima seja atingida
else:
    print("Valor permitido")



