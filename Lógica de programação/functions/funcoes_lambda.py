# Funcao regular
def dobrar(n):
    return n * 2

# funcao lambda
dobrar_lambda = lambda n: n * 2

print(dobrar_lambda(2))
print(dobrar(5))

# Exemplo 2

def classificar_numero(n):
    if n < 0:
        return 'Negativo'
    elif n == 0:
        return 'Zero'
    else:
        return 'Positivo'


# Exemplo de uma lambda
classificar_numero_Labda = lambda n: 'Negativo' if n < 0 else ('zero' if n == 0 else 'positivo')


print(classificar_numero_Labda(0))

"""
Exemplo de uma função lambda 
suponha que vc tenha uma lista de tulpas representando pessoas
e suas idades e vc queira classificadas pela idade

"""

pessoas = [('Lucas', 35), ('Maria', 29), ('Pedro', 60)]

pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)
