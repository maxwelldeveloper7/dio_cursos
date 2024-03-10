"""
    Este aplicativo é uma implementação de um desafio dos cursos formação 
    python.
    
    Integrando Python com SQLite e MongoDB    
"""
import pprint
import pymongo

client = pymongo.MongoClient("mongodb+srv://pymongo:pymongo@cluster0.lwevttd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.db

collection = db.bank
print(db.bank)

cliente = {"id": 1,
        "nome": "Maxwell",
        "cpf": "12345678912",
        "endereco": "Rua dos vencedores, 777",
        "agencia": "001",
        "conta": "001",
        "tipo": "Conta Corrente",
        "saldo": 100.00
    }

bank = db.bank
post_id = bank.insert_one(cliente).inserted_id
print(post_id)

pprint.pprint(db.bank.find_one())

novos_clientes = [
        {
            "id": 1,
            "nome": "Isabella",
            "cpf": "12345678912",
            "endereco": "Avenida das Conquistas, 123",
            "agencia": "001",
            "conta": "002",
            "tipo": "Conta Salário",
            "saldo": 1000.00
        },
        {
            "id": 1,
            "nome": "Lucas",
            "cpf": "12345678912",
            "endereco": "Travessa dos Triunfos, 456",
            "agencia": "001",
            "conta": "003",
            "tipo": "Conta Poupança",
            "saldo": 100.00
        }]

result = bank.insert_many(novos_clientes)
print(result.inserted_ids)
print('\nRecuperando dados')
result = db.bank.find({"nome":"Maxwell"})

for cliente in result:
    pprint.pprint(cliente)
