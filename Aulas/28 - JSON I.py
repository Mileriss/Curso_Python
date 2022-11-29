#JSON - é possivel ler e criar arquivos JSON em Python e tambem arquivos JSON externos
#O mesmo aprendizado do DICTIONARY pode ser usado para manipular os arquivos JSON

import json #Biblioteca JSON

carros_json='{"Marca":"honda","Modelo":"HRV","Cor":"prata"}' #Arquivo JSON criado

#Transforma o arquivo json em uma string
carros=json.loads(carros_json)
print(carros)

#Exibir um valor especifico do documento
print(carros["Modelo"])

#FOR
carros=json.loads(carros_json)

#Exibe os itens
for c in carros.items():
    print(c)

#Exibe os valores
for c in carros.values():
    print(c)

#DICTIONARY
carros={
    "Marca":"honda",
    "Modelo":"HRV",
    "Cor":"prata"
}

carros_json=json.dumps(carros) #DICTIONARY -> objeto JSON
print(carros_json)

#ARRAY
carros_lista=["honda","wolkswagem","ford","fiat","chevrolet"]
lista_json=json.dumps(carros_lista) #ARRAY -> array JSON
print(lista_json)

#TUPLA
#JSON não aceita tuplas, as tuplas são convertidas em Arrays JSON
carros_tupla=("honda","wolkswagem","ford","fiat","chevrolet")
tupla_json=json.dumps(carros_tupla) #ARRAY -> array JSON
print(tupla_json)