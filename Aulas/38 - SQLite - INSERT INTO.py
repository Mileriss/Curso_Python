#INSERT INTO - é utilizado para criar informações e armazenar nos campos que foram criados na tabela
#Esse comando indica os valores desejados de acordo com cada campo que foi criado na tabela anteriormente

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

nome=input("Digite o nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o email: ")

valor_sql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+nome+"','"+telefone+"','"+email+"')"
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro inserido!")

inserir(vcon,valor_sql)