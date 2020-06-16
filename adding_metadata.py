import csv

with open('./output_2018.tsv','r') as f_in:
    with open ('output_with_metadata_2018.tsv','w') as f_out:
        writer = csv.writer(f_out, delimiter='\t')
        reader = csv.reader(f_in, delimiter='\t')
        
        header = next(reader)
        metadata_list = ['title_length','abstract_length','num_of_keywords','is_code', 'tldr_length','abstract_word_mean']
        header.extend(metadata_list)
        writer.writerow(header)
        #['title', 'accept', 'abstract', 'tldr', 'keyword', 'code']
        for row in reader:
            addition = [None]*6
            row[0] = ' '.join(row[0].split()) #reprocessing the title..since it has a line break 
            addition[0] = len(row[0].split()) #title length
            addition[1] = len(row[2].split()) #abstract length
            addition[2] = len(row[4].split(',')) if row[4] != '' else 0 #num of keyword
            addition[3] = 1 if row[5] != '' else 0 #is code
            addition[4] = len(row[3].split()) if row[3] != '' else 0 #tldr length
            addition[5] = sum(len(word) for word in row[2].split()) / len(row[2].split())
            row.extend(addition)
            writer.writerow(row)
            