import csv
import pickle
import sys
import re

with open('abstract_vocab.pickle', 'rb') as handle:
    vocab_dict = pickle.load(handle)

with open('./output_2020.tsv','r') as f_in:
    with open ('output_with_metadata_2020.tsv','w') as f_out:
        writer = csv.writer(f_out, delimiter='\t')
        reader = csv.reader(f_in, delimiter='\t')
        
        header = next(reader)
        metadata_list = ['title_length','abstract_length','num_of_keywords','is_code', 'tldr_length', 'num_oov']
        header.extend(metadata_list)
        writer.writerow(header)
        #['title', 'accept', 'abstract', 'tldr', 'keyword', 'code']
        avg_acc = 0
        cnt_acc = 0
        avg_rej = 0
        cnt_rej = 0
        for row in reader:
            addition = [None]*6
            row[0] = ' '.join(row[0].split()) #reprocessing the title..since it has a line break 
            addition[0] = len(row[0].split()) #title length
            if row[1] == '1':
                cnt_acc += 1
            else:
                cnt_rej += 1
            addition[1] = len(row[2].split()) #abstract length
            addition[2] = len(row[4].split(',')) if row[4] != '' else 0 #num of keyword
            addition[3] = 1 if row[5] != '' else 0 #is code
            addition[4] = len(row[3].split()) if row[3] != '' else 0 #tldr length
            addition[5] = 0 #num of oov
            for word in re.findall(r"[\w]+", row[2]):
                word = word.lower()
                if word in vocab_dict and vocab_dict[word] == 1:
                    addition[5] += 1
                    if row[1] == '1':
                        avg_acc += 1
                    else:
                        avg_rej += 1

            row.extend(addition)
            writer.writerow(row)
        print(avg_acc / cnt_acc)
        print(avg_rej / cnt_rej)
