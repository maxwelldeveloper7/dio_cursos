
lista = [1, 10]

try:    
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('erro desconhecida. Erro: {}'.format(ex))
else:
    print("Executa quanto não ocorre exceção")
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()
