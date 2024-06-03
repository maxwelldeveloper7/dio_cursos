arquivo = open("lorem.txt", "r")
# print(arquivo.read())
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()