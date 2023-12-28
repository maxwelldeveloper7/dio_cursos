T = int(input())

for i in range(T):
    garrafas = input().split()
    N = int(garrafas[0])
    K = int(garrafas[1])
    
    numero_de_garrafas_vazias = N
    numero_de_garrafas_cheias = 0
    
    while numero_de_garrafas_vazias >= K:
        numero_de_garrafas_vazias -= K
        numero_de_garrafas_cheias += 1
    
    numero_maximo_de_garrafas = numero_de_garrafas_vazias + numero_de_garrafas_cheias
    
    print(numero_maximo_de_garrafas)
    

# def calcular_numero_de_garrafas(n, k):
#   """
#   Calcula o número de garrafas que um cliente terá no segundo dia de uma promoção de refrigerantes.

#   Args:
#     n: número de garrafas compradas no primeiro dia.
#     k: número de garrafas vazias para ganhar uma cheia.

#   Returns:
#     O número de garrafas que o cliente terá no segundo dia.
#   """

#   numero_de_garrafas_vazias = n
#   numero_de_garrafas_cheias = 0

#   while numero_de_garrafas_vazias >= k:
#     numero_de_garrafas_vazias -= k
#     numero_de_garrafas_cheias += 1

#   return numero_de_garrafas_cheias + numero_de_garrafas_vazias


# if __name__ == "__main__":
#   t = int(input())

#   for _ in range(t):
#     n, k = map(int, input().split())

#     print(calcular_numero_de_garrafas(n, k))
