import requests, time
import pandas as pd

# Repositório Fake.br-Corpus com os textos em TXT: https://github.com/roneysco/Fake.br-Corpus
URL = 'https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/'

TEXT_TRUE = 'full_texts/true/'
TEXT_TRUE_META_INFORMATION = 'full_texts/true-meta-information/'
TEXT_FAKE = 'full_texts/fake/'
TEXT_FAKE_META_INFORMATION = 'full_texts/fake-meta-information/'

# Número de notícias falsas e verdadeiras
TEXT_NUMBER = 3602

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
        'average_word_length': metadata[21],
        'percent_speeling_errors': metadata[22],
    }

def generateNews(df, fake_news):
    '''
    Método responsável por gerar as notícias de acordo com os parâmetros fornecidos
    '''
    falhas = 0
    falhasText = []
    # Busca as rotas de acordo com o tipo de notícia
    if fake_news == 0:
        rota = TEXT_TRUE
        rotaMeta = TEXT_TRUE_META_INFORMATION
    else:
        rota = TEXT_FAKE
        rotaMeta = TEXT_FAKE_META_INFORMATION

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

        print('Tipo %s - Notícia: %i' %(fake_news, i))
        # Remove múltiplos espaços
        text = ' '.join(req.text.split())
        # Insere a notícia no dataframe
        news = {**{'ID': i, 'fake_news': fake_news, 'text': text}, **metadata}
        df = df.append(news, ignore_index=True)

    return [
        df,
        falhas,
        falhasText,
    ]

try:
    print('Iniciando a criação do CSV')
    inicio = time.time()
    falhas = 0
    falhasTextFake = []
    falhasTextReal = []

    # Criação do DataFrame com as colunas iniciais
    columns = ['ID', 'fake_news', 'text']
    df = pd.DataFrame(columns = columns)

    # Monta o dataframe com as falsas notícias (fake_news = 1)
    result = generateNews(df, 1)
    df = result[0]
    falhas += result[1]
    falhasTextFake += result[2]

    # Monta o dataframe com as verdadeiras notícias (fake_news = 0)
    result = generateNews(df, 0)
    df = result[0]
    falhas += result[1]
    falhasTextReal +=result[2]

    # Realiza a conversão de colunas com números para o tipo numérico
    df[['ID', 'fake_news', 'average_word_length', 'percent_speeling_errors']] = df[['ID', 'fake_news', 'average_word_length', 'percent_speeling_errors']].apply(pd.to_numeric)

    # Realiza a criação do CSV
    df.to_csv('dataset_unformatted.csv')

    fim = time.time()
    print('CSV criado com sucesso! ')
    print('Número de falhas: %i' %(falhas))
    print('Falhas nas verdadeiras notícias: %a' %falhasTextReal)
    print('Falhas nas falsas notícias: %a' %falhasTextFake)
    print('Tempo de execução: %f minutos' %((fim - inicio) / 60))
except Exception as e:
    print('Falha ao gerar CSV: %s' %str(e))
