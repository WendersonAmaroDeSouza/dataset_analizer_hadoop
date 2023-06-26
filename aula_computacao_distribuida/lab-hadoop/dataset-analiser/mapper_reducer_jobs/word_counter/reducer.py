#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

currently_word = None
currently_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    
    if word == currently_word:
        currently_count += count
    else:
        if currently_word:
            print('{0};{1}'.format(currently_word, currently_count))
        currently_word = word
        currently_count = count

if currently_word:
    print('{0};{1}'.format(currently_word, currently_count))
