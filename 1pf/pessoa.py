class Pessoa():
    coração = 1
    cerebro = 1

    def __init__(self, nome, idade, raça):
        self.nome = nome
        self.idade = idade
        self.raça = raça

    def respirar(self):
        print("Ar")
    def meio_de_falar(self):
        print("sinais", "boca")

pessoa1 = Pessoa("Messi", "32 anos", "branca")
pessoa2 = Pessoa("Balotelli", "29 anos", "negra")

pessoa1.respirar()
pessoa2.meio_de_falar()
print(pessoa1.nome)
print(pessoa2.nome)