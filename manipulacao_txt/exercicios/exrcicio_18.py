def gerenciar_notas():
    alunos = []

    with open("../notas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            aluno = {
                "nome": dados[0],
                "nota1": float(dados[1]),
                "nota2": float(dados[2]),
                "nota3": float(dados[3])
            }

            alunos.append(aluno)

    for aluno in alunos:
        media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3

        if media >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"{aluno['nome']} - Média: {media:.2f} - {situacao}")


gerenciar_notas()