import time
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def wordCloud(df):
    '''
    Método responsável por montar um gráfico de nuvem de palavras dos textos
    Conta a frequência com que cada palavra aparece no texto e seta o tamanho das palavras proporcional à frequência
    '''
    # Monta uma string com as palavras de todos os textos
    text = ''
    for news in df.text.values:
        text += f" {news}"

    # Gera o word cloud
    wordcloud = WordCloud(
        width = 3000,
        height = 2000,
        background_color = 'white',
    ).generate(text)

    # Gera e salva a figura
    fig = plt.figure(
        figsize = (45, 30),
        facecolor = 'k',
        edgecolor = 'k',
    )
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('word_cloud.png')

try:
    print('Iniciando a criação dos gráficos para uma melhor visualização do dataset')
    inicio = time.time()

    # Realiza a leitura do CSV
    df = pd.read_csv('dataset_formatted.csv', index_col=0)

    print('Gerando o word cloud... ')
    wordCloud(df)

    fim = time.time()
    print('Gráficos criados com sucesso! ')
    print('Tempo de execução: %f minutos' %((fim - inicio) / 60))
except Exception as e:
    print('Falha ao gerar gráficos: %s' %str(e))