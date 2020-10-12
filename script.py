import requests, re, string, time
import time
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')

# Repositório Fake.br-Corpus com os textos em TXT: https://github.com/roneysco/Fake.br-Corpus
URL = 'https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/'

TEXT_TRUE = 'full_texts/true/'
TEXT_TRUE_META_INFORMATION = 'full_texts/true-meta-information/'
TEXT_FALSE = 'full_texts/false/'
TEXT_FAKE_META_INFORMATION = 'full_texts/fake-meta-information/'

# Número de notícias falsas e verdadeiras
TEXT_NUMBER = 3602
TEXT_NUMBER = 3

def textClean(text):
    '''
    Método responsável por realizar a limpeza do texto passado como parâmetro
    '''
    # Realiza a substituição de todos os caracteres diferentes do regex abaixo
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)

    # Coloca o texto em lowercase e realiza um slip no espaço
    text = text.lower().split()

    # Remove stopwords
    stops = set(nltk.corpus.stopwords.words('portuguese'))
    text = [w for w in text if not w in stops]
    text = " ".join(text)

    # Atualiza a string sem os caracteres de pontuação
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def generateNews(df, rota, fake_news):
    '''
    Método responsável por gerar as notícias de acordo com os parâmetros fornecidos
    '''
    falhas = 0
    falhasText = []

    for i in range(1, TEXT_NUMBER + 1):
        req = requests.get(URL + rota + str(i) + '.txt')
        if req.status_code == requests.codes.ok:
            df = df.append({'ID': i, 'fake_news': fake_news, 'text': textClean(req.text)}, ignore_index=True)
        else:
            falhas += 1
            falhasText.append(i)

    return [
        df,
        falhas,
        falhasText,
    ]

# Criação da DataFrame
columns = ['ID', 'fake_news', 'text']
# fake_news => 1 = True, 0 = False
df = pd.DataFrame(columns = columns)

print('Iniciano a criação do CSV')

inicio = time.time()
falhas = 0
falhasText = []

result = generateNews(df, TEXT_TRUE, 0)
df = result[0]
falhas = result[1]
falhasText = result[2]

fim = time.time()

# Realiza a criação do CSV
df.to_csv('dataset.csv')

print('CSV criado com sucesso! ')
print('Número de falhas: %i' %(falhas))
print('Falhas nos textos: ', falhasText)
print('Tempo de execução: %f minutos' %((fim - inicio) / 60))



##### COLUNAS #####
# author
# link
# category
# date of publication
# number of tokens
# number of words without punctuation
# number of types
# number of links inside the news
# number of words in upper case
# number of verbs
# number of subjuntive and imperative verbs
# number of nouns
# number of adjectives
# number of adverbs
# number of modal verbs (mainly auxiliary verbs)
# number of singular first and second personal pronouns
# number of plural first personal pronouns
# number of pronouns
# pausality
# number of characters
# average sentence length
# average word length
# percentage of news with speeling errors
# emotiveness
# diversity
