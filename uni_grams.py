# -*- coding: utf-8 -*-

import csv
from nltk.tokenize import RegexpTokenizer


def uni_grams():
    num_times = dict()
    num_reviews = dict()
    with open('./data/memory_dataset.txt', 'r') as f:
        texts = f.read().split('\n')
    cnt = 0
    tot = len(texts)
    for text in texts:
        tokenizer = RegexpTokenizer(r'\w+')
        word_list = tokenizer.tokenize(text)
        word_dict = dict()
        for word in word_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        for word in word_dict.keys():
            if word in num_times:
                num_times[word] += word_dict[word]
            else:
                num_times[word] = word_dict[word]
            if word in num_reviews:
                num_reviews[word] += 1
            else:
                num_reviews[word] = 1
        cnt += 1
        print '%d/%d' % (cnt, tot)
    num_times = sorted(num_times.items(), key=lambda x: x[1], reverse=True)
    num_reviews = sorted(num_reviews.items(), key=lambda x: x[1], reverse=True)
    with open('./data/uni_grams_count_times.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['word', 'count'])
        writer.writeheader()
        for word, count in num_times:
            writer.writerow({'word': word, 'count': count})
    with open('./data/uni_grams_count_reviews.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['word', 'count'])
        writer.writeheader()
        for word, count in num_reviews:
            writer.writerow({'word': word, 'count': count})


if __name__ == '__main__':
    uni_grams()
