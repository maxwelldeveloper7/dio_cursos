def encaixa(A, B):
    """Verifica se B corresponde aos últimos dígitos de A.

    Args:
        A: O primeiro valor.
        B: O segundo valor.

    Returns:
        True se B corresponde aos últimos dígitos de A, False caso contrário.
    """

    A_tamanho = len(A)
    B_tamanho = len(B)

    if B_tamanho > A_tamanho:
        return False

    A_final = A[-B_tamanho:]

    return A_final == B


def main():
   
    if encaixa("56234523485723854755454545478690", "78690"):
        print("encaixa")
    else:
        print("nao encaixa")


if __name__ == "__main__":
    main()
