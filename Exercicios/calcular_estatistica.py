list_numbers = list(map(float, input('Digite numeros ').split(' ')))


def estatisticas(*args):
    return sum(args) / len(args), max(args), min(args)


estatisticas(list_numbers)
