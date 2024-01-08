from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Transacao(ABC):
    @property
    @abstractclassmethod
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass


class Cliente():
    def __init__(self, endereco:str):
        self.endereco = endereco
        self.contas = []    
   
    def realizar_transacao(self, conta, transacao:Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco)

    def __str__(self) -> str:
        contas = ""
        for conta in self.contas:
            contas += f"{conta}\n"
        return f"CPF: {self.cpf}\nNome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nEndereço: {self.endereco}\nContas: {contas}"


class Historico():
    def __init__(self) -> None:
        self._transacoes:list = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%y %H:%M:%S"),
            }
        )

    def exibir_historico(self):
        for transacao in self._transacoes:
            print(f"Tipo: {transacao['tipo']}", end="\t\t")
            print(f"Valor: R${transacao['valor']:10.2f}", end="\t")
            print(f"Data: {transacao['data']}", end="\n")
             

class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int):
        return cls(cliente, numero)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor:float) -> bool:        
        excedeu_saldo = valor > self._saldo
        
        if excedeu_saldo:
            print("\nOperação cancelada! Você não tem saldo suficiente. :(")
        elif valor > 0:
            self._saldo -= valor
            print("\nOperação realizada com sucesso! :)")
            return True
        else:
            print("\nOperação cancelada! Valor informado é inválido. :(")
        return False
    
    def depositar(self, valor:float) -> bool:
        if valor > 0:
            self._saldo += valor
            print("\nOperação realizada com sucesso! :)")
            return True
        else:
            print("\nOperação cancelada! Valor informado é inválido. :(")
            return False   
        

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        # Método sobreescrito
        numero_saques = 0
        for transacao in self._historico.transacoes:
            if transacao["tipo"] == Saque.__name__:
                numero_saques += 1
        
        # numero_saques = len(
        #     [transacao for transacao in self._historico.transacoes if transacao["tipo"] == Saque.__name__]
        # )
        
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques
        
        if excedeu_limite:
            print("\nOperação cancelada! Valor do saque excede o limite. :(")
        elif excedeu_saques:
            print("\nOperação cancelada! Excedeu ao número diário de saques permitido :(")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"Agência: {self._agencia} \nC/C: {self._numero} \nTitular: {self._cliente.nome}"


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# cliente = PessoaFisica("12345678912","Maxwell","25-05-1979","Rua Rio Grande do Norte, 635")
# conta1 = ContaCorrente(1,cliente)
# cliente.adicionar_conta(conta1)
# conta2 = ContaCorrente(2,cliente)
# cliente.adicionar_conta(conta2)
# transacao = Deposito(500)
# cliente.realizar_transacao(conta1,transacao)
# transacao = Saque(100)
# cliente.realizar_transacao(conta1,transacao)
# conta1.historico.exibir_historico()
# print(conta1.saldo)

def menu():
    menu = """\n
    ================= MENU - SISTEMA BANCÁRIO ==================
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


def depositar(valor, conta, cliente):
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)


def sacar(valor, conta, cliente):
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(conta):
    print('Extrato'.center(70,'-'))
    print('Não foram realizadas movimentações.' if conta == None else conta.historico.exibir_historico())
    print(''.center(70,'-'))


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente número):')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\nJá existe um usuário com este CPF!')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascomento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    usuarios.append(cliente)
    print('Usuário criando com sucesso!')


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return True, usuario
    return False


def criar_conta(numero_conta, usuarios):
    cpf = input('Informe o CPF (somente número):')
    usuario_encontrado, cliente = filtrar_usuario(cpf, usuarios)
    
    if usuario_encontrado:
        conta = ContaCorrente(numero_conta, cliente)
        
        print('\nConta criada com sucesso!')
        return conta

    print('\nUsuário não encontrado, processo de abertura de conta encerrado!')


def listar_contas(contas):
    for conta in contas:
        print(conta)


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
        cpf = input("Informe o CPF: ")
        usuario_existente, cliente = filtrar_usuario(cpf, usuarios)
        if usuario_existente:
            valor = float(input('Informe o valor do depósito: '))
            listar_contas(contas)
            nr_conta = input("Informe o Número da Conta:")
            for conta in contas:
                if int(nr_conta) == conta.numero:
                    depositar(valor, conta, cliente)                
            
        else:
            print('Não existe usuário cadastrado com este CPF!')
    elif opcao == '2':
        cpf = input("Informe o CPF: ")
        usuario_existente, cliente = filtrar_usuario(cpf, usuarios)
        if usuario_existente:
            valor = float(input('Informe o valor do saque: '))
            listar_contas(contas)
            nr_conta = input("Informe o Número da Conta:")
            for conta in contas:
                if int(nr_conta) == conta.numero:
                    sacar(valor, conta, cliente)                
            
        else:
            print('Não existe usuário cadastrado com este CPF!')

    elif opcao == '3':
        cpf = input("Informe o CPF: ")
        usuario_existente, cliente = filtrar_usuario(cpf, usuarios)
        if usuario_existente:
            listar_contas(contas)
            nr_conta = input("Informe o Número da Conta:")
            for conta in contas:
                if int(nr_conta) == conta.numero:
                    exibir_extrato(conta)
    elif opcao == '4':
        numero_conta = len(contas) + 1
        conta = criar_conta(numero_conta, usuarios)
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