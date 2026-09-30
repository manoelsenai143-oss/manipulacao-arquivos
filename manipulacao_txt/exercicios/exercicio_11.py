def listar_aprovados():
    with open("../alunos.txt", "r", encoding="utf-8") as arquivo:
        print("Alunos aprovados:")

        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota = float(dados[1])

            if nota >= 6:
                print(f"{nome} - {nota}")


listar_aprovados()