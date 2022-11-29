#ITERATOR - é uma forma de manipularmos listas criadas, assim como é feito no loop FOR
#É possivel criar um iterator, armazenar em um array e utilizar comandos para manipularmos a lista

#ITERATOR SIMPLES
frutas=["Maca","Manga","Melancia","Morango","Melao"] #Lista criada
itFrutas=iter(frutas) #iterator criado
print(next(itFrutas)) #Comando para percorrer a lista

#ITERATOR COM WHILE
while itFrutas:
    try:
        print(next(itFrutas))
    except StopIteration:
        print("Fim da lista!")
        break
