tarefas = []
option_user = True

try:
    while option_user:
        print("[1] Adicionar Tarefa")
        print("[2] Listar Tarefas")
        print("[3] Remover Tarefas")
        print("[4] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
            print("Deseja adicionar outra tarefa? (s/n)")
            response = input().lower()
            if response == "s":
                tarefa2 = input("Digite a tarefa: ")
                tarefas.append(tarefa2)
                print("Tarefa adicionada com sucesso!")
                break
            else:
                option_user = False

        elif opcao == "2":
            if len(tarefas) == 0:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("Tarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")
                option_user = False

        elif opcao == "3":
            if len(tarefas) == 0:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("Tarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")
                indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefas.pop(indice)
                    print("Tarefa removida com sucesso!")
                    print("Deseja remover outra tarefa? (s/n)")
                    response = input().lower()
                    if response == "s":
                        indice2 = int(input("Digite o número da tarefa que deseja remover: ")) - 1
                        if 0 <= indice2 < len(tarefas):
                            tarefas.pop(indice2)
                            print("Tarefa removida com sucesso!")
                        else:
                            print("Número de tarefa inválido.")
                    else:
                        option_user = False
                else:
                    print("Número de tarefa inválido.")

        elif opcao == "4":
            print("Saindo do programa...")
            option_user = False

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            print("Retornando ao menu principal...")

except ValueError as e:
    print(f"Você deve digitar um número válido. Erro: {e}")


