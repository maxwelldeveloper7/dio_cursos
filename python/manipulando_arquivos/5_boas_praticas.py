from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "lorem.txt", 'r', encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")


try:
    with open(ROOT_PATH / "arquivo-utf-e.txt", 'w', encoding="utf-8") as arquivo:
        print(arquivo.write("Aprendendo a manipular arquivos utilizando Python."))
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")