given_string = input("Enter the string:")

print(len(given_string))

lower_str = given_string.lower()
print(lower_str)

upper_str = lower_str.upper()
print(upper_str)

given_string2 = input("Enter string for stripped string: ")
strpped_str = given_string2.strip()
print(strpped_str)

titled_str = given_string.title()
print(titled_str)

captialized_str = given_string.capitalize()
print(captialized_str)

given_string3 = "Hello Hello Hello, How are you"

print(given_string3.find("Hello"))
print(given_string3.index("you"))
print(given_string3.count("Hello"))

replaced_string  = given_string3.replace("Hello","Beautiful")
print(replaced_string)
