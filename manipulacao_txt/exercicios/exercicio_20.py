def sistema_alunos():
    alunos = []

    with open("../alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            aluno = {
                "id": int(dados[0]),
                "nome": dados[1],
                "idade": int(dados[2]),
                "curso": dados[3]
            }

            alunos.append(aluno)

    while True:
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("\nALUNOS:")

            for aluno in alunos:
                print(f"{aluno['id']} - {aluno['nome']} - {aluno['idade']} anos")

        elif opcao == "2":
            id_busca = int(input("Digite o ID: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_busca:
                    print("\nAluno encontrado:")
                    print(aluno["nome"])
                    print(f"{aluno['idade']} anos")
                    print(aluno["curso"])
                    encontrado = True

            if not encontrado:
                print("Aluno não encontrado!")

        elif opcao == "3":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            if alunos:
                novo_id = alunos[-1]["id"] + 1
            else:
                novo_id = 1

            aluno = {
                "id": novo_id,
                "nome": nome,
                "idade": idade,
                "curso": curso
            }

            alunos.append(aluno)

            with open("../alunos.txt", "w", encoding="utf-8") as arquivo:
                for aluno in alunos:
                    arquivo.write(
                        f"{aluno['id']};{aluno['nome']};"
                        f"{aluno['idade']};{aluno['curso']}\n"
                    )

            print("Aluno cadastrado com sucesso!")

        elif opcao == "4":
            id_remover = int(input("Digite o ID do aluno: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_remover:
                    alunos.remove(aluno)
                    encontrado = True
                    break

            if encontrado:
                with open("../alunos.txt", "w", encoding="utf-8") as arquivo:
                    for aluno in alunos:
                        arquivo.write(
                            f"{aluno['id']};{aluno['nome']};"
                            f"{aluno['idade']};{aluno['curso']}\n"
                        )

                print("Aluno removido com sucesso!")
            else:
                print("Aluno não encontrado!")

        elif opcao == "5":
            id_alterar = int(input("Digite o ID do aluno: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_alterar:
                    aluno["nome"] = input("Novo nome: ")
                    aluno["idade"] = int(input("Nova idade: "))
                    aluno["curso"] = input("Novo curso: ")

                    encontrado = True
                    break

            if encontrado:
                with open("../alunos.txt", "w", encoding="utf-8") as arquivo:
                    for aluno in alunos:
                        arquivo.write(
                            f"{aluno['id']};{aluno['nome']};"
                            f"{aluno['idade']};{aluno['curso']}\n"
                        )

                print("Aluno alterado com sucesso!")
            else:
                print("Aluno não encontrado!")

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


sistema_alunos()