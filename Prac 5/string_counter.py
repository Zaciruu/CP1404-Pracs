words_to_count = []
text = input("Please enter some text")
word_list = text.strip().split(",")
for word in word_list:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1
print(text)

