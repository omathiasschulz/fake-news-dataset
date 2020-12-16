import re, time, nltk
import pandas as pd
nltk.download('stopwords')

# Tamanho mínimo que os textos podem possuir no montagem do CSV de textos formatados
TEXT_LENGTH = 300

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

    # Remoção de palavras com apenas uma letra
    text = [w for w in text if len(w) > 1]

    # Remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    text = [w for w in text if not w in stopwords]
    text = ' '.join(text)

    return text

def fixLenTexts(df):
    '''
    Método responsável por setar um tamanho fixo de palavras para os textos
    '''
    # Cria uma nova coluna com o número de palavras de cada texto
    df['number_words'] = df.apply(lambda row: len(row.text.split()), axis=1)

    # Apresenta um esboço do CSV
    print(df.head())
    print('Menor número de palavras de um texto: %i ' %df['number_words'].min())
    print('Maior número de palavras de um texto: %i ' %df['number_words'].max())

    print('\n=> DataFrame sem tamanho mínino de palavras nos textos:')
    print('Quantidade de textos: %i' %len(df))
    print('Média de palavras dos textos: %i ' %df['number_words'].mean())

    # Removido textos com menos de 300 palavras
    df = df[df['number_words'] >= TEXT_LENGTH]

    print('\nNOVO DATAFRAME')
    print('=> DataFrame sem textos com menos de %i palavras' %TEXT_LENGTH)
    print('Quantidade de textos: %i' %len(df))
    print('Média de palavras dos textos: %i \n' %df['number_words'].mean())

    return df

try:
    print('Iniciando a formatação do texto do CSV')
    inicio = time.time()

    # Realiza a leitura do CSV com o texto não formatado
    df = pd.read_csv('dataset_unformatted.csv', index_col=0)

    # Realiza a pré-processamento do texto
    df.text = df.apply(lambda x: textClean(x.text), axis=1)

    # Seta um tamanho fixo de palavras para os textos
    df = fixLenTexts(df)

    # Realiza a criação do novo CSV
    df.to_csv('dataset.csv')

    fim = time.time()
    print('CSV com o texto formatado criado com sucesso! ')
    print('Tempo de execução: %f minutos' %((fim - inicio) / 60))
except Exception as e:
    print('Falha ao gerar CSV: %s' %str(e))
