#CREATE TABLE - é utilizado para criar tabelas no banco de dados
#Ao criar uma tabela no banco de dados, é possivel indicar um campo para cada tipo de informação e posteriormente adicionar dados/valores

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

#Criar tabela
vsql="""
CREATE TABLE tb_contatos(
    N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOMECONTATO VARCHAR(30),
    T_TELEFONECONTATO VARCHAR(15),
    T_EMAILCONTATO VARCHAR(30)
);
"""

def CriarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada!")
    except Error as ex:
        print(ex)

CriarTabela(vcon,vsql)

vcon.close()

