"""Implementa um gerador de lista de palavras"""
import itertools

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))
