# Tuplas

livro = ('A arte da guerra', 'Sun tzu', '978-857835080')

# Acessar informacoes

titulo = livro[0]
autor = livro[1]
isbn = livro[2]
print(titulo)
print(autor)
print(isbn)


# Criando uma tupla
destino1 = ('Paris', 'França', 5)

# Criando uma tupla com unico elemento

destino_indefinindo = ('Kyoto',)

# Tupla sem parenteses
destino2 = "Roma", 'Italia', 4

# Uso da funcao tuple

lista_destinos_EUA = ['Nova York', "EUA", 7]
destino3 = tuple(lista_destinos_EUA)
print(destino3)
