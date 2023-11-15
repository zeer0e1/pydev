class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


meu_livro = Livro('1984', 'George Owerll', 1984)

# atributos
print(meu_livro.titulo)
print(meu_livro.autor)
print(meu_livro.ano)


class Livro:
    def __init__(self, titulo, ano, autor) -> None:
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

    def descricao(self):
        return f'{self.titulo} por {self.autor} no ano {self.ano}'


meu_livro = Livro('1984', 'George Owerll', 1984)

print(meu_livro.descricao())
