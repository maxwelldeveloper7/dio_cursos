texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
print()

for numero in range(0, 61, 6):
    print(numero, end=" ")
