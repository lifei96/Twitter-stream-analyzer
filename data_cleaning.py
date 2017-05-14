# -*- coding: utf-8 -*-

import csv
from nltk.tokenize import RegexpTokenizer


def data_cleaning():
    bad_words = ['unmemorable', 'immemorable', 'forgettable']
    with open('./data/memory_dataset_old.txt', 'r') as f:
        texts = f.read().split('\n')
    with open('./data/memory_dataset.txt', 'w'):
        print 'clear'
    f = open('./data/memory_dataset.txt', 'a')
    for text in texts:
        tokenizer = RegexpTokenizer(r'\w+')
        word_list = tokenizer.tokenize(text)
        flag_del = 0
        for word in bad_words:
            if word in word_list:
                flag_del = 1
                break
        if not flag_del:
            f.write(text + '\n')


if __name__ == '__main__':
    data_cleaning()
