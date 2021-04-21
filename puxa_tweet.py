import tweepy
import os
import json

numero_tweets = 5000
freq_printa = 10

consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET_KEY')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

pesquisa = "#BBB21 -filter:retweets"  # Filtra pela # e remove retweets
# inicio = "2021-01-25"
ultimos_tweets = []
max_id = None

for pesquisa in range(numero_tweets // 100):
    # Le os tweets em ordem decrescente
    tweets = api.search(q=pesquisa,
                        tweet_mode="extended", lang='pt', max_id=max_id,
                        count=100, include_entities=False)

    ultimos_tweets += [status._json for status in tweets]
    max_id = ultimos_tweets[-1]["id"] - 1
    if pesquisa % freq_printa:
        print(max_id)

with open("tweets_json_bbb21.txt", "w") as arquivo:
    arquivo.write(json.dumps(ultimos_tweets, indent=4))
