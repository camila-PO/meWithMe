import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ""

def menu1():
    print('\nEscolha um dos exercicios abaixo: \n\n' +
          '1. Exercìcio para Insegurança.\n'                        +
          '2. Exercicio para Rotulações.\n'                        +
          '0.Sair\n')
    this.opcao = int(input())
def operacao():
    while (this.opcao != 0):
        menu1()
        if this.opcao == 1:
            print('\nOlá, bem vindo(a)! \n\n' +
          'Você fará agora um exercício para te ajudar a duvidar dos seus pensamentos ruins.\n'  +
          'Por favor, responda as seguintes questões, sendo honesto(a) com você mesmo(a). Faça quantas vezes precisar!\n' +
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
          'Pergunta 1. Neste momento, o que está te deixando inseguro(a)?\n' +
          '\n')
            perg1 = input()
            print('Pergunta 2. De 0 a 100, qual a chance disso acontecer?')
            perg2 = input()
            print('Pergunta 3. O que prova que esta porcentagem está correta? Evite começar a resposta com "eu acho" ou "eu sinto." \n'
                  'Considere somente o que você já tem certeza. E lembre-se, um evento não dá nenhuma certeza a outro, não generalize.')
            perg3 = input()
            print('Pergunta 4. O que me prova que isso realmente vai acontecer?')
            perg4 = input()
            print('Pergunta 5. Por fim, se acolha. Que conselho você daria a um amigo(a) que estivesse passando por esta situação?')
            perg5 = input()
            # Chamar o método inserir
            operacoes.inserir(perg1, perg2, perg3, perg4, perg5)

        elif this.opcao == 2:
            print('\nOlá, bem vindo(a)! \n\n' +
                  'Você fará agora um exercício para te ajudar a se livrar de rotulações.\n' +
                  'Por favor, responda as seguintes questões, sendo honesto(a) com você mesmo(a). Faça quantas vezes precisar!\n' +
                  '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
                  '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' +
                  'Pergunta 1. O que acho que eu sou? (Descreva com adjetivos).\n' +
                  '\n')
            perg6 = input()
            print('Pergunta 2. O que significam estas palavras? (Pesquise o significado de cada um dos adjetivos aos quais você se atribuiu.)')
            perg7 = input()
            print(
                'Pergunta 3. Depois desta pesquisa, você realmente acha que se encaixa nestas descrições?')
            perg8 = input()
            print('Pergunta 4. Se pergunte: Que prova tenho de que isso é real? (Leve em consideração somente FATOS).')
            perg9 = input()
            print(
                'Pergunta 5. Por fim, se acolha. Você atribuiria estes adjetivos a um amigo(a) seu?')
            perg10 = input()
            # Chamar o método inserir
            operacoes.inserir(perg6, perg7, perg8, perg9, perg10)
        else:
            print('Opção escolhida não é válida!')



