from TP1Utils import *

tarefas_pendentes = [[1, "-Varrer a casa-","-Pendente-"], [2, "-Lavar as louças-", "-Pendente-"]]

def adicionar_tarefa(tarefa):
    '''
    Adiciona uma nova tarefa à lista de tarefas.

    Verifica se o ID da tarefa já existe na lista antes de adicionar. Caso o ID seja único, 
    solicita o nome da tarefa e a adiciona com o status padrão inicial "-Pendente-".
    
    Parâmetros:
        tarefa (list): Lista de tarefas pendentes onde a nova tarefa será adicionada.
    '''
    id = entrar_id_tarefa()
    tarefa_existente = pesquisar_tarefa(tarefa, id)
    if (tarefa_existente):
        print('Erro: Tarefa já consta na lista')
        return
    nome_tarefa = entrar_nome_tarefa()
    status = '-Pendente-'
    adiciona_tarefa = [id, nome_tarefa, status]
    tarefa.append(adiciona_tarefa)

def listar_tarefas(tarefas):
    '''
    Exibe todas as tarefas com seus IDs, nomes e status.
    Parâmetros:
        tarefas (list): Lista contendo as tarefas a serem exibidas. 
                        Cada tarefa é uma lista [ID, Nome, Status].
    '''
    for id, nome, status in tarefas:
        print(id, nome, status)
    print()

def marcar_concluida(tarefas):
    '''
    Marca uma tarefa específica como concluída.

    Solicita o ID da tarefa e altera seu status para "-Concluída-",
    caso o status seja confirmado. Caso o ID não exista, exibe uma mensagem de erro.

    Parâmetros:
        tarefas (list): Lista de tarefas onde o status será atualizado.
    '''

    id = entrar_id_tarefa()
    tarefa = pesquisar_tarefa(tarefas, id)
    if (not tarefa):
        print('Erro: tarefa não encontrada')
        return
    status = alterar_status()
    if (status == 's'):
        tarefa[2] = '-Concluída-'
    else:
        tarefa[2]

def remover_tarefa(tarefas):
    '''
    Remove uma tarefa da lista de tarefas.

    Solicita o ID da tarefa a ser removida. Caso a tarefa seja encontrada,
    ela é removida da lista. Caso contrário, exibe uma mensagem de erro.

    Parâmetros:
        tarefas (list): Lista de tarefas de onde a tarefa será removida.
    '''
    
    id = entrar_id_tarefa()
    tarefa = pesquisar_tarefa(tarefas, id)
    if (not tarefa):
        print('Erro: Tarefa não encontrada')
        return
    tarefas.remove(tarefa)
