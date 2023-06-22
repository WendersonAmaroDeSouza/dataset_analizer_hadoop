import sys

currently_word = None
currently_count = 0

for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)
    if word == currently_word:
        currently_count += count
    else:
        if currently_word:
            print('{0};{1}'.format(currently_word, currently_count))
        currently_word = word
        currently_count = count

if currently_word:
    print('{0};{1}'.format(currently_word, currently_count))
