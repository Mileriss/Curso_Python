#LIST - ARRAY, é uma forma de criar uma lista de elementos que você desejar e alocando cada um em indices
#O indice de um array SEMPRE começa em 0

carros=["Carro0","Carro1","Carro2","Carro3","Carro4","Carro5","Carro6","Carro7","Carro8","Carro9","Carro10"] #Adiciona os itens a uma lista

carros[1]="Carro11" #Altera o item do indice 1 (Audi)

print(carros[1]) #Exibe o item no indice 1 (Chevete)

carros.append("Carro12") #Adiciona um novo item a lista

carros.remove("Carro11") #Remove um item da lista

carros.pop() #Remove o ultimo item da lista

del carros[1] #Remove o item que você definir no indice

print(str(len(carros)) + " carros na lista") #Exibe a quantidade de itens da lista

print(carros)

carros2 = list(carros) #Copia todo o conteudo da lista para a variavel que você definiu

print(carros2)

carros3 = carros+carros2  
print(carros3)