#RegEX Findall - é um recurso para conseguirmos pesquisar e retornar parametros especificos em variáveis
# É possivel verificar determinadas palavras, letras e etc. Especificas em variaveis / strings que foram criadas
# Desta forma, caso precise realizar alguma pesquisa especifica, o FINDALL auxilia bastante

import re #Biblioteca RegEx

texto="Meu nome eh Rafael Lopes Mileris" #Crie uma string
pesquisa=input("Digite o que deseja pesquisar: ") #Input para solicitar uma interação do usuário
resultado=re.findall(pesquisa,texto) #Resultado vai receber os parametros RegEx Findall: variavel > re (RegEx) > . > findall > (variaveis)
print(resultado) #Exibe o resultado

quantidade=len(resultado) #Recebe a quantidade de resultados encontrados
print("quantidade" + str(quantidade)) #Exibe a quantidade de resultados

for t in resultado: #Percorre todo o resultado 
    print(t) #Exibe todos os conteudos 
