# count the words in a sentence

line = "This line is test. and ye this line is test "

cleaned_text = line.replace(".","").lower()

words = cleaned_text.split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

for word, count in word_freq.items():
    print(f"{word} : {count}")