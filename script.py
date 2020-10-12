import requests
import time
import pandas as pd

# Repositório Fake.br-Corpus com os textos em TXT: https://github.com/roneysco/Fake.br-Corpus
URL = 'https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/'

TEXT_TRUE = 'full_texts/true/'
TEXT_TRUE_META_INFORMATION = 'full_texts/true-meta-information/'
TEXT_FALSE = 'full_texts/false/'
TEXT_FAKE_META_INFORMATION = 'full_texts/fake-meta-information/'

# Número de notícias falsas e verdadeiras
TEXT_NUMBER = 3602
TEXT_NUMBER = 3

# Criação da DataFrame
columns = ['ID', 'fake_news', 'text']
# fake_news => 1 = True, 0 = False
df = pd.DataFrame(columns = columns)

print('Iniciano a criação do CSV')

inicio = time.time()
falhas = 0
falhasText = []

# Gera as notícias verdadeiras
for i in range(1, TEXT_NUMBER + 1):
    print('Texto: %i' %(i))
    req = requests.get(URL + TEXT_TRUE + str(i) + '.txt')
    if req.status_code == requests.codes.ok:
        df = df.append({'ID': i, 'fake_news': 0, 'text': req.text}, ignore_index=True)
    else:
        falhas += 1
        falhasText.append(i)

# Gera as notícias falsas
for i in range(1, TEXT_NUMBER + 1):
    print('Texto: %i' %(i))
    req = requests.get(URL + TEXT_FALSE + str(i) + '.txt')
    if req.status_code == requests.codes.ok:
        df = df.append({'ID': i, 'fake_news': 1, 'text': req.text}, ignore_index=True)
    else:
        falhas += 1
        falhasText.append(i)
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
