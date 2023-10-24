animais = []

animais.append('gato')
animais.append('cachorro')
animais.append('passáro')

animais.insert(2, 'peixe')

animais.remove('gato')

animal_removido = animais.pop()

novos_animais = ['tartaruga', 'hamster']

todos_animais = animais + novos_animais

print('Existe um cachorro na lista?:', 'cachorro' in todos_animais)

animais_duplicados = todos_animais * 2
print(animais_duplicados)
