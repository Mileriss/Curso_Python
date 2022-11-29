#HERANÇA - tem como objetivo transferir todos os atributos de uma classe "PAI" para uma classe "Filho"
#Ou seja, tudo que for atribuido a uma classe pai, com o metodo de herança, é possivel passar para outras classes
#Classe pai - Super classe
#Classe filho - Sub-classe

class NPC: #Classe Pai / Super classe
    def __init__(self,nome,time,forca,municao): #Metodo construtor
        self.nome=nome #parametros
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self): #função
        print("Nome......: " + self.nome)
        print("Time......: " + str(self.time))
        print("forca.....: " + str(self.forca))
        print("municao...: " + str(self.municao))
        print("vivo......: " + str( "sim" if self.vivo else "nao"))
        print("energia...: " + str(self.energia))
        print("------------------------------------")

#Ao criar um construtor para a classe filho, os parametros vão sobrescrever o contrutor da classe pai
#ou seja, as novas informações vão substituir as informações da classe pai
class Soldado(NPC):
    def __init__(self,nome,time): #Construtor - Classe filho
        self.forca=200 #parametros
        self.municao=200
        #SUPER - vai invocar os parametros da classe pai, o que foi criado na classe pai, ao utilizar o super, será passado para a classe filho.
        super().__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self,nome,time):
        self.forca=100
        self.municao=20
        super().__init__(nome,time,self.forca,self.municao)

class Elite(NPC):
    def __init__(self,nome,time):
        self.forca=400
        self.municao=500
        super().__init__(nome,time,self.forca,self.municao)

#Criando os objetos da classe
s1=Guarda("Guarda 1",1)
s2=Soldado("Soldado 1",1)
s3=Elite("Elite 1",1)
s4=Guarda("Guarda 2",2)
s5=Soldado("Soldado 2",2)
s6=Elite("Elite 2",2)

s1.vivo=False #condição
s6.vivo=False

s1.info() #Exibe as informações criadas
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()