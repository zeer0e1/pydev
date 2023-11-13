minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# como acessar subconjunto de listas
subconjunto = minha_lista[1:4]
print(subconjunto)


# omissao de indices iniciais ou finais
# se não passarmos o parametro inicial
# python considera iniciar do começo da lista
# ou seja, da posição 0
primeiros_elemtos = minha_lista[:2]
print(primeiros_elemtos)

# podemos escolher por qual indice começar
elementos_depois_do_indice_2 = minha_lista[2:]
print(elementos_depois_do_indice_2)

# Slicing com passos
# o terceiro parametro é usa para dizer quantos passos ele
# vai para o proximo elemento
# nesse caso colocamos o numero dois
# então o python vai pular de 2 em 2
elementos_alternados = minha_lista[::2]
print(elementos_alternados)

# subconjunto alternado
subconjunto_alternado = minha_lista[2:8:2]
print(subconjunto_alternado)
