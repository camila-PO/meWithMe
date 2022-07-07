import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados
import menu
db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserir(perg1, perg2, perg3, perg4, perg5):
    try:
        sql = "insert into inseguranca (codInsegura, perg1, perg2, perg3, perg4, perg5) values('', '{}', '{}','{}', '{}', '{}')".format(perg1, perg2, perg3, perg4, perg5)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro


def consultar():
    try:
        sql = 'select * from inseguranca'
        con.execute(sql)

        for(codigo, perg1, perg2, perg3, perg4, perg5) in con:
            print('Código: {}, Resposta refente a pergunta 1: {}, Resposta refente a pergunta 2: {}, Resposta refente a pergunta 3 {}, Resposta refente a pergunta 4 {},Resposta refente a pergunta 5 {}, '.format(perg1, perg2, perg3, perg4, perg5))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, campo, novoDado):
    try:
        sql = "update inseguranca set {} = '{}' where codInsegura = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir(cod):
    try:
        sql = "delete from inseguranca where codInsegura = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def inserir2 (perg6, perg7, perg8, perg9, perg10):
    try:
        sql = "insert into rotulacao (codRotu, perg6, perg7, perg8, perg9, perg10) values('', '{}', '{}','{}', '{}', '{}')".format(perg6, perg7, perg8, perg9, perg10)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro


def consultar2():
    try:
        sql = 'select * from rotulacao'
        con.execute(sql)

        for(codRotu, perg6, perg7, perg8, perg9, perg10) in con:
            print('Código: {}, Resposta refente a pergunta 1: {}, Resposta refente a pergunta 2: {}, Resposta refente a pergunta 3 {}, Resposta refente a pergunta 4 {},Resposta refente a pergunta 5 {}, '.format(perg1, perg2, perg3, perg4, perg5))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar2(cod, campo, novoDado):
    try:
        sql = "update rotulacao set {} = '{}' where codRotu = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir2(cod):
    try:
        sql = "delete from rotulacao where codRotu = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)