# Criando um Agente para Automatizar um Fluxo de Trabalho em Python

Este projeto é uma implementação de um desafio de projeto da DIO para criar um agente inteligente capaz de automatizar a gestão de tarefas em um fluxo de trabalho diário, integrando Python, IA e um sistema de organização de tarefas.

O agente foi desenvolvido para interagir com o Trello, uma ferramenta de organização de listas e cartões, e criar, listar e atualizar tarefas de forma automatizada a partir de conversas com o usuário.

## Descrição do desafio

O desafio da DIO, intitulado "Criando um Agente para Automatizar um Fluxo de Trabalho em Python", tem como objetivo demonstrar como combinar:

- Python como linguagem principal;
- Inteligência artificial para interpretar e responder a solicitações do usuário;
- APIs de serviços externos para automatizar processos reais;
- Ferramentas de produtividade para organizar tarefas.

A ideia central é criar um agente que entenda o contexto de trabalho e execute ações como:

- registrar novas tarefas;
- classificar tarefas por status;
- listar tarefas existentes;
- mover tarefas entre listas;
- organizar o planejamento do dia.

## Objetivo do projeto

O objetivo deste projeto é criar um agente de organização pessoal que:

1. pergunta ao usuário quais tarefas fazem parte do seu dia;
2. cria cartões no Trello para cada tarefa informada;
3. organiza essas tarefas em listas como "A Fazer", "Em andamento" e "Concluído";
4. permite consultar as tarefas por status;
5. auxilia no acompanhamento de rotina e produtividade.

## Como o projeto funciona

O projeto usa o Google Agent Development Kit (Google ADK) para criar um agente inteligente e o Trello como backend de organização de tarefas.

O agente define ferramentas que permitem:

- obter o contexto temporal atual;
- adicionar tarefas ao Trello;
- listar tarefas por status;
- alterar o status de uma tarefa.

O agente principal é definido em `agenttaskmanager/agent.py` e se chama `root_agent`.

## Estrutura do projeto

```text
agente_aut_fluxo_trabalho/
├── requirements.txt
├── README.md
└── agenttaskmanager/
    ├── __init__.py
    └── agent.py
```

### Arquivos principais

- `requirements.txt`: lista as dependências do projeto.
- `agenttaskmanager/agent.py`: contém a lógica do agente, a integração com o Trello e as ferramentas disponíveis.
- `agenttaskmanager/__init__.py`: exporta o módulo do agente.

## Dependências

As bibliotecas utilizadas no projeto são:

- `google-adk`
- `py-trello`
- `python-dotenv`

Essas dependências estão declaradas no arquivo `requirements.txt`.

## Configuração

Antes de executar o projeto, é necessário configurar as credenciais da API do Trello no arquivo `.env`.

Crie um arquivo `.env` com as seguintes variáveis:

```env
TRELLO_API_KEY=sua_api_key
TRELLO_API_SECRET=sua_api_secret
TRELLO_TOKEN=seu_token
```

Também é importante que exista um quadro no Trello chamado `DIO` e que ele contenha listas como:

- `A FAZER`
- `EM ANDAMENTO`
- `CONCLUÍDO`

A lógica do código procura por esse nome de board e essas listas para criar e mover os cartões.

## Funcionalidades implementadas

### 1. Contexto temporal

A função `get_temporal_context()` gera a data e a hora atuais, permitindo ao agente contextualizar a organização das tarefas do dia.

### 2. Criação de tarefas

A função `adicionar_tarefa()` recebe:

- nome da tarefa;
- descrição;
- data de vencimento;

e cria um cartão no Trello na lista de "A Fazer".

### 3. Listagem de tarefas

A função `listar_tarefas()` busca os cartões do board e pode filtrar por:

- todas;
- a fazer;
- em andamento;
- concluido.

### 4. Alteração de status

A função `mudar_status_tarefa()` consegue mover uma tarefa entre listas do Trello, conforme o status solicitado.

## Fluxo de uso do agente

A ideia do agente é orientar a conversa da seguinte maneira:

- perguntar quais são as tarefas do dia;
- inserir cada tarefa como um cartão no Trello;
- confirmar organização e status;
- responder às solicitações de consulta e atualização.

O agente foi configurado com instruções que definem seu papel como um assistente de organização de tarefas.

## Exemplo de comportamento

Um exemplo comum de interação seria:

- usuário: "Quais são as tarefas do dia?"
- agente: responde com o contexto temporal e pergunta quais tarefas devem ser adicionadas;
- usuário: informa tarefas como "Estudar Python", "Revisar projeto", "Enviar relatório";
- agente cria os cartões correspondentes no Trello.

## Observação

Este projeto funciona como exemplo prático de integração entre IA e automação de tarefas do cotidiano. Ele demonstra como um agente pode agir como um assistente produtivo, reduzindo a necessidade de execução manual de tarefas repetitivas.

## Conclusão

Este projeto representa uma aplicação concreta do desafio da DIO de combinar Python, agentes de IA e automação de fluxo de trabalho. Ele mostra como ferramentas modernas podem ser usadas para transformar interações em ações reais, conectando um assistente inteligente a um sistema de organização como o Trello.

## Autor

Projeto desenvolvido como parte de um desafio de projeto da DIO, com foco em automação de fluxo de trabalho usando Python e agentes inteligentes.
