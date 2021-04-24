import tweepy
import os
import csv
import pandas as pd


def busca_tweets(api, pesquisa, since_id, max_id):
    tweets = api.search(q=pesquisa,
                        tweet_mode="extended", lang='pt', since_id=since_id, max_id=max_id,
                        count=100, include_entities=False)

    if not tweets:
        return

    tweet_data = [{'id': tweet.id,
                   'criado_em': tweet.created_at.isoformat(),
                   'texto': tweet.full_text,
                   'usuario': tweet.user.screen_name,
                   'localizacao': tweet.user.location,
                   'qnt_retweets': tweet.retweet_count,
                   'qnt_favoritos': tweet.favorite_count} for tweet in tweets]
    return tweet_data


def main():
    # API
    consumer_key = os.environ.get('TWITTER_API_KEY')
    consumer_secret = os.environ.get('TWITTER_API_SECRET_KEY')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Arquivo de saida
    arquivo_saida = "tweets_bbb21.csv"
    file_exists = os.path.isfile(arquivo_saida)

    # Busca
    numero_buscas = 1e3
    buscas = 0

    pesquisa = "bbb21 -filter:retweets"

    with open(arquivo_saida, 'a+', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'criado_em', 'texto', 'usuario', 'localizacao', 'qnt_retweets', 'qnt_favoritos']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            # Cria o arquivo
            id_min = 0
            writer.writeheader()
        else:
            # Se o arquivo existe vai adicionar no arquivo
            reader = pd.read_csv(arquivo_saida)
            id_min = reader.id.max()
        try:
            max_id = None
            while buscas < numero_buscas:
                busca = busca_tweets(api, pesquisa, id_min, max_id)
                if not busca:
                    print(f"Realizou buscas até a busca {buscas}")
                    break
                buscas += 1
                max_id = busca[-1]['id'] - 1
                writer.writerows(busca)
        except tweepy.RateLimitError:
            print("Limite da API excedido")


if __name__ == '__main__':
    main()
