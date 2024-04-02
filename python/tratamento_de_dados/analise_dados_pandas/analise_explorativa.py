"""Scripts utilizados no calab notebook"""

# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8');

# Upload do arquivo
from google.colab import files
arq = files.upload()

# Criando nosso DataFrame
df = pd.read_excel('AdventureWorks.xlsx')

# Visualizando as 5 primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape

# Verificando os tipos de dados
df.dtypes

# Qual foi a Receita total?
df['Valor Venda'].sum()

# Qual é o custo Total?
df['custo'] = df['Custo Unitário'].mul(df['Quantidade'])  # Criando a coluna de custo

df.head(1)

# Qual é o custo Total?
round(df['custo'].sum(), 2)

# Agora que temos a receita e custo e o total, podemos achar o Lucro total
# Vamos criar uma coluna de Lucro que será Receita - Custo
df['lucro'] = df['Valor Venda'] - df['custo']

df.head(1)

# Total Lucro
round(df['lucro'].sum(), 2)

# Criando uma coluna com total de dias para enviar o produto
df['Tempo_envio'] = df['Data Envio'] - df['Data Venda']

df.head(1)

# Extraindo apenas os dias
df['Tempo_envio'] = (df['Data Envio'] - df['Data Venda']).dt.days

df.head(1)

# Verificando o tipo da coluna Tempo_envio
df['Tempo_envio'].dtype

# Média do tempo de envio por Marca
df.groupby('Marca')['Tempo_envio'].mean()

# Verificando se temos dados faltantes
df.isnull().sum()

# Formata a exibição de dados de número flutuante
pd.options.display.float_format = '{:20,.2f}'.format

# Vamos Agrupar por ano e marca
df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum()

# Resetando o index
lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum().reset_index()
lucro_ano

# Qual o total de produtos vendidos?
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

# Gráfico com total de produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title='Total de Produtos Vendidos')
plt.xlabel('Total')
plt.ylabel('Produto');

df.groupby(df['Data Venda'].dt.year)['lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita');

df.groupby(df['Data Venda'].dt.year)['lucro'].sum()

# Selecionando apenas as vendas de 2009
df_2009 = df[df['Data Venda'].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009['Data Venda'].dt.month)['lucro'].sum().plot(title='Lucro x Mês')
plt.xlabel('Mês')
plt.ylabel('Lucro');

df_2009.groupby('Marca')['lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');

df_2009.groupby('Classe')['lucro'].sum().plot.bar(title='Lucro x Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');

df['Tempo_envio'].describe()

# Gráfico de Boxplot
plt.boxplot(df['Tempo_envio']);

# Histograma
plt.hist(df['Tempo_envio']);

# Tempo mínimo de envio
df['Tempo_envio'].min();

# Tempo máximo de envio
df['Tempo_envio'].max();

# Identificando o Outlier
df[df['Tempo_envio'] == 20]

df.to_csv('df_vendas_novo.csv', index=False)
