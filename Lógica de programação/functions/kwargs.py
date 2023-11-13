def exibir_informacoes(**kwargs):
    """
    Funcao que xibe informacoes pessoais
    """

    for chave, valor in kwargs.items():
        print(chave + ": " + str(valor))


exibir_informacoes(nome='Lucas', idade=27, cidade="Sorocaba")

contator = 0


def incrementar_contador():
    global contator

    contator += 1
    print(contator)


incrementar_contador()
incrementar_contador()

incrementar_contador()

incrementar_contador()


# variavel nolocal
def funcao_exter():
    variavel_externa = "Eu sou externa"

    print(variavel_externa)

    def funcao_interna():
        nonlocal variavel_externa

        variavel_externa = "E fui modificiada pela função interna"

        print(variavel_externa)

    funcao_interna()

    print(variavel_externa)


funcao_exter()
