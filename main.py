import pandas as pd
import unidecode

# Usar unidecode para remover caracter especial do texto

df = pd.read_csv("tweets_bbb21.csv")
id = df['id'].unique()
print(df.shape)
print(len(id))