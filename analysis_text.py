import string
words = {}  
words_true = {}
for line in open('my_text'):
    for word in line.lower().split():
        word = word.strip(string.punctuation)
        words[word] = words.get(word, 0) + 1
words_true = words.values()
