import re
import time
import nltk
import pandas as pd

nltk.download('stopwords')

# tamanho mínimo que os textos podem possuir no montagem do CSV de textos formatados
TEXT_LENGTH_DEFAULT = 300
TEXT_LENGTH_FOR_TESTS = [100, 200]


def textClean(text):
    """
    Método responsável por realizar a limpeza do texto passado como parâmetro

    :param text: Texto que será formatado
    :type text: str
    :return: Retorna o texto formatado
    :rtype: str
    """
    # coloca o texto em lowercase
    text = text.lower()

    # regex que altera os caracteres para um espaço em branco, exceto os caracteres:
    # letras, algumas letras com acentos, números, e o espaço (é tratado mais à frente)
    text = re.sub(r'[^a-z0-9áàâãéèêíïóôõöúçñ ]', r' ', text)

    # realiza um slip no espaço
    text = text.split()

    # remoção de palavras com apenas uma letra
    text = [w for w in text if len(w) > 1]

    # remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    text = [w for w in text if w not in stopwords]
    text = ' '.join(text)

    return text


def infoDFAntigo(df):
    """
    Método responsável por apresentar o df sem filtrar pelo tamanho dos textos
    :param df: Dataframe para apresentar
    :type df: Dataframe
    """
    # cria uma nova coluna com o número de palavras de cada texto
    df['number_words'] = df.apply(lambda row: len(row.text.split()), axis=1)

    # apresenta um esboço do CSV
    print(df.head())
    print('Menor número de palavras de um texto: %i ' % df['number_words'].min())
    print('Maior número de palavras de um texto: %i ' % df['number_words'].max())

    print('\n=> DataFrame sem tamanho mínino de palavras nos textos:')
    print('Quantidade de textos: %i' % len(df))
    print('Média de palavras dos textos: %i ' % df['number_words'].mean())


def fixLenTexts(df, text_length):
    """
    Método responsável por setar um tamanho fixo de palavras para os textos

    :param df: Dataframe para ajustar o tamanho
    :type df: Dataframe
    :param text_length: Tamanho mínimo que os textos podem ter
    :type text_length: int
    :return: Retorna o Dataframe
    :rtype: Dataframe
    """
    # removido textos com menos de TEXT_LENGTH palavras
    df = df[df['number_words'] >= text_length]
    # reajusta os indexs
    df = df.reset_index(drop=True)

    print('\nNOVO DATAFRAME')
    print('=> DataFrame sem textos com menos de %i palavras' % text_length)
    print('Quantidade de textos: %i' % len(df))
    print('Média de palavras dos textos: %i \n' % df['number_words'].mean())

    return df


def main():
    """
    Método main do script
    """
    print('Iniciando a formatação do texto do CSV')
    inicio = time.time()

    # realiza a leitura do CSV com o texto não formatado
    df = pd.read_csv('dataset_unformatted.csv', index_col=0)

    # realiza a pré-processamento do texto
    print('Realizando a limpeza dos textos... ')
    df.text = df.apply(lambda x: textClean(x.text), axis=1)

    # apresenta o df
    infoDFAntigo(df)

    # seta um tamanho fixo de palavras para os textos
    print('Ajustando o tamanho dos textos... ')
    # cria o dataset.csv com o tamanho default para os textos
    df_length_default = fixLenTexts(df, TEXT_LENGTH_DEFAULT)
    # realiza a criação do novo CSV
    df_length_default.to_csv('dataset.csv')

    # cria outros CSV's com os tamanhos para teste
    for length in TEXT_LENGTH_FOR_TESTS:
        df_test = fixLenTexts(df, length)

        # realiza a criação do novo CSV para teste
        df_test.to_csv('dataset_' + str(length) + '_palavras.csv')

    fim = time.time()
    print('CSVs com o texto formatado criados com sucesso! ')
    print('Tempo de execução: %.2f minutos' % ((fim - inicio) / 60))


if __name__ == '__main__':
    main()
