print('Digite os números para ser ordenado, digi "ok" quando terminar: ')
list_numbers = []
while True:
    number = input()
    if number == 'ok':
        break
    else:
        list_numbers.append((int(number)))
        continue
list_numbers.sort()
print(f'Números ordenados: {list_numbers}')
