import csv
import pickle
import re
from nltk.corpus import gutenberg

nltk_vocab = []
for fileid in gutenberg.fileids():
    for sent in gutenberg.sents(fileid):
        for word in re.findall(r"[\w]+", ' '.join(sent)):
            word = word.lower()
            nltk_vocab.append(word)
            nltk_vocab = list(set(nltk_vocab))
print(len(nltk_vocab))
vocab_dict = {}
year_list = [2018, 2019, 2020]
except_list = ['(', ')', 'http', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


for year in year_list:
    with open('./output_{}.tsv'.format(year), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            for word in re.findall(r"[\w]+", row[2]):
                word = word.lower()
                flag = 0
                for except_character in except_list:
                    if except_character in word:
                        flag = 1
                        break
                if flag == 0 and word not in nltk_vocab:
                    if word in vocab_dict:
                        vocab_dict[word] += 1
                    else:
                        vocab_dict[word] = 1

### check which words are oov (count == 1)
cnt = 0
for k, v in vocab_dict.items():
    if v == 1:
        cnt += 1
        #print(k)
print(cnt)

with open('abstract_vocab.pickle', 'wb') as handle:
    pickle.dump(vocab_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

