import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

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

excluir_registro(conexao, cursor, 1)