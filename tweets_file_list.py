# -*- coding: utf-8 -*-

import os
import fnmatch


def tweets_file_list():
    file_list = list()
    for dirpath, dirnames, filenames in os.walk('tweets'):
        for filename in fnmatch.filter(filenames, '*.json'):
            file_list.append(os.path.join(dirpath, filename))
    print '%d files found' % len(file_list)
    return file_list


if __name__ == '__main__':
    with open('./tweets_file_list.txt', 'w') as f:
        f.write('\n'.join(tweets_file_list()))
