# File Handling in Python
# all about working with files—creating, reading, writing, and managing them efficiently.

# Opening a File --->
# Use the open() function

# Common modes:

# Mode  Description
# "r"	Read (default)
# "w"	Write (creates or overwrites)
# "a"	Append
# "x"	Create (fails if file exists)
# "b"	Binary mode
# "t"	Text mode (default)

# Reading from a File --->
# f.read()
# Reads the entire file (or a specified number of characters if you pass an argument).
# Returns a single string containing all the file content.
# Useful when you want to process the whole file at once.

# Other methods:
# readline() – reads one line
# readlines() – reads all lines into a list

# write method -->

# Writing to a file in Python is simple and powerful. 
# You can either create a new file or modify an existing one using the open() function with write or append modes.
# "w" mode overwrites the file if it exists.
# Automatically creates the file if it doesn’t.
# "a" mode adds content to the end without deleting existing data.
# writelines() writes a list of strings --> Make sure each string ends with \n if you want line breaks.




# Reading from a file
with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_1.txt", "r") as f:
    text = f.read()
    print(text)

# Writing to a file
with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_2.txt", "w") as f1:
    pass  # file is created and immediately closed


with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_2.txt", "w") as f2:
    f2.write("Hello, Learners!\nThis is your second file.")

with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_3.txt", "w") as f3:
    f3.write("Hello, Learners!\nThis is your third file.")


with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_3.txt", "a") as f3:
    f3.write("\nThis line is added later.")


with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_4.txt", "r") as f:
    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        i += 1
        parts = line.strip().split(".")  # split the line into sentences

        # Print each part if it exists
        for idx, sentence in enumerate(parts):
            print(f"{i} line of poem part {idx+1}: {sentence.strip()}")

        print(f"Original line {i}: {line.strip()}")
    print("--------------------------------------------------------------------------")


with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_4.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())


lines = ["Hello Jyotsna!\n", "This is line 2.\n", "And this is line 3.\n"]

with open(r"E:\Jyotsna\Python_Learning\21_File_Handling\my_file_5.txt", "w") as f:
    f.writelines(lines)

