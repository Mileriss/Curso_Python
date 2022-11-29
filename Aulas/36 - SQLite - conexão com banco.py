#SQLite - é o banco de dados que vamos utilizar para gravar, editar, excluir e armazenar registros
#Com a conexão de banco de dados é possivel deixar tudo armazenado de forma segura no sistema

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
