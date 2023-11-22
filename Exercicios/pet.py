class Pet:
    def __init__(self) -> None:
        self._nome = None
        self._idade = None
        self._peso = None

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_peso(self):
        return self._peso

    def set_nome(self, string):
        if string == ' ' or string is not isinstance(string, str):
            print('Verifique o nome digitado e tente novamente')
        else:
            self.set_nome(string)

    def set_idade(self, valor):
        if valor is isinstance(valor, int) and valor >= 0:
            self.set_idade = valor
        else:
            print('Verifique a idade digitada')

    def set_peso(self, valor):
        if valor is isinstance(valor, float) and valor > 0:
            self.set_peso = valor
        else:
            print('Verifique o peso digitado')

    def exibir_info(self) -> str:
        print(f'Nome: {self.get_nome()}')
        print(f'Peso: {self.get_peso()}')
        print(f'Idade: {self.get_idade()}')


# Testes
pet2 = Pet()
pet2.set_nome('Buddy')
pet2.set_idade(5)
pet2.set_peso(9.5)
pet2.exibir_info()
