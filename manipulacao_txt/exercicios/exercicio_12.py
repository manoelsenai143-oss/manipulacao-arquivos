def classificar_alunos():
    with open("../alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota = float(dados[1])

            if nota >= 6:
                situacao = "Aprovado"
            elif nota >= 4:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            print(f"{nome} - {nota} - {situacao}")


classificar_alunos()