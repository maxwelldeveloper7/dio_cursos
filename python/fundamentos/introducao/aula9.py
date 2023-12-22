import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w') # parâmetro 'w' apenas para escrita
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a') # parâmetro 'a' atualiza o texto do arquivo
    arquivo.write(texto)
    arquivo.close()


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    aluno_nota.pop() # apaga a ultima linha vazia
    #print(aluno_nota)
    lista_media = [] # variável de retorno que retornará uma lista de dicionários
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / len(lista_notas)
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '../')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '../')

if __name__ == '__main__':
    move_arquivo('./notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha. \n')
    # aluno = 'Cesar,7,9,3,8\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('./teste.txt')