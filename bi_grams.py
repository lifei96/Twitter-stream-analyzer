# -*- coding: utf-8 -*-

import nltk
from nltk.collocations import *
from nltk.tokenize import word_tokenize
import csv


def bi_grams():
    keyword_list = ['memorable', 'unforgettable', 'indelible']
    with open('./data/memory_dataset.txt', 'r') as f:
        text = f.read().split()
    print len(text)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(text, window_size=5)
    bigrams = finder.score_ngrams(bigram_measures.pmi)
    f1 = open('./data/bi_grams_with_memory_words.csv', 'w')
    f2 = open('./data/bi_grams_without_memory_words.csv', 'w')
    writer1 = csv.DictWriter(f1, fieldnames=['bi_gram', 'pmi'])
    writer1.writeheader()
    writer2 = csv.DictWriter(f2, fieldnames=['bi_gram', 'pmi'])
    writer2.writeheader()
    for bi_gram, pmi in bigrams:
        if bi_gram[0] in keyword_list or bi_gram[1] in keyword_list:
            writer1.writerow({'bi_gram': bi_gram, 'pmi': pmi})
        else:
            writer2.writerow({'bi_gram': bi_gram, 'pmi': pmi})


if __name__ == '__main__':
    bi_grams()
