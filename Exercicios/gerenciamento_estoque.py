def resumo_vendas(vendas_smartphones, vend_smartwatches):
    produto_mais_vendido = "SmartPhone" if vendas_smartphones > \
        vend_smartwatches else "Smartwatches"
    return produto_mais_vendido


print(f'O produto mais vendido foi:{resumo_vendas(80,70)}')


# uso de tuplas em loops for
vendas_semana = [(70, 65), (80, 82), (90, 88)]

i = 1

for ven_phones, ven_watches in vendas_semana:
    print('')
    print(f'Vendas na semana : {i} ')
    print(f'Total de vendas de celulares: {ven_phones}')
    print(f'Total de vendas relógios: {ven_watches}')
    i += 1

# trocando valores
vendas_segunda = (65, 80)

ven_phones, ven_watches = vendas_segunda

ven_phones, ven_watches = ven_watches, ven_phones
print(f'Venda de telefones na segunda feira {ven_phones}')
