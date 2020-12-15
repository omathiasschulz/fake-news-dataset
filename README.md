# fake-new-dataset :floppy_disk:

Dataset com falsas e verdadeiras notícias baseado no [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

## Instalar as dependências

**Obs:** Para rodar os scripts utilize o Python 3

Para instalar as dependências do projeto, na pasta raiz do projeto digite:

`pip3 install -r requirements.txt`

## Datasets

O projeto possui dois datasets, apresentados abaixo:

### Dataset sem formatação

O dataset `dataset_unformatted.csv` é um CSV gerado a partir do script `script_01_create.py`

Neste CSV, foram buscados em textos e informações do [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus) e convertidas em um CSV

Para criar o Dataset, na pasta raiz do projeto digite:

`python3 script_01_create.py`

**Resultados**

Número de falhas: 4

Falhas nas verdadeiras notícias: [697, 1468]

Falhas nas falsas notícias: [697, 1468]

Tempo de execução: 82.52 minutos

### Dataset Formatado

O dataset `dataset.csv` é um CSV gerado a partir do script `script_02_format.py`

Para criar o Dataset, na pasta raiz do projeto digite:

`python3 script_02_format.py`

**Etapas de formatação dos textos**

 - Realizado a substituição das letras maiúsculas por minúsculas utilizando o Python;
 - Atualizado os caracteres para um espaço em branco utilizando o Python, exceto os caracteres: Letras, algumas letras com acentos e o espaço;
 - Removido palavras com apenas um carácter por meio da biblioteca Pandas;
 - Removido stopwords por meio da biblioteca Gensim, utilizando o NLTK;
 - Removido múltiplos espaços por um único espaço utilizando o Python;
 - Removido textos com menos de 300 palavras;

**Resultados**

*=> DataFrame Original*

Menor número de palavras de um texto: 4 

Maior número de palavras de um texto: 4327 

Quantidade de textos: 7200

Média de palavras dos textos: 372 

*=> DataFrame sem textos com menos de 300 palavras*

Quantidade de textos: 3159

Média de palavras dos textos: 697 

CSV com o texto formatado criado com sucesso! 

Tempo de execução: 0.04 minutos

## Gráficos

Os gráficos são gerados a partir do script `script_03_info.py` e se encontram na pasta `graphics`

Para criar os gráficos, na pasta raiz do projeto digite:

`python3 script_03_info.py`

### Gráfico 01 - Word Cloud

O gráfico da imagem `graphics/word_cloud.png` apresenta a nuvem de palavras dos textos

No qual conta a frequência com que cada palavra aparece nos textos e define o tamanho das palavras proporcional à frequência

### Gráfico 02 - Number Words

O gráfico da imagem `graphics/number_words.png` apresenta a quantidade de palavras nos textos

**Resultados**

Tempo de execução: 0.38 minutos
