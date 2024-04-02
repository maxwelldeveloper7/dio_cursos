"""Scripts para colab notebook"""

# Importando a biblioteca
import pandas as pd

# Leitura dos arquivos
df1 = pd.read_excel('Aracaju.xlsx')
df2 = pd.read_excel('Fortaleza.xlsx')
df3 = pd.read_excel('Natal.xlsx')
df4 = pd.read_excel('Recife.xlsx')
df5 = pd.read_excel('Salvador.xlsx')

# Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

# Exibindo as 5 primeiras linhas
df.head()

# Amostra de linhas de dados
df.sample(5)

# Exibindo as 5 últimas linhas
df.tail()

# Verificando o tipo de dados de cada coluna
df.dtypes

# Alterando o tipo de dado da coluna LojaID
df['LojaID'] = df['LojaID'].astype('object')

df.head()

df.isnull().sum()

# Substituindo os valores nulos pela média
df['Vendas'].fillna(df['Vendas'].mean(), inplace=True)

df.isnull().sum()

df.sample(15)

# Substituindo os valores nulos por zero
df['Vendas'].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=['Vendas'], inplace=True)

# Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how='all', inplace=True)

# Criando a coluna receita
df['Receita'] = df['Vendas'].mul(df['Qtde'])

df['Receita/Vendas'] = df['Receita'] / df['Vendas']

df.head()

# Retornando a maior receita
df['Receita'].max()

# Retornando a menor receita
df['Receita'].min()

# Retorna top 3 das maiores receitas
df.nlargest(3, 'Receita')

# Retorna top 3 das piores receitas
df.nsmallest(3, 'Receita')

# Agrupamento por cidade
df.groupby('Cidade')['Receita'].sum()

# Ordenanndo o conjunto de dados
df.sort_values('Receita', ascending=False).head(10)

# Transformando a coluna de data em tipo inteiro
df['Data'] = df['Data'].astype('int64')

# Verificando o tipo de dados de cada coluna
df.dtypes

# Transformando a coluna data do tipo inteiro para data
df['Data'] = pd.to_datetime(df['Data'])

# Agrupando por ano
df.groupby(df['Data'].dt.year)['Receita'].sum()

# Criando uma nova coluna com o ano
df['Ano_Venda'] = df['Data'].dt.year

df.sample(5)

#Extraindo o mês e o dia
df['mes_venda'], df['dia_venda'] = (df['Data'].dt.month, df['Data'].dt.day)

df.sample(5)

# Retornando a data mais antiga
df['Data'].min()

# Calculando a diferença de dias
df['diferenca_dias'] = df['Data'] - df['Data'].min()

df.sample(5)

# Criando a coluna de trimestre
df['trimestre_venda'] = df['Data'].dt.quarter

df.sample(5)

# Filtrando as venda de 2019 do mês de março
vendas_marco_19 = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]

vendas_marco_19

df['LojaID'].value_counts(ascending=False)

# Gráfico de barras
df['LojaID'].value_counts(ascending=False).plot.bar()

df['LojaID'].value_counts(ascending=False).plot.barh()

df['LojaID'].value_counts(ascending=True).plot.barh();

# Gráfico de Pizza
df.groupby(df['Data'].dt.year)['Receita'].sum().plot.pie();

# Total de vendas por cidade
df['Cidade'].value_counts()

# Adicionando um título e alterando o nome dos eixos
import matplotlib.pyplot as plt
df['Cidade'].value_counts().plot.bar(title='Total de Vendas por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas');

# Alterando a cor
import matplotlib.pyplot as plt
df['Cidade'].value_counts().plot.bar(title='Total de Vendas por Cidade', color='red')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas');

# Alterando o estilo
plt.style.use('ggplot')

df.groupby(df['mes_venda'])['Qtde'].sum().plot(title="Total de Produtos Vendidos por Mês")
plt.xlabel('Mês')
plt.ylabel('Total de Produtos Vendidos')
plt.legend();

df.groupby(df['mes_venda'])['Qtde'].sum()

# Selecionando apenas as vendas de 2019
df_2019 = df[df['Ano_Venda'] == 2019]

df_2019.groupby(df_2019['mes_venda'])['Qtde'].sum()

# Total de produtos vendidos por mês
df_2019.groupby(df_2019['mes_venda'])['Qtde'].sum().plot(marker = 'v')
plt.xlabel('Mês')
plt.ylabel('Total de Produtos Vendidos')
plt.legend();

# Histograma
plt.hist(df['Qtde'], color='magenta');

plt.scatter(x=df_2019['dia_venda'], y = df_2019['Receita']);

# Salvando em png
df_2019.groupby(df_2019['mes_venda'])['Qtde'].sum().plot(marker = 'v')
plt.title('Quantidade de produtos vendidos x mês')
plt.xlabel('Mês')
plt.ylabel('Total Produtos Vendidos')
plt.legend()
plt.savefig('grafico QTDE X MES.png');

