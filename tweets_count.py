# -*- coding: utf-8 -*-


def tweets_count():
    count = 0
    file_list = list()
    with open('./tweets_file_list.txt', 'r') as f:
        file_list = f.read().split('\n')
    for file_path in file_list:
        with open(file_path, 'r') as f:
            count += len(f.read().split('\n'))
    return count


if __name__ == '__main__':
    print tweets_count()
