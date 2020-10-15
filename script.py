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
TEXT_FAKE = 'full_texts/fake/'
TEXT_FAKE_META_INFORMATION = 'full_texts/fake-meta-information/'

# Número de notícias falsas e verdadeiras
# TEXT_NUMBER = 3602 - TODO ajustar
TEXT_NUMBER = 3

def textClean(text):
    '''
    Método responsável por realizar a limpeza do texto passado como parâmetro
    '''    
    # Coloca o texto em lowercase
    text = text.lower()

    # Regex que altera os caracteres para um espaço em branco, exceto os caracteres: 
    # Letras, algumas letras com acentos, números, e o espaço (é tratado mais à frente)
    text = re.sub(r'[^a-z0-9áàâãéèêíïóôõöúçñ ]', r' ', text)

    # Realiza um slip no espaço
    text = text.split()

    # Remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    text = [w for w in text if not w in stopwords]
    text = ' '.join(text)

    return text

def requestMetaInformation(rota, index):
    '''
    Método responsável por buscar o metadata da notícia determinada pelo index
    '''
    req = requests.get(URL + rota + str(index) + '-meta.txt')

    # Valida se o request ocorreu com sucesso
    if req.status_code != requests.codes.ok:
        return None

    # Converte o metadata para array
    metadata = req.text.split('\r\n')
    # Se a quantidade de informações é diferente de 25 ocorreu algum erro
    if len(metadata) != 25:
        raise Exception('Falha ao buscar o metadata da notícia %i' %index)

    return {
        'author': metadata[0],
        'link': metadata[1],
        'category': metadata[2],
        'date_publication': metadata[3],
        'number_tokens': metadata[4],
        'number_words': metadata[5],
        'number_types': metadata[6],
        'number_links': metadata[7],
        'number_words_upper': metadata[8],
        'number_verbs': metadata[9],
        'number_sub_imp_verbs': metadata[10],
        'number_nouns': metadata[11],
        'number_adjectives': metadata[12],
        'number_adverbs': metadata[13],
        'number_modal_verbs': metadata[14],
        'number_singular': metadata[15],
        'number_plural': metadata[16],
        'number_pronouns': metadata[17],
        'pausality': metadata[18],
        'number_characters': metadata[19],
        'average_sentence_length': metadata[20],
        'average_word_length': metadata[21],
        'percent_speeling_errors': metadata[22],
        'emotiveness': metadata[23],
        'diversity': metadata[24],
    }

def generateNews(df, fake_news):
    '''
    Método responsável por gerar as notícias de acordo com os parâmetros fornecidos
    '''
    falhas = 0
    falhasText = []
    # Busca as rotas de acordo com o tipo de notícia
    if fake_news == 0:
        rota = TEXT_FAKE
        rotaMeta = TEXT_FAKE_META_INFORMATION
    else:
        rota = TEXT_TRUE
        rotaMeta = TEXT_TRUE_META_INFORMATION

    for i in range(1, TEXT_NUMBER + 1):
        # Realiza a busca da noticia i, caso resulte algum erro registra uma falha
        req = requests.get(URL + rota + str(i) + '.txt')
        if req.status_code != requests.codes.ok:
            falhas += 1
            falhasText.append(i)
            continue

        # Busca o metadata, caso resulte algum erro registra uma falha
        metadata = requestMetaInformation(rotaMeta, i)
        if metadata == None:
            falhas += 1
            falhasText.append(i)
            continue

        # Insere a notícia no dataframe
        news = {**{'ID': i, 'fake_news': fake_news, 'text': textClean(req.text)}, **metadata}
        df = df.append(news, ignore_index=True)

    return [
        df,
        falhas,
        falhasText,
    ]

try:
    print('Iniciano a criação do CSV')
    inicio = time.time()
    falhas = 0
    falhasTextFake = []
    falhasTextReal = []

    # Criação do DataFrame com as colunas iniciais
    columns = ['ID', 'fake_news', 'text']
    df = pd.DataFrame(columns = columns)

    # Monta o dataframe com as falsas notícias (fake_news = 0)
    result = generateNews(df, 0)
    df = result[0]
    falhas += result[1]
    falhasTextFake += result[2]

    # Monta o dataframe com as verdadeiras notícias (fake_news = 1)
    result = generateNews(df, 1)
    df = result[0]
    falhas += result[1]
    falhasTextReal +=result[2]

    # Realiza a criação do CSV
    df.to_csv('dataset.csv')

    fim = time.time()
    print('CSV criado com sucesso! ')
    print('Número de falhas: %i' %(falhas))
    print('Falhas nas verdadeiras notícias: %a' %falhasTextReal)
    print('Falhas nas falsas notícias: %a' %falhasTextFake)
    print('Tempo de execução: %f minutos' %((fim - inicio) / 60))
except Exception as e:
    print('Falha ao gerar CSV: %s' %str(e))
