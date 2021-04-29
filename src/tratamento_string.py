import re
import unidecode
from nltk import word_tokenize
from nltk.corpus import stopwords

# Tokeniza : nltk.word_tokenize(string)

patterns = [
    r"http\S+",  # Links
    "#?bbb21" # tag bbb
]


def remove_patterns(string, patterns):
    pat = "|".join(patterns)
    filtro = re.compile(pat, flags=re.IGNORECASE)
    return re.sub(filtro, '', string)


def remove_stop_words(tokens):
    """Remover as Stopwords das palavras tokenizadas"""
    stopwordpt = stopwords.words('portuguese')
    stopwordpt = set(stopwordpt)
    new_words = [palavra for palavra in tokens if palavra not in stopwordpt]
    return new_words


def to_ascii(tokens):
    """remover acentos"""
    return [unidecode.unidecode(w) for w in tokens]


def remove_pontuacao(tokens):
    """remover pontuacao"""
    sem_pontuacao = [re.sub(r'[^\w\s]', '', palavra) for palavra in tokens]
    return [tkn for tkn in sem_pontuacao if tkn]


def to_lowercase(tokens):
    """converter todos os caracteres para lowercase"""
    return [w.lower() for w in tokens]


def normalize(string, pattern=patterns):
    """Normaliza a string (remove stopwords, pontuacao e deixa em caixa baixa)
    recebe: string
    Retorna: string normalizada"""
    string = remove_patterns(string, pattern)
    tokens = word_tokenize(string)
    tokens = to_ascii(tokens)
    tokens = to_lowercase(tokens)
    tokens = remove_pontuacao(tokens)
    tokens = remove_stop_words(tokens)
    return tokens


if __name__ == '__main__':
    # Testes
    s = """***

Se o próximo Paredão for este, que será ELIMINADO ???

Arthur X Gilberto X Pocah

#BBB21 #RedeBBB #ForaViihTube #FestaBBB
8 MILHÕES DO RODOLFFO / PARABÉNS KERLINE /
PARABENS CAON / Mais Você / Alok"""
    outro_tweet = """genteeee eu amei o jogo KKKSKSKSKSK a voz da juliette ""vai te lascar pra lá"" #BBB21 https://t.co/VJ1xNNL4M7"""
    tok = word_tokenize(outro_tweet)
    print(remove_stop_words(tok))
    print(to_ascii(tok))
    print(to_lowercase(s))
    print(normalize(s))
