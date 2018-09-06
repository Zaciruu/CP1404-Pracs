unique_words = {}
text = input("Words: ")
words = text.split()
for word in words:
    frequency_of_words = unique_words.get(word, 0)
    unique_words[word] = frequency_of_words + 1
words = list(unique_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))
