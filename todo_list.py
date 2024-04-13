#Define a lista de tarefas
tarefas = []

#função para adicionar uma nova tarefa à lista
def adicionar_tarefa():
    nova_tarefa = input("Digite a nova tarefa: ")
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")
    
#função para remover uma tarefa da lista
def remover_tarefa():
    if not tarefas:
        print("A lista de tarefas está vazia.")
        return
    
print("Lista de Tarefas:")
for i, tarefa in enumerate(tarefas, start=1):
    print(f"{i}.{tarefa}")
    
indice = int(input("Digite o número da tarefa que deseja remover: "))
if 1 <= indice <= len(tarefas):
    tarefa_removida = tarefas.pop(indice - 1)
    print(f"Tarefa '{tarefa_removida} removida com sucesso!")
else:
    print("Índice inválido.")
    
#Função para exibir todas as tarefas da lista
def exibir_tarefas():
    if not tarefas:
        print("A lista de tarefas está vazia.")
        return
    
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")
        
#Loop principal do programa
def main():
    while True:
        print("\n==== Menu de Opções ====")
        print("1. Adicionar Tarefa.")
        print("2. Remover Tarefa.")
        print("3. Exibir Tarefa.")
        print("4. Sair do Programa.")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            remover_tarefa()
        elif opcao == "3":
            exibir_tarefas()
        elif opcao == "4":
            print("Saindo do programa...")    
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")

if __name__ =="__main__":
    main()