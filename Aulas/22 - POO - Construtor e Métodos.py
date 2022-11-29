#CONSTRUTOR - é um método que será chamado quando um objeto da classe for instanciado
#__init__ - é a maneira de definir um método (construtor)
#self - é uma referencia para a propria classe

class Carro(): #Classe 
    velMaxima=0 #Atributos
    ligado=False #Atributos
    cor="" #Atributos

    def __init__(self,v, l, c): #Método
        self.velMaxima=v #Definição do método
        self.ligado=l #Definição do método
        self.cor=c #Definição do método


    def mostrar(self): #Função mostrar
        print("Velocidade maxima: " + str(self.velMaxima))
        print("Cor:................: " + (self.cor))
        print("Ligado:.............: " + str(self.ligado))
        estado="Sim" if self.ligado else "Nao"
        print("Ligado:.............: " + estado)
        print("--------------------------")

    def ligar(self): #Função Ligar
        self.ligado=True
    def desligar(self): #Função desligar
        self.ligado=False
    def andar(self): #Função andar
        if self == True:
            print("Andando")
        else:
            print("Parado")
        
c1=Carro(200,False,"Preto") #Atribuição do objeto 1
c2=Carro(180,False,"Branco") #Atribuição do objeto 2
c3=Carro(220,False,"Vermelho") #Atribuição do objeto 3

c1.ligar() #Exibição das funções do objeto 1
c1.mostrar()
c1.andar()

c2.desligar() #Exibição das funções do objeto 2
c2.mostrar()
c2.andar()

c3.ligar() #Exibição das funções do objeto 3
c3.mostrar()
c3.andar()