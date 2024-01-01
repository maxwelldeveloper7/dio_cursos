class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

    def __str__(self):
        return 'Mamifero'

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

    def __str__(self):
        return 'Ave'

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__)
        print(Ornitorrinco.mro())
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

    def __str__(self):
        return 'Ornitorrinco'

gato = Gato(nro_patas = 4, cor_pelo='Preto')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo='vermelho', cor_bico='laranja')
print(ornitorrinco)