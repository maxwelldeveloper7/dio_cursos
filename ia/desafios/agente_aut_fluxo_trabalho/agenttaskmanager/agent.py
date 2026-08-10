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
        TO DO contunuar em 7:00 minutos


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
    tools=[get_temporal_context, adicionar_tarefa]
)
