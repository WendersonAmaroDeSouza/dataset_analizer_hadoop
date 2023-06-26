#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

currently_word = None
currently_sentiment_sum = 0.0
currently_count = 0

for line in sys.stdin:
    word, sentiment, count = line.split('\t')
    sentiment = float(sentiment)
    count = int(count)
    if word == currently_word:
        currently_sentiment_sum += sentiment
        currently_count += count
    else:
        if currently_word:
            currently_sentiment_rate = currently_sentiment_sum / currently_count
            print('{0};{1};{2}'.format(currently_word, currently_count, currently_sentiment_rate))
        currently_word = word
        currently_sentiment_sum = sentiment
        currently_count = count

if currently_word:
    currently_sentiment_rate = currently_sentiment_sum / currently_count
    print('{0};{1};{2}'.format(currently_word, currently_count, currently_sentiment_rate))
