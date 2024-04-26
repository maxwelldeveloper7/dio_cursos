# Entrada do usuário
cogumelo_desejado = input().strip().title()  # Padroniza a entrada

# Função para sugerir cogumelos com preços mais baixos com base no cogumelo desejado
def sugerir_cogumelos(cogumelo_desejado):
    # Dicionário de cogumelos e seus preços
    catalogo = {
        "Shitake": 10,
        "Portobelo": 8,
        "Shimeji": 6,
        "Champignon": 12,
        "Funghi": 16,
        "Porcini": 16,
    }

    # Verifica se o cogumelo desejado está no catálogo
    if cogumelo_desejado not in catalogo:
        print("Este cogumelo não está na lista")
        return

    valor_desejado = catalogo[cogumelo_desejado]
    sugestoes = []

    # Procura por cogumelos mais baratos no catálogo
    for cogumelo, valor in catalogo.items():
        if valor < valor_desejado:  # Estritamente menor
            sugestoes.append((cogumelo, valor))
            if len(sugestoes) == 2:  # Limitar a duas sugestões
                break

    # Verifica se há sugestões
    if not sugestoes:
        print("Desculpe, não há sugestões")
    else:
        print("Sugestões de cogumelos mais baratos:")
        for sugestao, valor_sugestao in sugestoes:
            print(f"{sugestao} - Valor: {valor_sugestao}")

# Chamada da função para sugerir cogumelos
sugerir_cogumelos(cogumelo_desejado)
