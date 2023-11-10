# Exec 1
def destinos(deste: list):
    i = 1
    for destino, cidade, cod in deste:
        print('---------')
        print(f'Item: {i}')
        print(f'Cod: {cod}\nDestino: {destino}\nCidade: {cidade}')
        i += 1


def feedback(cod, obs, qtd_estrelas):
    feedebacks_destinos.append([cod, obs, qtd_estrelas])


def info_feedbacks():
    for cod1, obs, stars in feedebacks_destinos:
        for destino, cidade, cod in destinos_turisticos:
            if cod1 == cod:
                print('---------')
                print(
                    f'Destino: {destino}\nAvaliacao:{stars}\
                        \nComentário: {obs}')
                print('---------')


destinos_turisticos = [('Rio de janeiro', 'Brasil', '1423'),
                       ('Recife', 'Brasil', '1324'),
                       ('Disney', 'Estados Unidos', '1512')]

# Exec 2
feedebacks_destinos = []


# destinos(destinos_turisticos)

# Exec 2
feedback('1423', 'Top de mais', 5)
feedback('1324', 'Muit lindooo amei', 5)
feedback('1512', 'Achei muito caro as coisas', 3)
feedback('1423', 'Voltaria novamente', 5)
feedback('1324', 'Amei de mais', 5)

info_feedbacks()
