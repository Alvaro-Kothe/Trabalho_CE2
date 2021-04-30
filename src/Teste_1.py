import json
import tratamento_string

outro_tweet = """  """

token = tratamento_string.normalize(outro_tweet)

with open("../SentiLex-PT02/dicionario_palavra.json") as palavra:
    dic_palavra = json.load(palavra)


print(token)
print(type(dic_palavra))

print(sum(dic_palavra.get(s,0) for s in token))