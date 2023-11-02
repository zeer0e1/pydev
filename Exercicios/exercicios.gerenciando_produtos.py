produto = ('Smartphone', 1000.00, [2, 3, 4])


"""
produto[1] = 1100.00

Se tentarmos aletar o valor da dupla iremos receber o 
erro de typeErro pois não é possivel alterar o valor de uma tupla

"""
produto[2].append(5)

print('Valor de celulares vendido por dias:', produto[2])
