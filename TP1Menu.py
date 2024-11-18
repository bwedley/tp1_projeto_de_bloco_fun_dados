from TP1 import *

def exibir_menu():
    '''
    Exibe o menu principal com as opções disponíveis para o usuário
    '''
    print("----Menu----")
    print("[1] - Adicionar Tarefa")
    print("[2] - Listar Tarefas")
    print("[3] - Marcar Conclusão de Tarefas")
    print("[4] - Remover Tarefa")
    print("[0] - Sair")


def entrar_opcao():
    '''
    Exibe o menu e solicita ao usuário que insira uma opção.
    A função continua socilitando até que o usuário insira uma opção válida.
    Retorna
        int: A opção escolhida (0 a 4)
    '''
    while (True):
        exibir_menu()
        opcao = int(input("Entre com a opção: "))
        if (opcao not in(0, 1, 2, 3, 4, 5)):
            print("Erro: opção inválida")
        else:
            break
    return opcao



def main(): 
    '''
    Função de fluxo principal do programa
    '''
    opcao = entrar_opcao()
    while (opcao != 0):
        match (opcao):
            case 1: adicionar_tarefa(tarefas_pendentes)
            case 2: listar_tarefas(tarefas_pendentes)
            case 3: marcar_concluida(tarefas_pendentes)
            case 4: remover_tarefa(tarefas_pendentes)
            case _: print("Erro: opção inválida")
        opcao = entrar_opcao()

main()