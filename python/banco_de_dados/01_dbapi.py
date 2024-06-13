import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory =  sqlite3.Row

def criar_tabela(conn, cur):
    """Cria a tabela clientes"""
    cur.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))'
    )
    conn.commit()


def inserir_registro(conn, cur, nome, email):
    """Insere um registro na tabela clientes"""
    data = (nome, email)
    cur.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', data)
    conn.commit()

def atualizar_registro(conn, cur, nome, email, id):
    """Atualiza um registro na tabela clientes"""
    data = (nome, email, id)
    cur.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?;', data)
    conn.commit()

def excluir_registro(conn, cur, id):
    """Exclui um registro na tabela clientes"""
    data = (id,)
    cur.execute('DELETE FROM clientes WHERE id = ?;', data)
    conn.commit()

def inserir_muitos(conn, cur, dados):
    cur.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?);', dados)
    conn.commit()

# def recuperar_cliente(cur, id):
#     cur.execute('SELECT * FROM clientes WHERE id = ?;', (id,))
#     return cur.fetchone()

def recuperar_cliente(cur, id):
    cur.execute('SELECT * FROM clientes WHERE id = ?;', (id,))
    return cur.fetchone()

def listar_clientes(cur):
    cur.execute('SELECT * FROM clientes ORDER BY nome;')
    return cur.fetchall()

cliente = recuperar_cliente(cursor, 10)
print(dict(cliente))

clientes = listar_clientes(cursor)
print(clientes)

for cliente in clientes:
    print(dict(cliente))
# dados = [
#     ("Ana Silva", "ana.silva@example.com"),
#     ("Carlos Pereira", "carlos.pereira@example.com"),
#     ("Maria Oliveira", "maria.oliveira@example.com"),
#     ("João Souza", "joao.souza@example.com"),
#     ("Luiza Fernandes", "luiza.fernandes@example.com"),
#     ("Pedro Lima", "pedro.lima@example.com"),
#     ("Carla Dias", "carla.dias@example.com"),
#     ("Lucas Mendes", "lucas.mendes@example.com"),
#     ("Juliana Costa", "juliana.costa@example.com"),
#     ("Marcos Alves", "marcos.alves@example.com"),
#     ("Fernanda Rocha", "fernanda.rocha@example.com"),
#     ("Roberto Gonçalves", "roberto.goncalves@example.com"),
#     ("Sofia Martins", "sofia.martins@example.com"),
#     ("Rafael Silva", "rafael.silva@example.com"),
#     ("Bianca Souza", "bianca.souza@example.com"),
#     ("Renato Alves", "renato.alves@example.com"),
#     ("Patrícia Ferreira", "patricia.ferreira@example.com"),
#     ("Ricardo Costa", "ricardo.costa@example.com"),
#     ("Larissa Oliveira", "larissa.oliveira@example.com"),
#     ("Gabriel Lima", "gabriel.lima@example.com")
# ]

# inserir_muitos(conexao, cursor, dados)


