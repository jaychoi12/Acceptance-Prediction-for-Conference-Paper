import os

from datasets.bow_processors.abstract_processor import BagOfWordsProcessor, InputExample


class IMDBProcessor(BagOfWordsProcessor):
    NAME = 'Yelp'
    NUM_CLASSES = 2
#     VOCAB_SIZE = 395495
    VOCAB_SIZE = 1
    IS_MULTILABEL = False

    def get_train_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'Yelp', 'train.tsv')), 'train')

    def get_dev_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'Yelp', 'dev.tsv')), 'dev')

    def get_test_examples(self, data_dir):
        return self._create_examples(
            self._read_tsv(os.path.join(data_dir, 'Yelp', 'test.tsv')), 'test')

    def _create_examples(self, lines, set_type):
        examples = []
        for (i, line) in enumerate(lines):
            guid = '%s-%s' % (set_type, i)
            examples.append(InputExample(guid=guid, text=line[1], label=line[0]))
        return examples