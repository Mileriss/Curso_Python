import os

#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binário

#OPEN - é um comando para criarmos e editarmos arquivos utilizando comandos em Python
nomeArquivo="teste.txt"
arquivo=open("C:/Users/Rafael Mileris/OneDrive/CFB Cursos/Python/Arquivos Criados em aula/" + nomeArquivo,"w") #W - indicando o Write
texto=input("Digite um texto: ")
arquivo.write(texto + "\n")

#READLINE - é uma maneira de conseguirmos realizar a leitura do arquivo criado com o comando OPEN
print(arquivo.readline()) #realiza a leitura de uma linha do arquivo

#REMOVE - é uma maneira de conseguirmos deletar arquivos que foram criados ou que desejamos remover do nosso computador
#É necessário importar a biblioteca 'os'
os.remove(arquivo)





