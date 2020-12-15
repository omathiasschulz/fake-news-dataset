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

`python3 script_format.py`

**Etapas de formatação dos textos**

 - Realizado a substituição das letras maiúsculas por minúsculas utilizando o Python;
 - Atualizado os caracteres para um espaço em branco utilizando o Python, exceto os caracteres: Letras, algumas letras com acentos e o espaço;
 - Removido palavras com apenas um carácter por meio da biblioteca Pandas;
 - Removido stopwords por meio da biblioteca Gensim, utilizando o NLTK;
 - Removido múltiplos espaços por um único espaço utilizando o Python;
 - Removido textos com menos de 300 palavras;

**Resultados**

RESULTADO

## Graphics

The image `graphic_word_cloud.png` shows the word cloud graphic of the texts.

Counts the frequency with which each word appears in the texts and sets the size of the words proportional to the frequency.

To generate the cloud graphic it is necessary to run script `script_info.py`, in the project folder type:

`python3 script_info.py`

This script generate the image `graphic_number_words.png` that shows the number of words in the texts.
