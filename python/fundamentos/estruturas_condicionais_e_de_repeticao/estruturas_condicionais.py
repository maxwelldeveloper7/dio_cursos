MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade  = int(input('Informe a sua idade: '))

if idade >= MAIOR_IDADE:
    print('Mair de idade, pode tirar a CHN.')
if idade < MAIOR_IDADE:
    print('Ainda não pode tirar a CHN')


if idade >= MAIOR_IDADE:
    print('Mair de idade, pode tirar a CHN.')
else:
    print('Ainda não pode tirar a CHN')
    

if idade >= MAIOR_IDADE:
    print('Mair de idade, pode tirar a CHN.')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas')
else:
    print('Ainda não pode tirar a CHN')