import csv
import pickle

vocab_dict = {}
year_list = [2018, 2019, 2020]

for year in year_list:
    with open('./output_{}.tsv'.format(year), 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            for word in row[2].split():
                if word in vocab_dict:
                    vocab_dict[word] += 1
                else:
                    vocab_dict[word] = 1

### check which words are oov (count == 1)
for k, v in vocab_dict.items():
    if v == 1:
        print(k)

with open('abstract_vocab.pickle', 'wb') as handle:
    pickle.dump(vocab_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

