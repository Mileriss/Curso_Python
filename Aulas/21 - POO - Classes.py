#POO - Programação Orientada a Objetos
#CLASSE - é o "projeto" que recebe diversas instancias / objetos
#OBJETO - é uma instancia da classe, onde será atribuido um determinado valor a um determinado objeto que representa uma parte de uma classe

class Carro: #classe carro
    velMax=0 #propriedade da classe
    ligado=True #propriedade da classe
    cor="" #propriedade da classe

c1=Carro() #novo objeto 1
c2=Carro() #novo objeto 2
c3=Carro() #novo objeto 3

c1.velMax=200 #atribuição da propriedade da classe no objeto 1
c2.ligado=True #atribuição da propriedade da classe no objeto 2
c3.cor="Vermelho" #atribuição da propriedade da classe no objeto 3

print("A velocidade maxima do carro eh: " + str(c1.velMax))
print("O carro esta ligado? " + str(c2.ligado))
print("A cor do carro eh: " + c3.cor)

#IF Ternário
estado="Sim" if c2.ligado else "Nao" #Se c2 for TRUE = Sim, caso contrário = Nao
print(estado)




