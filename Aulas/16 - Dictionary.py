#DICTIONARY - é uma coleção aberta onde podemos adicionar, remover, editar os valores.
#É utilizado {} para adicionar os valores, indicando cada valor dentro de chaves individuais

from stat import FILE_ATTRIBUTE_READONLY


carro={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2010",
    "Cor":"Preto"
}
print(carro) #Exibe todos os resultados

carro["Cor"]="Prata" #Altera o valor da COR

for x in carro:
    print(carro[x]) #Percorre os valores e exibe na tela

for chave, valor in carro.items(): #Variavel chave para o primeiro indice | variavel valor para o segundo indice
    print(chave + " : " + valor) #Exibe os valores dos itens

print("Tamanho do Dictionary: " + str(len(carro))) #Quantidade de listas

carro["Cambio"]="Automatico" #Adiciona um elemento
carro.pop("Cambio") #Remove um elemento

carro.clear() #Remove tudo do Dictionary

print(carro)

#Criar varios dictionary
frutas={
    "Feira":{
        "Morango":"Doce",
        "Melao":"Azedo",
    },
    "Mercado":{
        "Banana":"Verde",
        "Melancia":"s/caroco"
    },
    "Hortifruit":{
        "Jabuticaba":"Azul",
        "Mamao":"Papaya"
    }
}

print(frutas["Feira"])
print(frutas["Hortifruit"])
print(frutas["Mercado"])

for x in frutas:
    print(frutas[x])


