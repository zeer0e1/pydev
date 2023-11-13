# criando um conjunto inicial

s = {1, 2, 3, 4}
print(s)

# 2 usando o add()
s.add(5)
print(s)

# 3 usando o rmeove()

s.remove(5)
print(s)

try:
    s.remove(5)
except KeyError as e:
    print(f'Error:{e}')

# usando do dicsard()
s.discard(4)
print(s)

# pop() remove aleatoriamente
elemento_removido = s.pop()
print(elemento_removido)

# cleat() remove todos os elemtnso do conjuntop
s.clear()
