menu = """
--------- MENU OPERAÇÕES BANCÁRIAS -----------
| [1] Depositar                              |
| [2] Sacar                                  |
| [3] Extrato                                |
| [0] Sair                                   |
----------------------------------------------
--> """

saldo = 0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == '1':
        print('\nDepósito selecionado\n')        
        valor = float(input('Informe o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito realizado: R$ {valor:5.2f}\n'
            extrato += f'Saldo atual:        R$ {saldo:5.2f}\n'
            print('Depósito realizado com sucesso!')
            print(f'Valor: R$ {valor:.2f}')
        else:
            print('Valores menores que zero não são permitidos, tente novamente!')

    elif opcao == '2':
        print('\nSaque selecionado\n')
        if numero_saques == LIMITE_SAQUES:
            print('Você já efetuou 3 saques diários permitidos! Tente novamente amanhã!')
            continue
        
        if limite == 0:
            print('Você alcançou o limite de saque diários de R$ 500,00! Tente novamente amanhã!')
            continue
        
        valor = float(input('Informe o valor a ser sacado: '))
        
        if valor <= 0:
            print('Valores menores que zero não são permitidos, tente novamente!')
        elif limite - valor < 0:
            print('Limite de saques diários excedido! Tente novamente amanhã!')
            print(f'Limite de saque atual: R$ {limite:.2f}')
        elif valor > saldo:
            print('Saldo indisponível')
            print(f'Saldo atual: R$ {saldo:.2f}')
        else:
            saldo -= valor
            extrato += f'Saque realizado:    R$ {valor:5.2f}\n'
            extrato += f'Saldo atual:        R$ {saldo:5.2f}\n'
            print('Saque realizado com sucesso!')
            print(f'Valor: R$ {valor:.2f}')
            limite -= valor
            numero_saques += 1        
        
    elif opcao == '3':
        print('Extrato'.center(48,'-'))
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        if saldo == 0:
            print(f'Saldo atual:        R$ {saldo:5.2f}')
        print(''.center(48,'-'))
        print(f'Limite disponível para saques diários: R$ {limite:5.2f}')
        print('Limite de saques diários: 3')
        print(f'Saques realizados: {numero_saques}')
    elif opcao == '0':
        print('Fim do programa')
        break
    else:
        print('Opção inválida, por favor selecione novamente a operação desejada.')