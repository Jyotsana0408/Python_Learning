given_str = input("Enter the string: ")

rev_str  = given_str.lower().replace(" ","")

palindrome_string = rev_str[::-1]

if palindrome_string == given_str:
    print("given string is palindrome string!!")
else:
    print("given string is not palindrome string!!")