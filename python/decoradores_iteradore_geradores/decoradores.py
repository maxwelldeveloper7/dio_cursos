def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos!"

def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")


def pai():
    print("Escrevendo da pai() função")
    
    def filho1():
        print("Escrevendo da filho1() função")

    def filho2():
        print("Escrevendo da filho2() função")

    filho2()
    filho1()


def calcular(operacao):
    def somar(x, y):
        return x + y

    def subtrair(x, y):
        return x - y

    if operacao == "+":
        return somar
    else:
        return subtrair

resultado = calcular("+")(10, 5)
print(resultado)
