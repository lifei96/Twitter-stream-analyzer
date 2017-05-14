# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
import json


def create_memory_dataset():
    stopword_list = stopwords.words('english')
    keyword_list = ['memorable', 'unforgettable', 'indelible']
    with open('./tweets_file_list.txt', 'r') as f:
        file_list = f.read().split('\n')
    cnt_file = 0
    tot_file = len(file_list)
    sum_tweets = 0
    with open('./data/memory_dataset.txt', 'w') as f:
        print '-----clear'
    for file_path in file_list:
        with open(file_path, 'r') as f:
            tweets_list = f.read().split('\n')
        cnt_tweets = 0
        tot_tweets = len(tweets_list)
        for tweet_data in tweets_list:
            try:
                tweet = json.loads(tweet_data)
                if 'text' not in tweet:
                    continue
                text = ' '.join(word_tokenize(tweet['text'].lower()))
                flag_add = 0
                flag_remove = 0
                for keyword in keyword_list:
                    if 'not ' + keyword in text:
                        flag_remove = 1
                        break
                    if keyword in text:
                        flag_add = 1
                tokenizer = RegexpTokenizer(r'\w+')
                if flag_remove == 0 and flag_add == 1:
                    word_list = tokenizer.tokenize(text)
                    text = ' '.join([word for word in word_list if word not in stopword_list])
                    with open('./data/memory_dataset.txt', 'a') as f:
                        f.write(text + '\n')
                cnt_tweets += 1
                sum_tweets += 1
                print 'tweets: %d/%d' % (cnt_tweets, tot_tweets)
            except:
                continue
        cnt_file += 1
        print 'files: %d/%d' % (cnt_file, tot_file)
    print sum_tweets


if __name__ == '__main__':
    create_memory_dataset()
