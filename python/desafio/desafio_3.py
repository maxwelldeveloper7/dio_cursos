n = int(input())

encaixa = True

while(n > 0):
    a = 0
    while a < 1:
        a = int(input())
    b = 0
    while b < 1:
        b = int(input())
    
    
    a = str(a)
    b = str(b)
        
    a_maior_igual_b = len(a) >= len(b)
    
    encaixa = a_maior_igual_b and a[-len(b):] == b
    
    if encaixa:        
        print('encaixa')    
    else:
        print('nao encaixa')
    n -= 1