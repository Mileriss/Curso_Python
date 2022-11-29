#FOR - Serve para percorrer sobre coleções e realizar determinadas ações
#WHILE - Serve para realizar uma determinada ação de acordo com a condição que for estabelecida

carros=["Carro0","Carro1","Carro2","Carro3","Carro4","Carro5"]
print(carros)

for x in carros: #x é a variavel criada e IN é para identificar qual lista desejamos percorrer
    print(x)
    if x == "Carro0": #Realiza uma verificação
        print("  BMW") #Caso a verificação seja verdadeira, exibe BMW abaixo do indice 0

texto="Texto de exemplo"
for y in texto:
    print(texto) #Vai ser exibido a string 16 vezes porque é a quantidade de elementos que contem na variavel

texto2="Texto de exemplo 2"
for z in texto2:
    print(texto2)
    break #Vai exibir apenas 1 resultado da string porque é um comando de parada
          #Ou seja, quando a condição é atingida, este comando interrompe a ação
