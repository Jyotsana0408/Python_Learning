given_word = input("Enter the words: ")

s = given_word.lower()
count = 0
for i in s:
    if i in "aioue":
            count +=1
print(count)