 #RegEx SUB - é utilizado para realizar alterações em um parametro especifico da String
 #É possivel indicar novos parametros ou alterar parametros já existentes

import re #Biblioteca RegEx

texto="Meu nome eh Rafael, Lopes, Mileris" #String Criada

resultado=re.sub("\s","-",texto) #\s -> espaço em branco: todos os espaços em branco serão alterados para o simbolo -
resultado=re.sub(",",".",resultado) #Todas as virgulas serão substituidas por pontos
print(resultado) #Exibe o resultado



