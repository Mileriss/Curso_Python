#LAMBDA - são funções anonimas e simples de declarar
#É fácil de realizar operações com as funções lambdas, por exemplo não é necessário se preocupar com definição de nome ou definir a propria função

#1
soma=lambda a,b:a+b
resultado=soma(10,20)
print(resultado)

#2
soma=lambda a,b:a+b
print(soma(10,20))

#3
soma=lambda a,b,c:(a+b)*c
print(soma(10,10,2))

#4
print((lambda a,b:a+b)(10,5))

#5
operacao=lambda x,func:x+func(x)
resultado=operacao(2, lambda x:x*x)
print(resultado)

#6
resultado=operacao(2, lambda x:x+x)
print(resultado)


