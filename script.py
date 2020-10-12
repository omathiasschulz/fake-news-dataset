import wget

# Repositório Fake.br-Corpus com os textos em TXT: https://github.com/roneysco/Fake.br-Corpus
URL = 'https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/'

TEXT_TRUE = 'full_texts/true/'
TEXT_TRUE_META_INFORMATION = 'full_texts/true-meta-information/'
TEXT_FALSE = 'full_texts/false/'
TEXT_FAKE_META_INFORMATION = 'full_texts/fake-meta-information/'

TEXT_NUMBER = 3602

# # pip install wget
# a = wget.download(URL + TEXT_TRUE + '1.txt')

# print(a)


import base64
import requests

ABC = URL + TEXT_TRUE + '1.txt'
req = requests.get(ABC)
print(req.text)
# if req.status_code == requests.codes.ok:
#     req = req.json()  # the response is a JSON
#     # req is now a dict with keys: name, encoding, url, size ...
#     # and content. But it is encoded with base64.
#     content = base64.decodestring(req['content'])
#     print(content)
# else:
#     print('Content was not found.')
