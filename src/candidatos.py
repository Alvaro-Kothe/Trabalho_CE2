import re
import json


candidatos = ('Gil', 'Juliette', 'Camilla',
              'Pocah', 'Fiuk', 'Arthur', "Karol",
              "Sarah", "Viih Tube")
patterns = ("gil", "juliet{1,2}e", 'camil{1,2}a',
            "pocah", "fiuk", "arthur", "[kc]arol",
            "sarah?","vi{1,2}h? tube")


def dicionario_candidato(string, lista=candidatos, repattern=patterns):
    return {k: bool(re.search(pattern, string, re.IGNORECASE)) for k, pattern in
            zip(lista, repattern)}

with open("SentiLex-PT02/dicionario_palavra.json") as palavra:
    dic_palavra = json.load(palavra)


def soma_sentimento(token):
    return sum(dic_palavra.get(s,0) for s in token)


