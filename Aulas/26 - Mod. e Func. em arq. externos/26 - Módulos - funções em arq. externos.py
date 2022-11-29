#MÓDULOS / FUNÇÕES EM ARQUIVOS EXTERNOS - é possível criar um arquivo na pasta com um trecho de código e importar para um novo arquivo
#É necessário que ambos os arquivos estejam na mesma pasta, caso contrário, não é possivel realizar a importação

#Foi criado um arquivo chamado 'teste' na mesma pasta que o arquivo da aula

import teste #importe o arquivo criado
teste.jogador() #chame a função criada no arquivo, a sintaxe é: nome_do_arquivo.nome_da_função()

import teste as ts #Altera o nome do arquivo
ts.jogador()

from teste import jogador #Vai chamar apenas a função do arquivo criado
jogador()