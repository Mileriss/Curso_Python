#SELECT - é a maneira para consultarmos regitros em uma tabela, utilizando 'querys' especificas 
#QUERY - é o nome utilizado para identificar os comandos criados em banco de dados
#Com as querys é possivel estipular pesquisas especificas para localizar qualquer tipo de informação

import sqlite3 #Importando o banco de dados
from sqlite3 import Error #importando os erros do banco de dados, para realizarmos o tratamento necessário

#Criar conexão do banco de dados
def ConexaoBanco():
    caminho="C:\\Users\\Rafael Mileris\\OneDrive\\Python\\Banco de dados\\Bancos\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
            print(ex)
    return con
vcon=ConexaoBanco()

def consultar(conexao,sql):
        c=conexao.cursor()
        c.execute(sql)
        resultado=c.fetchall()
        return resultado

valor_sql="SELECT * FROM tb_contatos"
resultado=consultar(vcon,valor_sql)

for c in resultado:
    print(c)