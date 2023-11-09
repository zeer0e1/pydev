avaliacoes = (5, 4, 4, 3, 5, 2, 4, 3, 5, 5, 1, 5, 3, 5, 2)
qtd_5_estrelas = avaliacoes.count(5)
posicao_1_estrela = avaliacoes.index(1) + 1
print(f'O filme recebeu {qtd_5_estrelas} vezes 5 estrelas')
print(f'O filme foi avaliado com 1 estrela no dia {posicao_1_estrela}')
