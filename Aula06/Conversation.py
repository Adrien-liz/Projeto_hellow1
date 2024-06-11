#Sei que não vai ver, mais eu tenho ansiedade skdjskdjsk era isso que eu estava fazendo quando você viu eu no chat gpt. Tinha um erro no código, mas nunca usaria para o curso.
def start():
    print('Uma figura, aparece. Seus cabelos são enrolados compridos, até a cintura. Além da sua coloração azul, o tom de pele claro e uma expressão alegre.')
    print('??:Olá! É um novo dia! Espero que tenha dormido bem')
    print('Meu nome é Mia!, eu sou o novo talking daqui.')

    anykey = input('Envie qualquer coisa para continuar')

    escolha()

    print('Vocês andam mais pra frente, neste caminho estranho. Agora, sua cabeça percebe onde está, o ambiente é branco, como se estivesse dentro de algo, de vez em quando quebras na visão aparecem.')
    print('Você vê, mais duas figuras, na esquerda, um homem. Ele possui cabelos curtos e, apenas um olho bem grande no meio. Na direita, Uma garota com cabelos nos ombros e uma blusa escrito ''yes, i am a talking''.')

    anykey = input('Envie qualquer coisa para continuar')

    print('Figura da esquerda: ... essa é a pessoa que você disse que ia nos mostrar?')
    print('Mia: Sim ué, ela tem o potencial para ser um talking.')

    print('Figura da direita: Maiss!! QUE PESSOA LINDA!!! Você faz skin care? Qual o seu nome? Mais que olhos lindos!')

    escolha1()

    anykey = input("E, fim. Este jogo não está pronto, hehe. Digite qualquer coisa para retornar ao menu principal.")
    mainMenu()


def escolha1():
    print('1.Rosto')
    print('2.Nome')
    print('3.Pele')

    while True:
        try:
            selection = int(input('Coloque a resposta: '))
            if selection == 1:
                rosto()
                break
            elif selection == 2:
                nome()
                break
            elif selection == 3:
                olhos()
                break
            else:
                print('Resposta inválida. Escolha 1-3')
        except ValueError:
            print('Resposta inválida. Escolha 1-3')

def rosto():
    print('Eu.. Nunca fiz skin care não.. Na verdade.')
    print('(Quem sou eu? Eu não lembro..)')

def nome():
        
    name = input('Coloque seu nome:')
    nomes_lindos = ['Noah', 'Gabriel', 'Monica', 'Martha', 'Judas', 'Romeu', 'Claire', 'Iris', 'Charlotte', 'Harry', 'Charlie']

    if name in nomes_lindos:
        print ('??: ' + name + '? que nome mais lindo! eu sempre quis ter o nome de ' + name)
    elif name == 'Adrian':
        print('??: Adrian? esse nome me dá uma sensação estranha....')
    else:
        print('??: ' + name + '? É um nome bonito.')
    
def olhos():
    print('S-sim, eu faço skin care.. eu acho? ou eu não faço?.. Minha cabeça, fica um pouco zonza.')

def escolha():
    print('1.O que são talkins?')
    print('2.Seus cabelos são bonitos')
    print('3.Ahh, entendi...')

    while True:
        try:
            selection = int(input('Coloque a resposta: '))
            if selection == 1:
                conversadores()
                break
            elif selection == 2:
                cabelos()
                break
            elif selection == 3:
                que()
                break
            else:
                print('Resposta inválida. Escolha 1-3')
        except ValueError:
            print('Resposta inválida. Escolha 1-3')

def credits():
    print('Essa conversação foi feita por Adrian C. Borges, com o objetivo de divertir e entreter seu amigo, Noah.')
    anykey = input('Envie qualquer coisa para retornar ao menu: ')
    mainMenu()

def conversadores():
    print('Mia: Ah, talkins ou conversadores são como psicólogos, mais não são profissionais. Meio que servem para as pessoas conversarem, ou até para colocar num jogo. Bemmm, eu acho que os outros talkins estão nos esperando! vamos!')

def cabelos():
    print('Mia: Ah.. Muito obrigado! Você também é uma pessoa muito bonita. Queria que o meu cabelo fosse que nem o seu..... os Outros talkins devem estar nos esperando! vamos!')

def que():
    print('...')
    print('Mia: Okay, os outros talkings devem estar esperando, vamos!')

def mainMenu():
    print('Bem vindo à Conversention!')
    print('1.Começe')
    print('2.Creditos')
    print('3.Sair')
    while True:
        try:
            selection = int(input('Coloque a resposta: '))
            if selection == 1:
                start()
                break
            elif selection == 2:
                credits()
                break
            elif selection == 3:
                break
            else:
                print('Resposta inválida. Escolha 1-3')
        except ValueError:
            print('Resposta inválida. Escolha 1-3')

mainMenu()