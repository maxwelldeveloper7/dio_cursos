"""Implementa um servidor"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso!')

HOST = 'localhost'
PORT =  5430

s.bind((HOST, PORT))
MENSAGEM = '\nServidor: Olá cliente e aí beleza?'

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (MENSAGEM.encode('utf-8')), end)
