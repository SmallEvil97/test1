import string
words = {}  
for line in open('my_text'):
    b = []
    for word in line.lower().split():
        word = word.strip(string.punctuation)
        words[word] = words.get(word, 0) + 1
        b.append(words[word])
