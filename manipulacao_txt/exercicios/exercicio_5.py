def contar_caracteres():
    with open("../texto.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

        print(f"Quantidade de caracteres: {len(texto)}")


contar_caracteres()