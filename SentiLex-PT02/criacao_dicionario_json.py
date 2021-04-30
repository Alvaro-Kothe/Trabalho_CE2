import json
import re
sentilexpt = open('SentiLex-flex-PT02.txt', encoding='utf-8')

#Criando um dicionário de palavras com a respectiva polaridade.
dic_palavra_polaridade = {}
dic_radical_polaridade = {}

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

for i in sentilexpt.readlines():
  pos_ponto = i.find('.')
  palavra = (i[:pos_ponto])
  palavra,radical = palavra.split(',')
  polaridades = re.findall(r"N[01]=(.+?);",i)
  polaridade = sum(float(x) for x in polaridades)/len(polaridades)
  dic_palavra_polaridade[palavra] = polaridade
  if radical not in dic_radical_polaridade:
    dic_radical_polaridade[radical] = polaridade

print(list( dic_palavra_polaridade.items())[0:12])
print(len(dic_palavra_polaridade))
print(len(dic_radical_polaridade))

sentilexpt.close()

with open("dicionario_palavra.json","w") as palavra,\
    open("dicionario_radical.json","w") as radical:
    json.dump(dic_palavra_polaridade,palavra)
    json.dump(dic_radical_polaridade,radical)

