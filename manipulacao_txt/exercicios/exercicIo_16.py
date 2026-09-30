def buscar_produto():
    produtos = []

    with open("../produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            produto = {
                "nome": dados[0],
                "preco": float(dados[1]),
                "quantidade": int(dados[2])
            }

            produtos.append(produto)

    nome_produto = input("Digite o produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome_produto.lower():
            print("Produto encontrado!")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            break
    else:
        print("Produto não encontrado!")


buscar_produto()