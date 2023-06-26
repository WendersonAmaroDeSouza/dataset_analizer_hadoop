#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
import subprocess

def install_dependencies():
    command = 'pip3 install textblob'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode != 0:
        raise Exception(f'Erro: {error.decode()}')

def import_dependencies():
    from textblob import TextBlob
    import re

# Install dependences before import libs
try:
    import_dependencies()
except:
    install_dependencies()
    import_dependencies()

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
