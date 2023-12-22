n = int(input())


while n > 0:


    values = input().split()


    aux = ''
    for digit in values[0][::-1]:
        aux += digit
        if aux == values[1][::-1]:
            print('encaixa')
            break
    else:
        print('nao encaixa')


    aux = ''


    n -= 1