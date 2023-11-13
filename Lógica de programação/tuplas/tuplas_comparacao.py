# Comparando tuplas
t1 = (1, 2)
t2 = (1, 3)
print(t1 < t2)  # Imprime true por causa que 2 é maior que 3

# Ignorando elementos iguais

t3 = (1, 2, 3)
t4 = (1, 2, 4)
print(t3 < t4)  # imprime true pois 3 é menor que 4

# Comparando tuplas de diferentes tamanhos

t1 = (1, 2)
t2 = (1, 2, 3)
print(t1 < t2)  # imprime True porque t1 é mair curot
# que a t2, mesmmo que seus elementos
# sejam iguais

# Comparacao de elementos de diferentes tipos

t1 = (1, "apple")
t2 = (2, "Banana")
print(t1 < t2)
# Nessa comparação o resultado será true pois ele comapara
# com base na classficação de tipos onde int vem primeiro
# que string ele nmem chega a comparar
