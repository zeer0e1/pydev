# Posicao letra

posicao_letra = 'Python'
print(posicao_letra[0])
print(posicao_letra[1])
print(posicao_letra[2])
print(posicao_letra[3])
print(posicao_letra[4])

frase = 'Olá mundo!'

# Obtendo uma parte da string usando slice
parte = frase[4:8]  # Saida: mund
print(parte)

#  Obtendo os primeiros 5 caractres da string
primeiros = frase[:5]
print(primeiros)  # Olá ,

# Obtendo os útlimos 6 carctres da string
ultimos = frase[-6:]
print(ultimos)


# O operador in é  usado em python para verificar a presença de um item em uma tupla ou lista
frase2 = 'O módulo de python é muito legal'
print('python' in frase2)

# Veriricando se a frase python existe na frase
if "python" in frase2:
    print('Sim a palavra python está a frase')

frase3 = "         O módulo python é muito legal"

# Strip - usamos para remover os caractres no inicio ou o final da frase
print(frase3.strip())

# Split divide a frase em varias partes

frase4 = 'Olá como vai vc'
palavras = frase4.split()
print(palavras)


# o método join() junta os elementos de uma lista em uma íunica string utilizando  o separador especificado entre cada elemento
frase_completa = '-'.join(palavras)
print(frase_completa)
