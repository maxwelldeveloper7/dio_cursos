from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()


# Trello API credentials
API_KEY = os.getenv('TRELLO_API_KEY')
API_SECRET = os.getenv('TRELLO_API_SECRET')
TOKEN = os.getenv('TRELLO_TOKEN')


def get_temporal_context():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def adicionar_tarefa(nome_da_task: str, descricao_da_task: str, due_date: str):
    client = TrelloClient(
        api_key=API_KEY,
        api_secret=API_SECRET,
        token=TOKEN
    )

    client.list_boards() # obter o board (você precisa do id do board para criar o card)
    boards = client.list_boards()
    meu_board = [b for b in boards if b.name == 'DIO'][0]

    # Obter a lista (você precisa do id da lista para criar o card)
    listas = meu_board.list_lists()

    minha_lista = [l for l in listas if l.name.upper() == 'TO DO' or l.name.upper() == 'A FAZER'][0]


    # Criar o card
    minha_lista.add_card(
        nome_da_task, 
        desc=descricao_da_task, 
        due=due_date
    )


def listar_tarefas(status: str = 'todas'):
    client = TrelloClient(
        api_key=API_KEY,
        api_secret=API_SECRET,
        token=TOKEN
    )

    boards = client.list_boards()
    meu_board = [b for b in boards if b.name == 'DIO'][0]

    # Obter as listas do board
    listas = meu_board.list_lists()

    # Filtrar as tarefas por status
    if status == 'todas':
        listas_filtradas = listas
    elif status == 'a fazer':
        listas_filtradas = [l for l in listas if l.name.upper() in ['A FAZER', 'TO DO', 'TODO']]
    elif status == 'em andamento':
        listas_filtradas = [l for l in listas if l.name.upper() in ['EM ANDAMENTO', 'DOING']]
    elif status == 'concluido':
        listas_filtradas = [l for l in listas if l.name.upper() in ['CONCLUÍDO', 'CONCLUIDO', 'DONE']]
    else:
        listas_filtradas = listas

    tarefas = []

    for lista in listas_filtradas:
        cards = lista.list_cards()
        for card in cards:
            tarefas.append({
                'nome': card.name,
                'descricao': card.desc,
                'vencimento': card.due,
                'status': lista.name,
                'id': card.id
            })

    return tarefas


def mudar_status_tarefa(nome_da_task: str, novo_status: str) -> str:
    try:
        client = TrelloClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            token=TOKEN
        )

        boards = client.list_boards()
        meu_board = [b for b in boards if b.name == 'DIO'][0]
        listas = meu_board.list_lists()

        # Mapear status para listas
        status_map = {
            "a fazer": "A FAZER",
            "em andamento": "EM ANDAMENTO",
            "concluido": "CONCLUÍDO"
        }
        
        nome_lista_destino = status_map.get(novo_status.lower())

        if not nome_lista_destino:
            return f"❌ Status inválido. Use: 'a fazer', 'em andamento' ou 'concluido'"
        
        # Encontrar lista de destino
        lista_destino = next(
            (l for l in listas if l.name.upper() == nome_lista_destino.upper()), 
            None
        )

        if not lista_destino:
            return f"❌ Lista '{nome_lista_destino}' não encontrada no board"
        
        # Buscar card em todas as listas
        card_encontrado = None
        lista_origem = None

        for lista in listas:
            cards = lista.list_cards()
            card_encontrado = next(
                (c for c in cards if c.name.lower() == nome_da_task.lower()), 
                None
            )
            if card_encontrado:
                lista_origem = lista
                break
        
        if not card_encontrado:
            return f"❌ Card '{nome_da_task}' não encontrado"
        
        # Mover
        card_encontrado.change_list(lista_destino.id)
        return f"✅ '{nome_da_task}': {lista_origem.name} → {lista_destino.name}"
    except Exception as e:
        return f"❌ Erro: {str(e)}"


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction="""
        Vocé é um agente de organização de tarevas.
        Sua função e receber uma tarefa e criar um card no Trello com o nome e descrição da tarefa.
        Você deve me perguntar as atividades que tenho no dia e criar um card para cada uma delas.
        Você inicia a conersa assim que for ativado, perguntado quais são as tarefas do dia.
        Sempre inicie a conversa perguntando quais são as tarefas do dia informando a data pela ferramenta agent_temporal_context,
        e depois vá perguntando se tem pais alguma tarefa, até que o usuário diga que não tem mais tarefas.
        Suas funções:
        1. Adicionar novas tarefas com nome e descrição.
        2. Listar todas as tarefas ou filtrar por status.
        3. Marcar tarefas como concluídas.
        4. Remover tarefas da lista
        5. Mudar o status da tarefa (ex: de "A fazer" para "Em andamento" ou "Concluída").
        6. Gerar contexto temporal (data e hora atual) para organizar as tarefas do dia.
    """,
    tools=[get_temporal_context, adicionar_tarefa, listar_tarefas, mudar_status_tarefa]
)
