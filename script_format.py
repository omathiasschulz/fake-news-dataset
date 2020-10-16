import re, string, time
import time
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
# Setando um estilo padrão
sns.set_style('darkgrid')

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
    print('Média de palavras dos textos: %i ' %df['number_words'].mean())

    # Monta o gráfico com a Quantidade de palavras de cada notícia
    df_words = pd.DataFrame(columns = ['quantidade', 'numero_palavras'])
    df_words['numero_palavras'] = df.number_words.value_counts().index.to_numpy()
    df_words['quantidade'] = df.number_words.value_counts().values

    sns_plot = sns.scatterplot(x='numero_palavras', y='quantidade', data=df_words)
    sns_plot.set_title('Quantidade de palavras de cada notícia')
    sns_plot.set_xlabel('Quantidade de palavras')
    sns_plot.set_ylabel('Quantidade de textos')
    sns_plot.figure.savefig('number_words.png')

    # TODO - Setar um número mínimo de palavras para os textos
    # Acima de 200 palavras tem 3706 textos
    # Acima de 300 palavras tem 3174 textos
    # Acima de 400 palavras tem 2600 textos
    print(df[df['number_words'] > 200].count())

    return df

try:
    print('Iniciando a formatação do texto do CSV')
    inicio = time.time()

    # Realiza a leitura do CSV com o texto não formatado
    df = pd.read_csv('dataset_unformatted.csv', index_col=0)

    # Realiza a pré-processamento do texto
    df.text = df.apply(lambda x: textClean(x.text), axis=1)

    # Seta um tamanho fixo de palavras para os textos
    fixLenTexts(df)

    # Realiza a criação do novo CSV
    df.to_csv('dataset_formatted.csv')

    fim = time.time()
    print('CSV com o texto formatado criado com sucesso! ')
    print('Tempo de execução: %f minutos' %((fim - inicio) / 60))
except Exception as e:
    print('Falha ao gerar CSV: %s' %str(e))
