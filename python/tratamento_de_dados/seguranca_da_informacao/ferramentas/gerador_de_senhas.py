"""Implementa um gerador de senhas"""
import random
import string

TAMANHO = int(input("Digite a quantidade de caracteres que sua senha deva ter: "))
CHARS = string.ascii_letters + string.digits + "'!@#$%&*()-=+,.;:/?'ç"

rnd = random.SystemRandom()

print(''.join(rnd.choice(CHARS) for i in range(TAMANHO)))
