def meu_decorator(funcao):
    def envelope():
        print("Faz algo antes da execução da função")
        funcao()
        print("Faz algo depois da execução da função")

    return envelope

# def ola_mundo():
#     print("Olá mundo!")

# ola_mundo = meu_decorator(ola_mundo)
# ola_mundo()

@meu_decorator
def ola_mundo():
    print("Olá mundo!")

ola_mundo()