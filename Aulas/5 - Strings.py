#STRINGS - São variáveis que contem valores em textos ou caracteres

curso = "Curso de Python"
print(curso)

print("A primeira letra da string eh: " + str(curso[0])) #Vai indicar o indice selecionado, neste caso a letra "C"

print("Do indice 0 ao indice 5: " + str(curso[0:5])) #Vai indicar 2 indices, do 0 - "C" ao 5 - "o"

print("Tamanho: " + str(len(curso))) #Vai retornar o tamanho da string armazenada na variável

print("Retirando os espacos da frase: " + str(curso.strip())) #Retira espaços vazios da string (caso haja)

print("Convertendo o texto para letras minusculas: " + str(curso.lower())) #Vai converter a string para letras minusculas

print("Convertendo o texto para letras maiusculas: " + str(curso.upper())) #Vai converter a string para letras maiusculas

print("Substituindo a terceira palavra: " + str(curso.replace("Python","Programacao"))) #Vai substituir a palavra "Python" para "Programacao"

print("Indicando uma condicao para criacao de indices: " + str(curso.split(" "))) #Vai converter a variável em um Array criando um indice para cada palavra separada por um espaço. 
                        #Neste caso é possível indicar o que desejar dentro do SPLIT
