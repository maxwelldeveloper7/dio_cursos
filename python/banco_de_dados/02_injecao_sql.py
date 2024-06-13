import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory =  sqlite3.Row

id_cliente = input("Digite o ID do cliente: ") # informe: 1 or 1=1; | exibirá todos os registros
cursor.execute(f"SELECT * FROM clientes WHERE id = {id_cliente}")
clientes = cursor.fetchall()
for cliente in clientes:
    print(dict(cliente))