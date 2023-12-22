T = input('Digite sua mensagem (no máximo 140 caracteres): ')

T = T.replace('0', 'zero')
T = T.replace('1', 'um')
T = T.replace('2', 'dois')
T = T.replace('3', 'três')
T = T.replace('4', 'quatro')
T = T.replace('5', 'cinco')
T = T.replace('6', 'seis')
T = T.replace('7', 'sete')
T = T.replace('8', 'oito')
T = T.replace('9', 'nove')


if len(T)>= 1 and len(T) <= 140:
    print("TWEET")
else:
    print("MUTE")