# INPUT - é um comando para armazenarmos um valor em uma variável que seja definido pelo usuário
# O programa vai solicitar que o usuário digite um conteudo e esse conteudo será armazenado na variável que for definida

import os
# Configuração para limpar a tela automaticamente quando for rodar o programa
os.system('cls')

#INPUT - STRING
nome = input("Digite o seu nome: ")

#INPUT - INT
idade = int(input("Digite a sua idade: "))

#INPUT - FLOAT
altura = float(input("Digite a sua altura: "))

print("Voce se chama " + str(nome) + ", esta com " + str(idade) +
      " de idade e mede " + str(altura) + " de altura")

# INPUT - SOMA DE VALORES
# STRING
numero1 = input("\nDigite o primeiro numero: ")
numero2 = input("Digite o segundo numero: ")
print("Resultado: " + numero1+numero2)

# INT
numero3 = int(input("\nDigite o primeiro numero: "))
numero4 = int(input("Digite o segundo numero: "))
print("Resultado: " + str(numero3+numero4))
