import random #Biblioteca para operações com Random

#TIPOS NUMERICOS - São variáveis que contem valores numericos, como: INT, FLOAT e COMPLEX
num1 = 10 
num2 = 10.5
num3 = 1j

print(num1)
print(num2)
print(num3)


#CASTING - É a operação de converter um tipo de variável para outro, por exemplo: INT -> STRING
#1
print("Valor: " + str(num1) + " eh do tipo " + str(type(num1))) #STR - realiza a conversão do tipo INT para o tipo STRING
#2
num1 = float(10) #Converte a variável INT para FLOAT
print("Valor: " + str(num1) + " eh do tipo " + str(type(num1)))
#3
num2 = int(10.5) #Converte a variável FLOAT para INT
print("Valor: " + str(num2) + " eh do tipo " + str(type(num2)))
#4
num3 = complex(10) #Converte a variável INT para COMPLEX
print("Valor: " + str(num3) + " eh do tipo " + str(type(num3)))

#.FORMAT - É a conversão de variaveis realizada diretamente na linha de comando
#É definido de acordo com a ordem dos colchetes {}
#O primeiro {} vai corresponder a primeira variavel indicada no .format
nome="Rafael"
sobrenome="Mileris"
idade=24
altura=1.75
sexo='Masculino'
print("O seu nome eh {} {}, voce tem {} anos e mede {} de altura, do sexo {}" .format(nome,sobrenome,idade,altura,sexo))



#RANDOM - É uma função para gerar valores aleatórios na tela.
#IMPORT RANDOM - É a biblioteca que vai disponibilizar essa operação
num_Aleatorio = random.randrange(0,60) #Vai gerar um numero entre 0 e 60 aleatoriamente
print(num_Aleatorio) #Vai exibir um numero aleatorio entre as condições propostas acima

#RANDOM COM ARRAY - Vai gerar valores aleatorios para diferentes posições do Array
num_Aleatorio2 = [
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60)
    ]

print("Valor 1: " + str(num_Aleatorio2[0]))
print("Valor 2: " + str(num_Aleatorio2[1]))
print("Valor 3: " + str(num_Aleatorio2[2]))
print("Valor 4: " + str(num_Aleatorio2[3]))
print("Valor 5: " + str(num_Aleatorio2[4]))
print("Valor 6: " + str(num_Aleatorio2[5]))