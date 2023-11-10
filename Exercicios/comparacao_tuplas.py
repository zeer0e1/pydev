t1 = (3, 5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)

# Qual é maior t1 ou t2?
print('t1' if t1 < t2 else 't2')  # Por causa do comprimento

# t3 é maior que t1 ?
print(t3 < t1)  # ignora os elemetos iguais e commpara os diferntes

# t4 e t1 qual é maior ?

print('t4' if t4 < t1 else 't1')  # Compara todos os elementos

# t1 e t5 são iguais ?
print(t1 == t5)  # possui os memso elementos
