class Jogador:
    def __init__(self, nome, posicao, numero_camisa, gols=0) -> None:
        self.nome = nome,
        self.posicao = posicao,
        self.numero_camisa = numero_camisa,
        self.gols = gols


# Instanciando jogadores
Jogador1 = Jogador("Roberto", "Atacante", 9)
Jogador2 = Jogador('Carlos', 'Goleiro', 1)

# Acessando atributos
print(f"{Jogador1.nome} é um {Jogador1.posicao} e usa a camisa número {Jogador1.numero_camisa}")
print(f'{Jogador2.nome} é um {Jogador2.posicao} e usa a camisa número {Jogador2.numero_camisa}')
