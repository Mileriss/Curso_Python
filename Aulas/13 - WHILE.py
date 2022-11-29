#WHILE - é um loop utilizado para realizar determinada ação diante de uma determinada condição
#É um loop que sempre vai executar uma condição de acordo com a instrução que foi indicada

import os
os.system('cls')

#WHILE Simples
num=0 #Variavel para iniciar o loop
while num < 10: #Condição 
        print("WHILE simples") #Mensagem a ser exibida
        num=num+1 #Incremento da variavel
        print("Fim do loop \n")

#WHILE com Break
num2=0
while num2 < 10:
    print("Exemplo com IF e BREAK")
    num2=num2+1
    if (num2 == 5):
        break #Caso a condição do IF seja atingida, o BREAK vai finalizar a execução
    print("Fim do loop \n")

#WHILE com condição OR
num3=0
while num3 == 0 or num3 < 5:
    print("Exemplo com OR")
    num3=num3+1
    print("Fim do loop \n")

#WHILE com condição AND
num4=1
while num4 > 0 and num4 == 1:
    print("Exemplo com AND")
    num4=num4+1
    print("Fim do loop \n")

#WHILE com Array
frutas=["pera","banana","laranja","manga","morango"] #Lista de frutas
i=0 #variavel para iniciar loop
tamanho=len(frutas) #tamanho da lista criada
while i < tamanho: #condição para o loop
    print(frutas[i]) #Exibe a lista com o indice em i, ou seja, a variavel que for incrementada
    i=i+1 #incremento da variável
    print("Fim do loop \n")
    
    os.system('cls')

#WHILE com FOR
carros=[] #Cria uma lista vazia
carro=input("Digite o nome do carro: ") #Usuário insere novos carros
while carro != "fim": #Enquanto o que for digitado ser diferente da palavra fim, o usuario pode adicionar mais carros 
    carros.append(carro) #Comando para adicionar carros a lista
    carro=input("Digite o nome do novo carro: ") #Usuário insere novos carros

os.system('cls') #Limpa a tela

for x in carros: #cria uma variavel e assimila a lista
    print(x) #Exibe o conteudo adicionado a lista

print("\nFim do loop")



