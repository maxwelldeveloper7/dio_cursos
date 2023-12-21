menu = """
========== MENU OPERAÇÕES BANCÁRIAS ===========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        print('Depósito')
    elif opcao == 's':
        print('Saque')
    elif opcao == 'e':
        print('Extrato')
    elif opcao == 'q':
        print('Fim do programa')
        break
    else:
        print('Oção inválida, por favor selecione novamente a operação desejada.')