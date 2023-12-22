from  aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':

    tv = Televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)

    calc = Calculadora(5, 10)
    print(calc.soma())
    
    lista = ['cachorro', 'gato', 'elefante']
    total_letras =contador_letras(lista)
    print('total de letras por palavra de lista: {}'.format(total_letras))
    print(teste())