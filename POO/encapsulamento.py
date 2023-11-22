class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self._idade = idade
        self.__saldo = 0

        def mostrar_nome(self):
            return self.nome

        def mostrar_idade(self):
            return self._idade

        def _aumentar_idade(self):
            self._idade += 1

        def __aumentar_saldo(self, quantidade):
            self.__saldo += quantidade

        def depositiar(self, quaantidadde):
            self.__aumentar_saldo(quaantidadde)

            return self.__saldo


p = Pessoa('alice', 30)

print(p.nome)
print(p._idade)
