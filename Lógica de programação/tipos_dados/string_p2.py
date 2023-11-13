nome = 'Lucas'
idade = 27
altura = 1.68

mensagem = f'Olá meu nome é  {nome}. Tenho {idade} anos e minha altura é {altura:.2f} metros'
print(mensagem)


texto = 'hello mundo'
texto_upper = texto.upper()
texto_lower = texto.lower()
texto_captalize = texto.capitalize()

# Upper deixa todo o texto em caixa alta
print(texto_upper)

# lower() deixa o texto todo em letra minuscula
print(texto_lower)

# captalize() deixa o texto com a primeira letra em maiscula
print(texto_captalize)


# count() conta quantas vezers o caractrere informado como parametro foi encontrado na frase
print(texto_lower.count('o'))

# replace() substitui todos as ocorrencias encontradas na string
print(texto_lower.replace('o', 'a'))
