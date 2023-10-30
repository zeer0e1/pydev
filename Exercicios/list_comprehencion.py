numeros = [x ** 3 for x in range(10)]
print(numeros)

numeros_divisiveis_3 = [x for x in range(1, 21) if x % 3 == 0]
print(numeros_divisiveis_3)

frutas = ['Maça', 'Banana', 'Manga', 'Uva', 'abacaxi', 'Laranja']
frutas_5_letras = [fruta for fruta in frutas if len(fruta) > 5]
print(frutas_5_letras)

notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]

notas_maiores_75 = [nota for nota in notas if nota > 75]
print(notas_maiores_75)
