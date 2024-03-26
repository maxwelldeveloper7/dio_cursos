"""Implementando um ping"""
import os

print('#' * 60)
ip_ou_host = input('Digite o Ip ou host a ser verificado: ')
print('-' * 60)
os.system(f'ping {ip_ou_host}')
