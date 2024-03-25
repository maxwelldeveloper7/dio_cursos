"""Implementando ping múltiplo"""
import os
import time


with open('hosts.txt', 'r', encoding='utf-8') as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print('Verificando o ip: ', ip)
        time.sleep(5)
        print('-' * 60)
        os.system('ping -c 2 ' + ip)
        print('-' * 60, '\n')
