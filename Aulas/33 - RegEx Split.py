#RegEx SPLIT - é utilizado para retirar ou esconder parametros especificos indicados com o comando re.split
#É possivel verificar e retirar um parametro especifico de uma STRING, indicando espaços em branco no lugar do parametro

import re #Biblioteca RegEx

texto="Meu nome eh Rafael Lopes Mileris" #String criada
resultado=re.split("e",texto) #Resultado recebe os parametros para o SPLIT
print(resultado) #Exibe o resultado sem o parametro indicado anteriormente
print(resultado[2]) #Define um indice especifico

for r in resultado:
    print(r)