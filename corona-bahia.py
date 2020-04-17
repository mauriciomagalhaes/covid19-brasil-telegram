import pandas as pd
import numpy as np

df = pd.read_csv('https://brasil.io/dataset/covid19/caso?format=csv')
cidades = df.loc[df.place_type == 'city']
data = cidades[['date', 'city', 'confirmed','deaths', 'is_last']]

cidade = 'Salvador'
dataplot = data.drop(['is_last'], axis=1)

df_cidade = dataplot.loc[data.city == cidade]
df_cidade = df_cidade.groupby('date').sum()
df_cidade.columns = ['Confirmados', 'Mortes']

print(df_cidade)
