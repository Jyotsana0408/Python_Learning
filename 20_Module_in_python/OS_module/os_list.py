# The os module in Python is like a bridge between your code and the operating system—it lets you interact with files,
# folders, environment variables, and system-level tasks in a portable way

# What You Can Do with os module --->

# Task	Function            ||        Example	         ||        Description
# List files/folders	    ||  os.listdir("path")	     ||    Lists contents of a directory


import os

base_path = r"E:\Jyotsna\Python_Learning\20_Module_in_python\OS_module\Data"
items = os.listdir(base_path)

for item in items:
    item_path = os.path.join(base_path, item)
    if os.path.isdir(item_path):
        print(f"\nContents of {item}:")
        print(os.listdir(item_path))
    else:
        print(f"\n{item} is a file, not a folder.")

