"""Implementa om cliente tcp"""
import socket
import sys

def main():
    """Tenta abrir um socket do tipo tcp"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falou!!!")
        print(f'Erro: {e}')
        sys.exit()
    print("Socket criado com sucesso")

    host_alvo = input("Digite o Host ou Ip a ser conectado: ")
    porta_alvo = int(input("Digite a porta a ser conectada: "))

    try:
        s.connect((host_alvo, porta_alvo))
        print(f"Cliente TCP conectado com Sucesso no Host: {host_alvo}, na porta{porta_alvo}")
        s.shutdown(2)
    except socket.error as e:
        print(f'Não foi possível conectar no host: {host_alvo} - porta: {porta_alvo}')
        print(f'Erro: {e}')
        sys.exit()


if __name__ == '__main__':
    main()
