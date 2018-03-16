import pickle
import nltk
#from nltk.corpus import stopwords
from pathlib import Path
#from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
#import re
#import functools

#nltk.download('punkt')


text_file_name = Path(r"../Texts/Alice.txt")
f2 = text_file_name.name

#sentence_list_file = Path(text_file_name.replace('.txt', '.pickle').replace('.TXT', '.pickle'))
sentence_list_file = Path('.pickles/' + text_file_name.name + '.pickle')
extra_abbreviations = {'dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e'}
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentence_tokenizer._params.abbrev_types.update(extra_abbreviations)


if sentence_list_file.is_file():
    with open(sentence_list_file, 'rb') as text_file:
        sentences=pickle.load(text_file)
        print('LOADING pickle')
else:
    with open(text_file_name, 'rt') as text_file:     ##, encoding='1251'
        sentences = sentence_tokenizer.tokenize(text_file.read(), realign_boundaries=True)
        print(len(sentences))

        with open(sentence_list_file, 'wb') as text_file:
            pickle.dump(sentences, text_file, pickle.HIGHEST_PROTOCOL)


for sentence in sentences:
    if ' rather' in sentence:
        print(sentence)