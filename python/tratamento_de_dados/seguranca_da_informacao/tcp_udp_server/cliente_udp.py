"""Implementa um cliente udp"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso!!!')

HOST = 'localhost'
PORTA = 5433
MENSAGEM = 'Olá servidor firmeza?'

try:
    print(f'Cliente: {MENSAGEM}')
    s.sendto(MENSAGEM.encode('utf-8'), (HOST, 5430))
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")
finally:
    print('Cliente: Fechando a conexão!')
    s.close()
