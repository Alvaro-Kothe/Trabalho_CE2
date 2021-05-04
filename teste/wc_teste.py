from wordcloud import WordCloud
import matplotlib.pyplot as plt
from src import tratamento_string
import pandas as pd
pd.set_option('display.max_columns', 500)
plt.figure(figsize=(8, 6), dpi=300)

tweets = pd.read_csv("../tweets_bbb21.csv")


tweets['tweet_chave'] = tweets.apply(lambda linha: tratamento_string.normalize(linha['texto']), axis=1) # Muito demorado normalizar



texto = tweets['tweet_chave'].str.join(' ')
tt = ' '.join(texto).upper()
wordcloud = WordCloud().generate(tt)

# Display the generated image:
# the matplotlib way:

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()