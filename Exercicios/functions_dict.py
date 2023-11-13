# 1 registro de livro
def registrar_livro(titulo, autor, ano):
    return {
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    }


def exibir_livro(livro: dict):
    for chave, valor in livro.items():
        print(f'\n{str(chave).capitalize()}: {valor}')


livro = registrar_livro('1984', 'Geroge Orwell', 1949)
exibir_livro(livro)
