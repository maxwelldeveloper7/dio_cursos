class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1

    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada')

    def correr(self):
        print('Vrummmmm...')
    
    # def __str__(self) -> str:
    #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('vermeleha', 'caloi', '2022', 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde', 'monark', 2000, 189)
print(b2)