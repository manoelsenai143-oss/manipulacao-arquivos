def gerar_relatorio():
    vendas = []

    with open("../vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            venda = {
                "vendedor": dados[0],
                "produto": dados[1],
                "valor": float(dados[2])
            }

            vendas.append(venda)

    total_vendas = 0
    quantidade_vendas = {}

    print("VENDAS:")

    for venda in vendas:
        print(f"{venda['vendedor']} - {venda['produto']} - R$ {venda['valor']:.2f}")

        total_vendas += venda["valor"]

        vendedor = venda["vendedor"]

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] += 1
        else:
            quantidade_vendas[vendedor] = 1

    print(f"\nTOTAL DE VENDAS: R$ {total_vendas:.2f}")

    print("\nQuantidade de vendas:")

    for vendedor, quantidade in quantidade_vendas.items():
        print(f"{vendedor}: {quantidade}")


gerar_relatorio()