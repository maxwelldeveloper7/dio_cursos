a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('soma: {soma}. \n'
      'Subitração: {sub}.\n'
      'Multiplicação: {mult}.\n'
      'Divisão: {div}.\n'
      'Resto: {r}.'.format(
          soma = soma,
          sub = subtracao,
          mult = multiplicacao,
          div = divisao,
          r = resto))