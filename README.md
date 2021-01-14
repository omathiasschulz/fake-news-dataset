# fake-news-dataset :floppy_disk:

Dataset com falsas e verdadeiras notícias baseado no [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

## Instalar as dependências

**Obs:** Para rodar os scripts utilize o Python 3.8

Para instalar as dependências do projeto, na pasta raiz do projeto digite:

`pip3 install -r requirements.txt`

## Datasets

Os datasets do projeto estão no diretório `datasets/` e são apresentados abaixo:

### Dataset sem formatação

O dataset do CSV `datasets/unformatted/dataset.csv` é gerado a partir do script `script_01_create.py`

Este CSV possui os textos sem formatação e outras informações que foram buscados do [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus) e convertidas em um CSV

Para criar o Dataset, na pasta raiz do projeto digite:

`python3 script_01_create.py`

**Resultados**

Número de falhas: 4

Falhas nas verdadeiras notícias: [697, 1468]

Falhas nas falsas notícias: [697, 1468]

Tempo aproximado de execução: 82.52 minutos

### Datasets Formatados

Os datasets que estão na pasta `datasets/formatted/` são gerados a partir do script `script_02_format.py`

Os datasets dessa pasta foram criados com base na variável `TEXT_LENGTH`, cada posição da variável gera um dataset, no qual o valor determina que o dataset não deve possuir notícias menores que o valor especificado

*Por exemplo:* O dataset do CSV `dataset_100_palavras.csv` possui apenas textos maiores ou iguais que 100 palavras e o dataset do CSV `dataset_200_palavras.csv` possui apenas textos maiores ou iguais que 200 palavras

Para criar novos CSV's com tamanhos variados ou alterar os existentes apenas é necessário alterar os valores da lista `TEXT_LENGTH`

Para criar os Datasets, na pasta raiz do projeto digite:

`python3 script_02_format.py`

**Etapas de formatação dos textos**

 - Realizado a substituição das letras maiúsculas por minúsculas utilizando o Python;
 - Atualizado os caracteres para um espaço em branco utilizando o Python, exceto os caracteres: Letras, algumas letras com acentos e o espaço (tratado mais à frente);
 - Removido palavras com apenas um carácter por meio da biblioteca Pandas;
 - Removido stopwords por meio da biblioteca Gensim, utilizando o NLTK;
 - Removido múltiplos espaços por um único espaço utilizando o Python;

**Resultados**

**NOVO DATAFRAME**

=> DataFrame sem notícias com menos de 0 palavras

Quantidade de notícias: 7200

Quantidade de notícias verdadeiras (fake_news=0): 3600

Quantidade de notícias falsas (fake_news=1): 3600

Média de palavras das notícias: 372.04

Média de palavras das notícias verdadeiras: 634.94

Média de palavras das notícias falsas: 109.15

**NOVO DATAFRAME**

=> DataFrame sem notícias com menos de 50 palavras

Quantidade de notícias: 6853

Quantidade de notícias verdadeiras (fake_news=0): 3599

Quantidade de notícias falsas (fake_news=1): 3254

Média de palavras das notícias: 389.11

Média de palavras das notícias verdadeiras: 635.11

Média de palavras das notícias falsas: 117.02

**NOVO DATAFRAME**

=> DataFrame sem notícias com menos de 100 palavras

Quantidade de notícias: 5166

Quantidade de notícias verdadeiras (fake_news=0): 3576

Quantidade de notícias falsas (fake_news=1): 1590

Média de palavras das notícias: 491.53

Média de palavras das notícias verdadeiras: 638.67

Média de palavras das notícias falsas: 160.59

**NOVO DATAFRAME**

=> DataFrame sem notícias com menos de 150 palavras

Quantidade de notícias: 4170

Quantidade de notícias verdadeiras (fake_news=0): 3520

Quantidade de notícias falsas (fake_news=1): 650

Média de palavras das notícias: 580.03

Média de palavras das notícias verdadeiras: 646.81

Média de palavras das notícias falsas: 218.39

**NOVO DATAFRAME**

=> DataFrame sem notícias com menos de 200 palavras

Quantidade de notícias: 3699

Quantidade de notícias verdadeiras (fake_news=0): 3432

Quantidade de notícias falsas (fake_news=1): 267

Média de palavras das notícias: 631.98

Média de palavras das notícias verdadeiras: 658.82

Média de palavras das notícias falsas: 286.86

CSVs com o texto formatado criados com sucesso! 

Tempo de execução: 0.07 minutos

## Gráficos

Os gráficos são gerados a partir do script `script_03_info.py` e se encontram na pasta `graphics/`

Os gráficos são gerados baseados nos dados do dataset `dataset.csv`

Para criar os gráficos, na pasta raiz do projeto digite:

`python3 script_03_info.py`

### Gráfico 01 - Word Cloud

O gráfico da imagem `graphics/word_cloud.png` apresenta a nuvem de palavras dos textos

No qual conta a frequência com que cada palavra aparece nos textos e define o tamanho das palavras proporcional à frequência

### Gráfico 02 - Number Words

O gráfico da imagem `graphics/number_words.png` apresenta a quantidade de palavras nos textos

**Resultados**

Tempo aproximado de execução: 0.36 minutos
