import time
import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
matplotlib.use('Agg')
# setando um estilo padrão
sns.set_style('darkgrid')


def wordCloud(df):
    """
    Método responsável por montar um gráfico de nuvem de palavras dos textos
    Conta a frequência com que cada palavra aparece nos textos e seta o tamanho das palavras proporcional à frequência

    :param df: Dataframe com os textos
    :type df: Dataframe
    """
    print('Gerando o wordcloud... ')
    # monta uma string com as palavras de todos os textos
    text = ''
    for news in df.text.values:
        text += f" {news}"

    # gera o word cloud
    wordcloud = WordCloud(
        width=3000,
        height=2000,
        background_color='white',
    ).generate(text)

    # gera e salva a figura
    plt.figure(
        figsize=(45, 30),
        facecolor='k',
        edgecolor='k',
    )
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('graphics/word_cloud.png')
    plt.close()


def qtdPalavras(df):
    """
    Método responsável por montar um gráfico com a quantidade de palavras de cada notícia

    :param df: Dataframe com os textos
    :type df: Dataframe
    """
    print('Gerando o gráfico com a quantidade de palavras de cada notícia... ')

    df_words = pd.DataFrame(columns=['quantidade', 'numero_palavras'])
    df_words['numero_palavras'] = df.number_words.value_counts().index.to_numpy()
    df_words['quantidade'] = df.number_words.value_counts().values

    sns_plot = sns.scatterplot(x='numero_palavras', y='quantidade', data=df_words)
    sns_plot.set_title('Quantidade de palavras em cada notícia')
    sns_plot.set_xlabel('Quantidade de palavras por texto')
    sns_plot.set_ylabel('Quantidade de textos')
    sns_plot.figure.savefig('graphics/number_words.png')
    plt.close()


def main():
    print('Iniciando a criação dos gráficos para uma melhor visualização do dataset')
    inicio = time.time()

    # os gráficos são construídos com base no dataset_0_palavras
    # realiza a leitura do CSV
    df = pd.read_csv('datasets/formatted/dataset_0_palavras.csv', index_col=0)

    wordCloud(df)
    qtdPalavras(df)

    fim = time.time()
    print('Gráficos criados com sucesso! ')
    print('Tempo de execução: %.2f minutos' % ((fim - inicio) / 60))


if __name__ == '__main__':
    main()
