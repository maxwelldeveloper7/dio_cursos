print('True and True: {}'.format(True and True))
print('True and False: {}'.format(True and False))
print('False and False: {}'.format(False and False))
print('True or True: {}'.format(True or True))
print('True or False: {}'.format(True or False))
print('False or False: {}'.format(False or False))

saldo = 1000
saque = 250
limite = 200
conta_especial = True


saque_autorizado = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
saque_autorizado = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print('Saque autorizado {}'.format(saque_autorizado))