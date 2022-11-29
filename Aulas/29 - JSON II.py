import json

def linha():
    print("----------------------------")

jogador_json='{"Nome":"Rafael", "Time":"soldado", "Vivo":"True", "Energia":"100", "Mochila":["faca","arma","corda","martelo","arame"], "Transporte":[{"Aviao":"transporte","Energia":"100","Forca":"80"}, {"Caminhao":"transporte","Energia":"100","Forca":"200"}, {"Moto":"transporte","Energia":"100","Forca":"60"}]}'


jogador=json.loads(jogador_json)

#ITEMS
for i in jogador.items():
    print("Items:" + str(i))
linha()

#VALORES
for v in jogador.values():
    print("Valores:" + str(v))
linha()

#Nome do jogador
print("Nome do jogador: " + str(jogador["Nome"]))
linha()

#ITEMS DA MOCHILA
for im in jogador["Mochila"]:
    print("Items da mochila: " + str(im))
linha()


for a in jogador["Transporte"]:
    print("Valores de Transporte: " + str(a["Energia"]))
linha()

