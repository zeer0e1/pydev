vendas = {
    'Janeiro': 120,
    'Fevereiro': 150,
    'Março': 80,
    'Abril': 190,
    'Maio': 210
}

# 1 iterando sobre os meses

for meses in vendas.keys():
    print(meses)

# 2 iterando sobre os valores
total_vendas = 0

for valor in vendas.values():
    total_vendas += valor

print('Total vendido:', total_vendas)

menor_valor = min(vendas.values())

for mes, valor in vendas.items():
    if valor == menor_valor:
        print(f'Mes com o menor valor: {mes}:{valor}')

    print(f'\nEm {mes} {valor} livros foram vendidos')

# 3
