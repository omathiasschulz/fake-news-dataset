import requests
import time
import pandas as pd

# repositório Fake.br-Corpus com os textos em TXT: https://github.com/roneysco/Fake.br-Corpus
URL = 'https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/'
# rotas para as notícias e os metadatas
TEXT_TRUE = 'full_texts/true/'
TEXT_TRUE_META_INFORMATION = 'full_texts/true-meta-information/'
TEXT_FAKE = 'full_texts/fake/'
TEXT_FAKE_META_INFORMATION = 'full_texts/fake-meta-information/'
# número de notícias falsas e verdadeiras
TEXT_NUMBER = 3602


def requestMetaInformation(rota, index):
    """
    Método responsável por buscar o metadata da notícia determinada pelo index

    :param rota: Rota para buscar o metadata da notícia
    :type rota: str
    :param index: ID da notícia
    :type index: int
    :return: Retorna o metadata da notícia
    :rtype: dict
    """
    req = requests.get(URL + rota + str(index) + '-meta.txt')

    # valida se o request ocorreu com sucesso
    if req.status_code != requests.codes.ok:
        return None

    # converte o metadata para array
    metadata = req.text.split('\r\n')
    # se a quantidade de informações é diferente de 25 ocorreu algum erro
    if len(metadata) != 25:
        raise Exception('Falha ao buscar o metadata da notícia %i' % index)

    return {
        'author': metadata[0],
        'link': metadata[1],
        'category': metadata[2],
        'date_publication': metadata[3],
        'average_word_length': metadata[21],
        'percent_speeling_errors': metadata[22],
    }


def generateNews(df, fake_news):
    """
    Método responsável por gerar as notícias de acordo com os parâmetros fornecidos

    :param df: Dataframe no qual será armazenado as notícias
    :type df: Dataframe
    :param fake_news: Determina se as notícias para buscar serão fake ou não
    :type fake_news: int
    :return: Retorna o Dataframe e os casos que resultaram falhas para buscar
    :rtype: list
    """
    falhas = 0
    falhas_text = []
    # busca as rotas de acordo com o tipo de notícia
    if fake_news == 0:
        rota = TEXT_TRUE
        rota_meta = TEXT_TRUE_META_INFORMATION
    else:
        rota = TEXT_FAKE
        rota_meta = TEXT_FAKE_META_INFORMATION

    for i in range(1, TEXT_NUMBER + 1):
        # realiza a busca da noticia i, caso resulte algum erro registra uma falha
        req = requests.get(URL + rota + str(i) + '.txt')
        if req.status_code != requests.codes.ok:
            falhas += 1
            falhas_text.append(i)
            continue

        # busca o metadata, caso resulte algum erro registra uma falha
        metadata = requestMetaInformation(rota_meta, i)
        if metadata is None:
            falhas += 1
            falhas_text.append(i)
            continue

        print('Tipo %s - Notícia: %i' % (fake_news, i))
        # remove múltiplos espaços
        text = ' '.join(req.text.split())
        # insere a notícia no dataframe
        news = {**{'ID': i, 'fake_news': fake_news, 'text': text}, **metadata}
        df = df.append(news, ignore_index=True)

    return [
        df,
        falhas,
        falhas_text,
    ]


def main():
    """
    Método main do script
    """
    print('Iniciando a criação do CSV')
    inicio = time.time()
    falhas = 0
    falhas_text_fake = []
    falhas_text_real = []

    # criação do DataFrame com as colunas iniciais
    columns = ['ID', 'fake_news', 'text']
    df = pd.DataFrame(columns=columns)

    # monta o dataframe com as falsas notícias (fake_news = 1)
    result = generateNews(df, 1)
    df = result[0]
    falhas += result[1]
    falhas_text_fake += result[2]

    # monta o dataframe com as verdadeiras notícias (fake_news = 0)
    result = generateNews(df, 0)
    df = result[0]
    falhas += result[1]
    falhas_text_real += result[2]

    # realiza a conversão de colunas com números para o tipo numérico
    columns_to_convert = ['ID', 'fake_news', 'average_word_length', 'percent_speeling_errors']
    df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric)

    # realiza a criação do CSV
    df.to_csv('dataset_unformatted.csv')

    fim = time.time()
    print('CSV criado com sucesso! ')
    print('Número de falhas: %i' % falhas)
    print('Falhas nas verdadeiras notícias: %a' % falhas_text_real)
    print('Falhas nas falsas notícias: %a' % falhas_text_fake)
    print('Tempo de execução: %.2f minutos' % ((fim - inicio) / 60))


if __name__ == '__main__':
    main()
