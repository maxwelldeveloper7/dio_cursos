"""Implementa threads"""

from threading import Thread
import time

def carro(velocidade, piloto):
    """Implementa um carro em um trajeto"""
    trajeto = 0
    while trajeto <=100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto} Km: {trajeto}\n')


t_carro1 = Thread(target=carro, args=[1, 'Maxwell'])
t_carro2 = Thread(target=carro, args=[1.1, 'Python'])

t_carro1.start()
t_carro2.start()
