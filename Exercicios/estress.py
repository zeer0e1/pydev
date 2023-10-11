import random

tenativas = 0
senha_padrao = 2
numeros_gerados = []


while True:
    numero_secreto = random.randrange(1,300)
    
    if numero_secreto in numeros_gerados:
        continue
    
    numeros_gerados.append(numero_secreto)


    if numero_secreto == senha_padrao:
        break

    tenativas += 1
  

print(f'numero tentivas {tenativas} numeros gerados {numeros_gerados}')
        
