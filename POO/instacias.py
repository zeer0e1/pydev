class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f'Velocidade autal: {self.velocidade} km/h')

    def freiar(self):

        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0

        print(f'Velocidade autal: {self.velocidade} km/h')

    def exibir_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}')


lista_carros = []

while True:
    print('\n--- Menu ---')
    print('1. Adcionar novo carro')
    print('2. Exibir informações do carro')
    print('3. Acelerar um carro')
    print('4. Frear um carro')
    print('5.Sair')

    escolha = input('Escolha uma opcao: ')

    if escolha == "1":
        marca = input('Digite a marca do carro: ')
        modelo = input('Digite o modelo do carro: ')
        cor = input('Digite a cor do carro: ')

        novo_carro = Carro(marca, modelo, cor)
        lista_carros.append(novo_carro)

    elif escolha == "2":
        if lista_carros:
            for carro in lista_carros:
                Carro.exibir_info()
        else:
            print('Nenhum carro adicionado ainda')

    elif escolha == '3':
        modelo = input('Digite o modelo do carro: ')
        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.acelerar()
                break
            else:
                print('Modelo não encontrado')

    elif escolha == "5":
        print('Saindo do programa')
        break
