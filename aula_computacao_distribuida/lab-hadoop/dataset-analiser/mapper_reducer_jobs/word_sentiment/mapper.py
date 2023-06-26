#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
from textblob import TextBlob
import re

def remove_special_characters(text):
    pattern = r'\b\w+\b'
    words = re.findall(pattern, text)
    
    return ' '.join(words)

for line in sys.stdin:
    phrases = line.split('.')
    for phrase in phrases:
        sentiment = TextBlob(phrase).sentiment.polarity

        line = remove_special_characters(line)
        line = line.strip()
        words = phrase.split()
        for word in words:
            print('{0}\t{1}\t{2}'.format(word, sentiment, 1))
