from src import candidatos, tratamento_string

import pandas as pd

pd.set_option('display.max_columns', 500)

tweets = pd.read_csv("../tweets_bbb21.csv")


# tweets['tweet_chave'] = tweets.apply(lambda linha: tratamento_string.normalize(linha['texto']), axis=1) # Muito demorado normalizar
# print(tweets.tweet_chave[0])
tweets['ind_candidato'] = tweets.apply(lambda linha: candidatos.dicionario_candidato(linha['texto']), axis=1)
print(tweets.columns)
tweets = tweets.join(pd.DataFrame(tweets.pop('ind_candidato').tolist()))
print(tweets.columns)
print(tweets.head())
