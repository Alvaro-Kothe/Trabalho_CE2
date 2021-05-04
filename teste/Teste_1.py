from src import tratamento_string, candidatos
import pandas as pd

#### Lendo os dados ######

tweets = pd.read_csv("../tweets_bbb21.csv")
tweets['tweet_chave'] = tweets.apply(lambda linha: tratamento_string.normalize(linha['texto']), axis=1)
tweets['ind_candidato'] = tweets.apply(lambda linha: candidatos.dicionario_candidato(linha['texto']), axis=1)
tweets['sentimento'] = tweets.apply(lambda  linha: candidatos.soma_sentimento(linha['tweet_chave']), axis =1)
tweets = tweets.join(pd.DataFrame(tweets.pop('ind_candidato').tolist()))

print(tweets.columns)


tweets.sentimento.head()
#### aplicando a busca no dicionário para todos os tweets

