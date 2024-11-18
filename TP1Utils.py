def entrar_id_tarefa():
    '''
    Solicita ao usuário que insira o ID de uma tarefa.

    Retorna:
        int: O ID da tarefa inserido pelo usuário.
    '''
    id = int(input('Entre com o id da tarefa: '))
    return id

def entrar_nome_tarefa():
    '''
    Solicita ao usuário que insira o nome de uma tarefa e formata-o.

    Retorna:
        string: O nome da tarefa formatado.
    '''
    tarefa = input('Entre com o nome da tarefa: ')
    return f'-{tarefa}-'

def pesquisar_tarefa(tarefas, id):
    '''
    Pesquisa uma tarefa na lista de tarefas pelo ID.

    Parâmetros:
        tarefas (list): Lista de tarefas, onde cada tarefa é representada por uma tupla ou lista.
        id (int): O ID da tarefa a ser pesquisada.

    Retorna:
        list: A tarefa correspondente ao ID, ou uma lista vazia se não encontrada.
    '''
    tarefa_listada = []
    for tarefa in tarefas:
        if (id == tarefa[0]):
            tarefa_listada = tarefa
            break
    return tarefa_listada

def alterar_status():
    '''
    Solicita ao usuário que indique se a tarefa foi concluída, aceitando apenas respostas válidas.

    Returns:
        string: 's' para concluído ou 'n' para não concluído.
    '''
    while (True):
        status = input('Sua tarefa foi concluída? [S/N]: ').lower()
        if (status not in ('s', 'n')):
            print('Erro: Resposta Inválida')
        else:
            break
    return status