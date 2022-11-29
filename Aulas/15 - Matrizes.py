#MATRIZES - é uma forma de criar listas dentro de listas, indicando indices e colunas
#É possível armazenar, gerenciar, alterar, adicionar e etc. em várias listas utilizando as matrizes

#Matriz
carros=[ #Variavel que armazena a matriz / as listas
        ["Modelo","Carro1"], #Linha 0 | Coluna 0 = Modelo, Coluna 1 = Carro1
        ["Fabricante","Fabricante1"], #Linha 1 | Coluna 0 = Fabricante, Coluna 1 = Fabricante1
        ["Ano","2010"] #Linha 1 | Coluna 0 = Ano, Coluna 1 = 2010
]

print(carros[0][0]) #Exibe a variavel e os indices indicados: Modelo | Carro1

#Alterando um item ou posição
carros[0][1]="carro0"
print(carros[0][1])

#Matriz com FOR
#FOR pega os indices de acordo com as variaveis definidas e percorre a lista

frutas=[
    ["Feira","Morango"],
    ["Mercado","Banana"],
    ["Hortifruit","Melancia"]
]

#Variavel linha: indice 0
#Variavel coluna: indice 1
for linha, coluna in frutas:
    print("Linha: " + linha+ " | " + "Coluna: " + coluna)




