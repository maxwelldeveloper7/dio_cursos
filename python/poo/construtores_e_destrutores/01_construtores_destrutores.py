class Cachorro:
    def __init__(self, nome, cor, acordado=True) -> None:
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordaddo = acordado

    def __del__(self):
        print('Removendo a instância da classe.')

    def falar(self):
        print('auau')

def criar_cachorro():
    c = Cachorro('Zeus', 'branco e preto', False)
    print(c.nome)

c = Cachorro('Chappie', 'amarelo')
c.falar()

print('ola mundo')
del c
print('ola mundo')
print('ola mundo')
print('ola mundo')

criar_cachorro()