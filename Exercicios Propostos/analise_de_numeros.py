import math
nunber = int(input('Write nunber: '))


if nunber % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')

if nunber > 0:
    print('É positivo')
    square = math.sqrt(nunber)
    print(f'A raiz quadrada de {nunber} is {square}')
elif nunber == 0:
    print('É zero')
else:
    print('É negativo')
