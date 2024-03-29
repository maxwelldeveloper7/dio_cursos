"""Implementa um comparador de hashes"""
import hashlib

ARQUIVO_A = 'a.txt'
ARQUIVO_B = 'b.txt'

hash1 = hashlib.sha256()

hash1.update(open(ARQUIVO_A, 'rb').read())

hash2 = hashlib.sha256()

hash2.update(open(ARQUIVO_B, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {ARQUIVO_A} é diferente do arquivo: {ARQUIVO_B}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {ARQUIVO_A} é igual ao arquivo: {ARQUIVO_B}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
