# listas
# São ideias para casos onde precisamos realizar mudanças na lista
# deixar mais dinamico
livros_mais_empretados = ['O pequeno principe', '1984', 'Dom quixote']
livros_mais_empretados.append('O senhor dos aneis')

# tuplas
# São ideais para garantir uma informação que não muda ou seja lgumas informação fixa no sistema
# imutabilidade
livro_info = ('O pequeno principe',
              'Antoine de saint-exuéry', '978-2-16-14-851')

# Quando utilizar uma ou outra
"""
    Listas:
        - quando so dados são dinamicos e podem mudar durante o tempo
        - quando você precisa de métodos como append() remove()
        - para sequencias de tamanho variavel
    Tuplas:
        - quando os dados não devem ser alterados (imutabilidade)
        - para garantir integridade dos dados
        - para usar como chave em dicionarios (listas nao podem ser usadas)
        - para melhorar eficiencia, pois tuplas saão geralmente 
        mais rapida para iteraçãoe preocessamento


"""
