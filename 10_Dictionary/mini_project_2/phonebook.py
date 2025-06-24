phonebook = {
    "Alice": 1234567890,
    "Bob" : 2132435456,
    "Charlie": 9876543210,
    "Dan":9786754375
}

print(phonebook)

for name , num in phonebook.items():
    print(f"{name} is {num}")

phonebook["Raj"] = 9809879787
print(phonebook)