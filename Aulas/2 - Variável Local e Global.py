#Variável Global
#São as variáveis que a gente define e podem ser utilizadas em qualquer lugar do nosso código.
num1=num2=num3=0
print(num1)
print(num2)
print(num3)


#Variável Local
#São as variáveis que a gente define dentro de funções e ficam disponíveis apenas dentro do escopo da função, não sendo permitido o uso delas fora da função.
#A variável local não será acessada ou exibida na tela, somente se você converter ela para uma variável global
def numeros():
    global numero1, numero2, numero3 #Definindo a variavel como Global
    numero1=10 #Atribuindo um valor a variável
    numero2=20
    numero3=30
    
numeros() #Chamando a função criada
print(numero1)
print(numero2)
print(numero3)
    