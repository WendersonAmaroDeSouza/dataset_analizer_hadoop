#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
import re

def remove_special_characters(text):
    pattern = r'\b\w+\b'
    words = re.findall(pattern, text)
    
    return ' '.join(words)

for line in sys.stdin:
    line = remove_special_characters(line)
    line = line.strip()
    words = line.split()
    for word in words:
        print('{0}\t{1}'.format(word, 1))
