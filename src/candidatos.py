import re

candidatos = ('Gil', 'Juliette', 'Camilla', 'Pocah', 'Fiuk', 'Arthur')
patterns = ("gil", "juliet{1,2}e", 'camil{1,2}a', "pocah", "fiuk", "arthur")


def dicionario_candidato(string, lista=candidatos, repattern=patterns):
    return {k: bool(re.search(pattern, string, re.IGNORECASE)) for k, pattern in
            zip(lista, repattern)}
