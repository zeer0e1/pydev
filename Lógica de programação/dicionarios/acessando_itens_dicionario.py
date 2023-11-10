smartphone = {
    'marca': 'Apple',
    'modelo': 'iphone 14',
    'cor': 'azul',
    'capacidade': '128GB',
    'sistema': 'iOS'
}

print('Método direto')

print('Marca:', smartphone['marca'])

print('Metodo get')

print('\nUsando o metodo get:')
print('Modelo:', smartphone.get('modelo', 'N existe essa opçao'))

print('Verificando a existencia')
if 'sistema' in smartphone:

    print('O smarthphine roda no sistema:', smartphone['sistema'])
else:
    print('Sitema operacional nao especificado')
