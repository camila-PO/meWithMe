import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados
import menu
import this

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserir1(perg1, perg2, perg3, perg4, perg5):
    try:
        sql = "insert into inseguranca (codInsegura, perg1, perg2, perg3, perg4, perg5) values('', '{}', '{}','{}', '{}', '{}')".format(perg1, perg2, perg3, perg4, perg5)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("	\033[1;37mSuas Respostas foram salvas e estarão sempre disponíveis para que você possa ler e refletir sobre elas.\033[0;0m".format(con.rowcount))
    except Exception as erro:
        return erro


def consultar1():
    try:
        sql = 'select * from inseguranca'
        con.execute(sql)

        for (codInsegura, perg1, perg2, perg3, perg4,perg5) in con:
            try:
                sql = 'select * from inseguranca '
                con.execute(sql)

                for (codInsegura, perg1, perg2, perg3, perg4, perg5) in con:
                    print(
                        '\033[1;34m CODIGO DO EXERCICIO:\033[0;0m {}\n\n Naquele momento, o que estava te deixando(a) inseguro(a)?\n\n \033[1;34m Sua resposta:\033[0;0m {}\n\n O que te provava, naquele momento, que esta porcentagem estava correta?\n\n \033[1;34m Sua resposta:\033[0;0m  {}\n\n O que te provava que isso realmente iria acontecer?\n\n \033[1;34m Sua resposta:\033[0;0m  {}\n\n Por fim, Como você se acolheu? Que conselho você daria a um amigo(a) que estivesse passando por esta situação?\n\n \033[1;34m Sua resposta:\033[0;0m  {}'.format(codInsegura,
                                                                                                          perg1,
                                                                                                          perg2,
                                                                                                          perg3,
                                                                                                          perg4,
                                                                                                          perg5))
                print('\n')
            except Exception as erro:
                print(erro)
    except Exception as erro:
        print(erro)


def excluir1(cod):
    try:
        sql = "delete from inseguranca where codInsegura = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('Exercício de código número {} foi excluido! \033[1;31m♡\033[0;0m '.format(con.rowcount))
    except Exception as erro:
        print(erro)

def inserir2 (perg6, perg7, perg8, perg9, perg10):
    try:
        sql = "insert into rotulacao (codRotu, perg6, perg7, perg8, perg9, perg10) values('', '{}', '{}','{}', '{}', '{}')".format(perg6, perg7, perg8, perg9, perg10)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("{} \033[1;37mSuas Respostas foram salvas e estarão sempre disponíveis para que você possa ler e refletir sobre elas.\033[0;0m".format(con.rowcount))
    except Exception as erro:
        return erro


def consultar2():
    try:
        sql = 'select * from rotulacao'
        con.execute(sql)

        for(codRotu, perg6, perg7, perg8, perg9, perg10) in con:
            print(
                '\033[1;34m CODIGO DO EXERCICIO:\033[0;0m {}\n\n Naquele momento, quais adjetivos você se atrubuiu?\n\n \033[1;34m Sua resposta:\033[0;0m {}\n\n De acordo com sua pesquisa, o que significavam estas palavras?\n\n \033[1;34m Sua resposta:\033[0;0m  {}\n\n Depois desta pesquisa, você realmente acha que se encaixa nestas descrições?\n\n \033[1;34m Sua resposta:\033[0;0m  {}\n\n Que fatos você listou como prova de que isso é real? \n\n \033[1;34m Sua resposta:\033[0;0m  {}\n\n Por fim, você atribuiria estas palavras a um amigo(a)?\n\n \033[1;34m Sua resposta:\033[0;0m  {}\n\n'.format(
                    codRotu,
                    perg6,
                    perg7,
                    perg8,
                    perg9,
                    perg10))
            print('\n')

    except Exception as erro:
        print(erro)

def excluir2(cod):
    try:
        sql = "delete from rotulacao where codRotu = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('Exercício de código número {} foi excluido! \033[1;31m♡\033[0;0m '.format(con.rowcount))
    except Exception as erro:
        print(erro)

def fim():
        print('\033[1;31m▹\033[0;0m1. Voltar ao menu?\n' + '\033[1;31m▹\033[0;0m0. Sair\n')
        abc = int(input())
        if abc == 1:
            menu.operacao()
        elif abc == 0:
            print('Tchau! volte sempre que precisar conversar, você com você mesmo.\033[1;31m♡\033[0;0m \n. ')
        else:
            while abc < 0 or abc > 1:
                print('Desculpe, mas a opção escolhida não é válida! Tente novamente.')
                fim()

