def contar_linhas():
    with open("../nomes.txt", "r", encoding="utf-8") as arquivo:
        linhas = 0

        for linha in arquivo:
            linhas += 1

        print(f"O arquivo possui {linhas} linhas.")


contar_linhas()