from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / 'novo-diretorio' / 'novo.txt', 'r')
except FileNotFoundError as exc:
    print(f'Arquivo não encontrado: {exc}')
except IsADirectoryError as exc:
    print(f'Não foi possível abri o arquivo: {exc}')
except IOError as exc:
    print(f'Erro ao abrir o arquivo: {exc}')
except Exception as exc:
    print(f'Algum problema ocorreu ao tentar abrir o arquivo: {exc}')