#UPDATE - é o comando utilizado para realizar alterações em informações da tabela
#É possivel modificar as informações de um registro que consta no banco de dados, utilizando parametros especificos para a busca

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

valor_sql="UPDATE tb_contatos SET T_NOMECONTATO='Rafael', T_TELEFONECONTATO='(11)99452-1196', T_EMAILCONTATO='rafael@teste.com.br' WHERE N_IDCONTATO=2"

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado!")

atualizar(vcon,valor_sql)