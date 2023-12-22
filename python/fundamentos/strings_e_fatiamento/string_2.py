nome = 'Maxwell'
idade = 44
profissao = 'Programador'
linguagem = 'Python'
saldo = 45.435

dados = {'nome': 'Maxwell', 'idade': 44}

print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {} Idade: {}'.format(idade, nome))
print('Nome: {1} Idade: {1} {1}'.format(idade, nome))
print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade = idade))
print('Nome: {name} Idade: {age}'.format(name=nome, age = idade))
print('Nome: {nome} Idade: {idade}'.format(**dados))
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}')