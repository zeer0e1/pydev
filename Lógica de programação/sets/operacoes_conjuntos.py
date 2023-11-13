s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# uniao

uniao = s1 | s2
print(uniao)

# uniao method
uniao_method = s1.union(s2)
print(uniao_method)

# interseção

intersecao = s1 & s2

print(intersecao)  # tbm poder ser usado s1.intersction(s2)

# diferenca
dife = s1 - s2  # tbm pode ser usado com o method
print(dife)

# diferenca simetrica
diferenca_simetrica = s1 ^ s2
print(diferenca_simetrica)

# subset
s3 = {1, 2}
is_subset = s3.issubset(s1)
print(is_subset)

# superset

is_superset = s1.issuperset(s2)
