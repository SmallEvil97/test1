import string
words = {} 
for line in open('my_text'): 
    for word in line.lower().split():  
        word = word.strip(string.punctuation)
        words[word] = words.get(word, 0) + 1  
for word in sorted(words): 
    print("'{0}'".format(word),"found:",words[word]) 