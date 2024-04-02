"""Scripts para colab"""
# Importando a biblioteca pandas
import pandas as pd

# visualizando as 5 primeiras linhas
df.head()

# Renomeando campos
df = df.rename(columns={"country":"Pais", "continent":"continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap":"PIB"})

df.head(10)

# Total de linhas e colunas
df.shape

# Retornar nome das colunas
df.columns

# Tipo de dado em cada coluna
df.dtypes

df.tail(15)

df.describe()

df['continente'].unique()

oceania = df.loc[df['continente'] ==  'Oceania']
oceania.head()

oceania['continente'].unique()

df.groupby('continente')['Pais'].nunique()

df.groupby('Ano')['Expectativa de vida'].mean()

df['PIB'].mean()

df['PIB'].sum()
