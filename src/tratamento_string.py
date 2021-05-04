import re
import unidecode
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# Tokeniza : nltk.word_tokenize(string)

patterns = [
    r"http\S+",  # Links
    "#?bbb21" # tag bbb
]


def remove_patterns(string, patterns):
    pat = "|".join(patterns)
    filtro = re.compile(pat, flags=re.IGNORECASE)
    return re.sub(filtro, '', string)


stopwordpt = stopwords.words('portuguese')
stopwordpt = set(stopwordpt)

def remove_stop_words(tokens, stopwords_=stopwordpt):
    """Remover as Stopwords das palavras tokenizadas"""
    new_words = [palavra for palavra in tokens if palavra not in stopwords_]
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


def remove_radical(tokens):
    stemmer = SnowballStemmer('portuguese')
    return [stemmer.stem(token) for token  in tokens]

