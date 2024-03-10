"""
    Este aplicativo é uma implementação de um desafio dos cursos formação 
    python.
    
    Integrando Python com SQLite e MongoDB    
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select

Base = declarative_base()

class Cliente(Base):
    """
        Esta Classe reprensenta  a tabela de cliente dentro do SQLite
    """
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String)
    endereco = Column(String)

    conta = relationship("Conta", back_populates="cliente")

    def __repr__(self):
        """
            Retorna uma representação dos campos do da tabela de cliente com a
            classe Cliente.
        """
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(Base):
    """
        Esta Classe reprensenta  a tabela de cliente dentro do SQLite
    """
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    saldo = Column(DECIMAL)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        """
            Retorna uma representação dos campos do da tabela de conta com a
            classe Conta.
        """
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, saldo={self.saldo}, id_cliente={self.cliente.id})"

print("verificando nome das tabelas: ",
      Cliente.__tablename__,
      ", ",
      Conta.__tablename__,
      "\n")

#  Conexão com o banco de dados
engine = create_engine("sqlite://")

#  Criando as classes como tabelas do banco de dados
Base.metadata.create_all(engine)

#  Investiga o esquema de banco de dados
print("Inspecionando esquema do banco de dados...")
inspetor_engine = inspect(engine)
print("Há uma tabela cliente? ",inspetor_engine.has_table("cliente"))
print("Há uma tabela conta? ",inspetor_engine.has_table("conta"))
print("Listando tabelas existentes: ",inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)
print("Inspeção concluída. Tudo Ok!\n")

print("Abrindo sessão para popular tabelas com dados de contas e clientes")

with Session(engine) as session:
    cliente1 = Cliente(
        nome='Maxwell',
        cpf='12345679812',
        endereco='Rua dos vencedores, 777'
    )
    conta1 = Conta(
        tipo='Conta Corrente',
        agencia='001',
        saldo=0.00,
        cliente=cliente1
    )

    cliente2 = Cliente(
        nome='Isabella',
        cpf='98765432101',
        endereco='Avenida das Conquistas, 123'
    )

    conta2 = Conta(
        tipo='Conta Poupança',
        agencia='001',
        saldo=1000.00,
        cliente=cliente2
    )

    cliente3 = Cliente(
        nome='Lucas',
        cpf='45678901234',
        endereco='Travessa dos Triunfos, 456'
    )

    conta3 = Conta(
        tipo='Conta Corrente',
        agencia='001',
        saldo=500.00,
        cliente=cliente3
    )

    #  Enviando para o DB
    session.add_all([conta1, conta2, conta3])
    session.commit()


stmt = select(Cliente)
print('\nRecuperando clientes')
for cliente in session.scalars(stmt):
    print(cliente)

stmt_cliente = select(Cliente).where(Cliente.nome.in_(['Maxwell']))
print('\nRecuperando cliente com nome Maxwell')
for cliente in session.scalars(stmt_cliente):
    print(cliente)

stmt_conta = select(Conta)
print('\nRecuperando contas')
for conta in session.scalars(stmt_conta):
    print(conta)

stmt_join = select(Conta, Cliente.nome).join_from(Cliente, Conta)
print('\nRecuperando join de tabelas')
for result in session.scalars(stmt_join):
    print(result)


connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print('\nExecutando statement a partir da connection')
for result in results:
    print(result)

session.close()
