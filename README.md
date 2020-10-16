# fake-new-dataset

Brazilian false and true news dataset based on [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

## Install dependencies

To install the dependencies, in the project folder just type

`pip3 install -r requirements.txt`

## Datasets

The project has two datasets the `dataset_unformatted.csv` and the `dataset_formatted.csv`

The `dataset_unformatted.csv` is a CSV generated from the `script_create.csv`, in which the texts are taken from the [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

Number of failures: 4

Failures in the real news: [697, 1468]

Failures in the fake news: [697, 1468]

Runtime: 83.660346 minutes

The `dataset_unformatted.csv` is a CSV with pre-processed text generated from the `script_format.csv`, in which the following steps were performed:

 - Put the text in lower case;
 - Changed the characters to a blank space, except the characters: Letters, some letters with accents, numbers, and the space (treated later)
 - Removed stopwords
 - Removed multiple spaces
 - Set the same size in all texts

The image `number_words.png` shows the number of words in the texts.
