# fake-new-dataset

Brazilian false and true news dataset based on [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

## Install dependencies

To install the dependencies in the project folder just type

`pip3 install -r requirements.txt`

## Datasets

The project has two datasets the `dataset_unformatted.csv` and the `dataset_formatted.csv`

### Unformatted Dataset

The `dataset_unformatted.csv` is a CSV generated from the `script_create.py`

To create the dataset, in the project folder type:

`python3 script_create.py`

In which the texts are taken from the [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus)

**Time to generate CSV:**

Number of failures: 4

Failures in the real news: [697, 1468]

Failures in the fake news: [697, 1468]

Runtime: 83.66 minutes

### Formatted Dataset

The `dataset_formatted.csv` is a CSV with pre-processed text generated from the `script_format.py`

To create the dataset, in the project folder type:

`python3 script_format.py`

In which the following steps were performed:

 - Put the text in lower case;
 - Changed the characters to a blank space, except the characters: Letters, some letters with accents, numbers, and the space (treated later)
 - Removed words with just one letter
 - Removed stopwords
 - Removed multiple spaces
 - Removed texts with less than 300 words

**Time to generate CSV:**

Runtime: 0.04 minutes

This script generate the image `graphic_number_words.png` that shows the number of words in the texts.

## Graphics

The image `graphic_word_cloud.png` shows the word cloud graphic of the texts.

Counts the frequency with which each word appears in the texts and sets the size of the words proportional to the frequency.

To generate the cloud graphic it is necessary to run script `script_info.py`, in the project folder type:

`python3 script_info.py`
