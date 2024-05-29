def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Antes da função")
        funcao(*args, **kwargs)
        print("Depois da função")
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")

ola_mundo("Maria")
