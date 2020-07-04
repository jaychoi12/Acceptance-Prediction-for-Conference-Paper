import os

from datasets.bert_processors.abstract_processor import BertProcessor, InputExample


class ICLRProcessor(BertProcessor):
    NAME = 'ICLR'
    NUM_CLASSES = 2
    IS_MULTILABEL = False

    def get_train_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir,'ICLR', 'train.tsv')), 'train')

    def get_dev_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'ICLR', 'dev.tsv')), 'dev')

    def get_test_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'ICLR', 'test.tsv')), 'test')

    def _create_examples(self, lines, set_type):
        examples = []
        for (i, line) in enumerate(lines):
            if i == 0:
                continue
            guid = "%s-%s" % (set_type, i)
            text_a = line[1]
            if len(line) > 8:
                for itr in range(len(line)-8):
                    text_a += line[-(len(line) - 2) + itr]
            label = line[0]
            
            # 여기서 메타데이터 부분을 조금 손을 봐야겠구만.
#             print (line[2], line[3], line[4], line[5], line[6], line[7])
            meta_data = [float(line[-6]), float(line[-5]), float(line[-4]), float(line[-3]), float(line[-2]), float(line[-1])]
#             meta_data = [line[2], line[3], line[4], line[5], line[6], line[7]]
            
            
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=None, label=label, meta_data=meta_data))
            
            # 여기서 메타데이터 부분을 조금 손을 봐야겠구만.
            # meta_data = line[1][-6:]
            
        return examples
