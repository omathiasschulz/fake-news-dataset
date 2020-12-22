# fake-news-dataset :floppy_disk:

Dataset com falsas e verdadeiras notícias baseado no [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

## Instalar as dependências

**Obs:** Para rodar os scripts utilize o Python 3.8

Para instalar as dependências do projeto, na pasta raiz do projeto digite:

`pip3 install -r requirements.txt`

## Datasets

Os datasets do projeto são apresentados abaixo:

### Dataset sem formatação

O dataset do CSV `dataset_unformatted.csv` é gerado a partir do script `script_01_create.py`

Neste CSV, foram buscados os textos e informações do [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus) e convertidas em um CSV

Para criar o Dataset, na pasta raiz do projeto digite:

`python3 script_01_create.py`

**Resultados**

Número de falhas: 4

Falhas nas verdadeiras notícias: [697, 1468]

Falhas nas falsas notícias: [697, 1468]

Tempo aproximado de execução: 82.52 minutos

### Datasets Formatados

O dataset do CSV `dataset.csv` é gerado a partir do script `script_02_format.py`

Por padrão, o dataset do CSV`dataset.csv` possui apenas textos maiores que 300 palavras, baseado na variável `TEXT_LENGTH_DEFAULT`

Os datasets dos CSV's `dataset_100_palavras.csv` e `dataset_200_palavras.csv` foram criados para teste e possuem o tamanho baseado na variável `TEXT_LENGTH_FOR_TESTS`  

Dessa forma, o dataset do CSV `dataset_100_palavras.csv` possui apenas textos maiores que 100 palavras e o dataset do CSV `dataset_200_palavras.csv` possui apenas textos maiores que 200 palavras

Para criar novos CSV's com tamanhos variados ou alterar os existentes apenas é necessário alterar os valores da lista `TEXT_LENGTH_FOR_TESTS`

Para criar os Datasets, na pasta raiz do projeto digite:

`python3 script_02_format.py`

**Etapas de formatação dos textos**

 - Realizado a substituição das letras maiúsculas por minúsculas utilizando o Python;
 - Atualizado os caracteres para um espaço em branco utilizando o Python, exceto os caracteres: Letras, algumas letras com acentos e o espaço (tratado mais à frente);
 - Removido palavras com apenas um carácter por meio da biblioteca Pandas;
 - Removido stopwords por meio da biblioteca Gensim, utilizando o NLTK;
 - Removido múltiplos espaços por um único espaço utilizando o Python;

**Resultados**

**=> DataFrame Original**

Menor número de palavras de um texto: 4 

Maior número de palavras de um texto: 4327 

Quantidade de textos: 7200

Média de palavras dos textos: 372 

**=> DataFrame sem textos com menos de 300 palavras**

Quantidade de textos: 3159

Média de palavras dos textos: 697 

**=> DataFrame sem textos com menos de 200 palavras**

Quantidade de textos: 3699

Média de palavras dos textos: 631 

**=> DataFrame sem textos com menos de 100 palavras**

Quantidade de textos: 5166

Média de palavras dos textos: 491 

Tempo aproximado de execução: 0.05 minutos

## Gráficos

Os gráficos são gerados a partir do script `script_03_info.py` e se encontram na pasta `graphics`

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
