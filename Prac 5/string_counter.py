unique_words = {}
text = input("Words: ")
words = text.split()
for word in words:
    frequency = unique_words.get(word, 0)
    # Note: this is the "Look Before You Leap" (LBYL) pattern
    # we could use the "Easier to Ask Forgiveness" pattern using exceptions
    unique_words[word] = frequency + 1

words = list(unique_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))
