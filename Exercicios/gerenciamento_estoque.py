def resumo_vendas(vendas_smartphones, vend_smartwatches):
    produto_mais_vendido = "SmartPhone" if vendas_smartphones > \
        vend_smartwatches else "Smartwatches"
    return produto_mais_vendido
