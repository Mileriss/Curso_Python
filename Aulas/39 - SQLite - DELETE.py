#DELETE - é utilizado para excluirmos informações que já foram inseridas na tabela
#Com esse comando, caso desejarmos, é posivel realizar a exclusão de registros especificos ou excluir toda a tabela.

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

valor_sql="DELETE from tb_contatos WHERE N_IDCONTATO=1"

def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido!")

deletar(vcon,valor_sql)