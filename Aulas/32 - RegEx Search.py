#RegEx SEARCH - Indica a posição onde está localizada a pesquisa que for realizada
#Assim como em listas, o indice começa em 0 

import re #Importe a biblioteca RegEx

texto="Meu nome eh Rafael Lopes Mileris" #String criada

pesquisa=input("Digite o que deseja visualizar: ") #Solicita interação
resultado=(re.search(pesquisa,texto)) #Indica o RegEx, o comando e as variaveis como parametros de busca

pos_inicial=("A palavra pesquisada começa no: " + str(resultado.start()) + " caractere") #Indica a posição inicial da busca
print(pos_inicial)
pos_final=("A palavra pesquisada termina no: " + str(resultado.end()) + " caractere") #Indica a posição final da busca
print(pos_final)


