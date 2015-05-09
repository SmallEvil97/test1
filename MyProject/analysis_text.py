import string
words = {} # создаю словарь  
for line in open('my_text'): # даю путь к файлу
    for word in line.lower().split(): # пройдемся по всем элементам в файле  
        word = word.strip(string.punctuation) # исключаю пунктуацию из слов
        words[word] = words.get(word, 0) + 1 # каждый раз когда встречаються одинаковые ключи (или новые), происходит + 1 
for word in sorted(words): # сортируем словарь 
    print("'{0}'".format(word),"found:",words[word]) # вывожу принт
