
def menu():
    menu = """\n
    ================= MENU ==================
    [1]\tDepositoar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar Contas
    [6]\tNovo usuário
    [0]\tSair
    =>
    """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print('\n Falha na operação! O valor informado é inválido.')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques == LIMITE_SAQUES:
        print('Você já efetuou 3 saques diários permitidos! Tente novamente amanhã!')
        return

    if limite == 0:
        print('Você alcançou o limite de saque diários de R$ 500,00! Tente novamente amanhã!')
        return

    
    if valor <= 0:
        print('Valores menores iguais a zero não são permitidos, tente novamente!')
    elif limite - valor < 0:
        print('Limite de saques diários excedido! Tente novamente amanhã!')
        print(f'Limite de saque atual: R$ {limite:.2f}')
    elif valor > saldo:
        print('Saldo indisponível')
        print(f'Saldo atual: R$ {saldo:.2f}')
    else:
        saldo -= valor
        extrato += f'Saque realizado:    R$ {valor:5.2f}\n'
        print('Saque realizado com sucesso!')
        print(f'Valor: R$ {valor:.2f}')
        limite -= valor
        numero_saques += 1     
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('Extrato'.center(48,'-'))
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo atual:    R$ {saldo:5.2f}')
    print(''.center(48,'-'))


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente número):')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\nJá existe um usuário com este CPF!')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascomento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    usuarios.append({'nome':nome, 'data_nascimento': data_nascimento, 'cpf':cpf, 'endereco': endereco})
    print('Usuário criando com sucesso!')


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF (somente número):')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\nConta criada com sucesso!')
        return {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario
        }

    print('\nUsuário não encontrado, processo de abertura de conta encerrado!')


def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print(linha)



LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:
    opcao = menu()

    if opcao == '1':
        valor = float(input('Informe o valor do depósito: '))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == '3':
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == '4':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    elif opcao == '5':
        listar_contas(contas)
    elif opcao == '6':
        criar_usuario(usuarios)
    elif opcao == '0':
        break
    else:
        print('Operação inválida, tente novamente!')            
