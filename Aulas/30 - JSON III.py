#JSON III - foi criado um arquivo com extensão .json
#No procedimento abaixo esta detalhado a importação do arquivo JSON

import json

#Indicando o caminho onde o JSON está armazenado nos arquivos do computador
#indicar o nome do arquivo na ultima parte da string
#Alterar todas as barras: \ -> /
#Indicar o 'as' e atribuir a uma variavel: as nome_da_variavel

with open('C:/Users/Rafael Mileris/OneDrive/CFB Cursos/Python/Aulas/30 - JSON - Importando arquivo.py/jogador.json') as f:
    jogador=json.load(f) #Indicar o comando para converter em JSON

print(jogador.items())