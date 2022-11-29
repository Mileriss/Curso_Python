#Boolean é o tipo de variável que vai retornar TRUE ou FALSE como resultado de uma operação

fato=10<15 #TRUE - 10 é menor que 15
print(fato)
fato=10>15 #FALSE - 10 não é maior que 15
print(fato)

texto="Vai retornar True"
print(bool(texto)) #String convertido para Boolean e retorna TRUE porque tem conteudo na variavel
texto=""
print(bool(texto)) #String convertido para Boolean e retorna FALSE porque não tem conteudo na variavel

if texto:
    print("Possui texto") #TRUE
else:
    print("Nao possui texto") #FALSE
