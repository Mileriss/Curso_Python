#DATAS - é possivel especificar e detalhar datas utilizando 'chaves' especificas 
#É possivel exibir datas inteiras, parciais ou detalhadas

import datetime
from time import strftime #Importe a biblioteca de datas

#Exibe a data atual
data=datetime.datetime.now()
print(data)

#data.day - dia atual
#data.month - mês atual
#data.year - ano atual
print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))

#Definindo uma data especifica como parametro
nascimento=datetime.datetime(1997,11,30) 
print(nascimento)

#STRFTIME - Permite usar chaves para detalhar o tipo e formato da data
print(nascimento.strftime("%A \n")) #Exibe o dia da semana que você informou


#%a - Texto: dia da semana (abreviado)
print(strftime("%a"))

#%A - Texto: dia da semana (inteiro)
print(strftime("%A"))

#%b - Texto: Mês (abreviado)
print(strftime("%b"))

#%B - Texto: Mês (Inteiro)
print(strftime("%B"))

#%w - Numero: dia da semana
print(strftime("%w"))

#%d - Numero: dia do mês
print(strftime("%d"))

#%m - Numero: Mês
print(strftime("%m"))

#%y - Ano (2 digitos)
print(strftime("%y"))

#%Y - Ano (4 digitos)
print(strftime("%Y"))

#%H - Hora (2 digitos: 00h - 23h)
print(strftime("%H"))

#%I - Hora (2 digitos: 00h - 12h)
print(strftime("%I"))

#%p - AM/PM
print(strftime("%p"))

#%M - Minutos
print(strftime("%M"))

#%S - Segundos
print(strftime("%S"))

#%f - Micro-Segundos
print(strftime("%f"))

#%j - Dia do ano (001 - 365)
print(strftime("%j"))

#%W - Numero: Semana do ano
print(strftime("%W"))
