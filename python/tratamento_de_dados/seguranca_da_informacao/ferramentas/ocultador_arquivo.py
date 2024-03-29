"""Implementa um ocultador de arquivo"""
import ctypes

ATRIBUTOS_OCULTAR = 0x02
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', ATRIBUTOS_OCULTAR)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquino não foi ocultado')
