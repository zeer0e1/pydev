# retornando +multiplos valores de uma funcao

def analisar_vendas(vendas_A, vendas_B):
    total_vendido = vendas_A + vendas_B
    mais_vendido = "A" if vendas_A > vendas_B else "B"
    return total_vendido, mais_vendido


total, top_produto = analisar_vendas(100, 85)

print(f'Total vendido: {total}')
print(f'Produto mais vendido: {top_produto}')

# uso de tuplas em loops for

vendas = [(100, 90), (100, 115), (105, 100)]


for vendas_A, vendas_B in vendas:
    print(f'Vendas de A: { vendas_A}, vendas de B: {vendas_B}')

# trocando valores entre duas variaveis
vendas_X = 100
vendas_z = 200
vendas_X, vendas_z = vendas_z, vendas_X
