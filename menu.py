import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ""

def menu():
    print('\nOlá, bem vindo(a) ao Me With Me!\033[1;31m♡\033[0;0m\n'  +
          '\nPor favor, escolha uma das opções abaixo: \n\n'            +
          '\033[1;31m▹\033[0;0m1. Exercìcio para Insegurança.\n'                            +
          '\033[1;31m▹\033[0;0m2. Consulte suas respostas - Insegurança.\n'                              +
          '\033[1;31m▹\033[0;0m3. Excluir exercicio - insegurança.\n'                 +
          '\033[1;31m▹\033[0;0m4. Exercìcio para Rotulação.\n'                   +
          '\033[1;31m▹\033[0;0m5. Consulte suas respostas - Rotulação.\n'                       +
          '\033[1;31m▹\033[0;0m6. Excluir exercicio - Rotulação.\n'                         +
          '\033[1;31m▹\033[0;0m0. Sair\n')
    this.opcao = int(input())
def operacao():
    while (this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('\nOlá, bem vindo(a)! \n\n' +
          'Você fará agora um exercício para te ajudar a duvidar dos seus pensamentos ruins.\n'  +
          ' \n' +
          'Por favor, responda as seguintes questões sendo sempre honesto(a) com você mesmo(a).'
          ''
          'Repita o exercicio sempre que julgar necessario.\n' +
          ' \n' +
          '\033[1;31m *Atenção!! Este exercicio NÃO substitui ajuda psicológica, procure também ajuda profissional.\033[0;0m \n' +
          ' \n' +
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
          ' \n' +
          '\033[1;34mPergunta 1. \033[0;0m Neste momento, o que está te deixando inseguro(a)?\n' +
          '\n')
            perg1 = input()
            print('\033[1;34mPergunta 2. \033[0;0m De 0 a 100, qual a chance disso acontecer?')
            perg2 = input()
            print('"\033[1;34m"Pergunta 3.\033[0;0m O que prova que esta porcentagem está correta?'
                  ' \n' +
                  'Evite começar a resposta com "eu acho" ou "eu sinto". \n'
                  'Considere somente o que você já tem certeza. E lembre-se, um evento não dá nenhuma certeza a outro, não generalize.')
            perg3 = input()
            print('\033[1;34m Pergunta 4.\033[0;0m O que me prova que isso realmente vai acontecer?')
            perg4 = input()
            print('\033[1;34mPergunta 5.\033[0;0m Por fim, se acolha. Que conselho você daria a um amigo(a) que estivesse passando por esta situação?')
            perg5 = input()
            # Chamar o método inserir
            operacoes.inserir1(perg1, perg2, perg3, perg4, perg5)
            operacoes.fim()
        elif this.opcao == 2:
            operacoes.consultar1()
            operacoes.fim()
        elif this.opcao == 3:
            print("Por favor, informe o código do exercício que deseja excluir:")
            this.codigo = int(input())
            operacoes.excluir1(this.codigo)
            operacoes.fim()
        elif this.opcao == 4:
            print('\nOlá, bem vindo(a)! \n\n' +
                  'Você fará agora um exercício para te ajudar a duvidar dos seus pensamentos ruins.\n' +
                  ' \n' +
                  'Por favor, responda as seguintes questões sendo sempre honesto(a) com você mesmo(a).'
                  ''
                  'Repita o exercicio sempre que julgar necessario.\n' +
                  ' \n' +
                  '\033[1;31m *Atenção!! Este exercicio NÃO substitui ajuda psicológica, procure também ajuda profissional.\033[0;0m \n' +
                  ' \n' +
                  '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
                  '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
                  ' \n' +
                  '\033[1;34mPergunta 1. \033[0;0mO que acho que eu sou? (Descreva com adjetivos).\\n' +
                  '\n')
            perg6 = input()
            print(
            '\033[1;34mPergunta 2.\033[0;0m O que significam estas palavras? (Pesquise o significado de cada um dos adjetivos aos quais você se atribuiu.)')
            perg7 = input()
            print(
            '\033[1;34mPergunta 3.\033[0;0m  Depois desta pesquisa, você realmente acha que se encaixa nestas descrições?')
            perg8 = input()
            print(
            '\033[1;34mPergunta 4. \033[0;0m Se pergunte: Que prova tenho de que isso é real? (Leve em consideração somente FATOS).')
            perg9 = input()
            print(
                '\033[1;34mPergunta 5.\033[0;0m Por fim, se acolha. Você atribuiria estes adjetivos a um amigo(a) seu?')
            perg10 = input()
        # Chamar o método inserir
            operacoes.inserir2(perg6, perg7, perg8, perg9, perg10)
            operacoes.fim()
            break
        elif this.opcao == 5:
            operacoes.consultar2()
            operacoes.fim()
        elif this.opcao == 6:
            print("Por favor, informe o código do exercício que deseja excluir:")
            this.codigo = int(input())
            operacoes.excluir2(this.codigo)
            operacoes.fim()
        elif this.opcao == 0:
             print('Tchau! volte sempre que precisar conversar, você com você mesmo.\033[1;31m♡\033[0;0m \n.')
        else:
             print('Desculpe, mas a opção escolhida não é válida! Tente novamente.')























