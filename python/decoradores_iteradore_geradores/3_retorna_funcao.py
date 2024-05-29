def calculadora(operacao):
    def soma(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    match operacao:
        case '+':
            return soma
        case '-':
            return sub
        case '*':
            return mul
        case '/':
            return div


print(calculadora('+')(10, 20))
print(calculadora('-')(10, 20))
print(calculadora('*')(10, 20))
print(calculadora('/')(10, 20))

op = calculadora('+')
print(op(10, 20))
op = calculadora('-')
print(op(10, 20))
op = calculadora('*')
print(op(10, 20))
op = calculadora('/')
print(op(10, 20))
