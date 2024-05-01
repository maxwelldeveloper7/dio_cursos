""" Realiza testes de persistência no banco de dados atividades.db"""
from models import Pessoas, Usuarios

def insere_pessoas():
    """ Insere dados na tabela pessoa. """
    pessoa = Pessoas(nome='Chaves', idade=45)
    print(pessoa)
    pessoa.save()

def consulta():
    """ Consulta dados na tabela pessoa. """
    #pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Maxwell')
    for p in pessoa:
        print(f'Nome: {p.nome}', end=" - ")
        print(f'Idade: {p.idade}')

def altera_pessoa():
    """ Altera dados na tabela pessoa. """
    pessoa = Pessoas.query.filter_by(nome='Maxwell').first()
    pessoa.idade = 44
    pessoa.save()

def exclui_pessoa():
    """ Deleta dados na tabela pessoa. """
    pessoa = Pessoas.query.filter_by(nome='Chaves').first()
    pessoa.delete()

def insere_usuario(login, senha):
    """ Insere um usuário e senha para acesso à API"""
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    # insere_pessoas()
    # exclui_pessoa()
    # consulta()
    insere_usuario('maxwell', '1234')
    insere_usuario('chaves', '4321')
    consulta_todos_usuarios()
