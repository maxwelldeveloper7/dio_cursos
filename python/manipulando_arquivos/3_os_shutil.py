import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# print(ROOT_PATH)
# #os.mkdir(ROOT_PATH / "novo-diretorio")

# arquivo = open(ROOT_PATH/"novo-diretorio/novo.txt", "w")
# arquivo.close()

# os.rename(ROOT_PATH/'novo-diretorio/novo.txt', ROOT_PATH/'novo-diretorio/alterado.txt')

# os.remove(ROOT_PATH/'novo-diretorio/alterado.txt')

shutil.move(ROOT_PATH/'novo-diretorio/novo.txt', ROOT_PATH/'novo-diretorio/novo.txt')