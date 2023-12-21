
LIMITE_DE_SAQUES = 3
VALOR_MAXIMO_DIARIO_SAQUE = 500.00
saldo = 0.0
extrato = ""

while True:
    print("""
    ========== MENU OPERAÇÕES BANCÁRIAS ===========
    [1] para depósito
    [2] para saque
    [3] para extrato
    [0] para sair
    """)
    opcao = input('Escola uma oção: ')
    
    if opcao == '1':
        print('Depósito')
    elif opcao == '2':
        print('Saque')
    elif opcao == '3':
        print('Extrato')
    elif opcao == '0':
        print('Fim do programa')
        break
    else:
        print('Oção inválida')