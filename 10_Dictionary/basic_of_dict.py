#  ordered collection of data items from pythom 3.7 version
#  key-value pair


dict = {
    "name" : "harry",
    "age" : 27,
    "class" : 12
}

print(dict)

# access values from dictionary
print(dict["name"]) #if key is not present it will throw an error
print(dict.get("name")) # if key is not present , it will return None

# access multiple keys

print(dict.keys())


# access multiiple values

print(dict.values())

for val in dict.keys():
    print(dict[val]) #ordered


# accesssing key-value pairs
print(dict.items())

for key, value in dict.items():
    print(f"the value corresponding to {key} is {value}")