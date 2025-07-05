# The os module in Python is like a bridge between your code and the operating system—it lets you interact with files,
# folders, environment variables, and system-level tasks in a portable way

# What You Can Do with os module --->

# Task	Function            ||        Example	         ||        Description
# Get current directory	    ||  os.getcwd()	             ||    Returns the current working folder
# Change directory	        ||  os.chdir("path")	     ||    Switches to a different folder
# List files/folders	    ||  os.listdir("path")	     ||    Lists contents of a directory
# Create folder	            ||  os.mkdir("folder")	     ||    Makes a new folder
# Create nested folders     ||	os.makedirs("a/b/c")     ||    Creates all intermediate folders
# Remove file	            ||  os.remove("file.txt")	 ||    Deletes a file
# Remove folder	            ||  os.rmdir("folder")	     ||    Deletes an empty folder
# Rename file/folder	    ||  os.rename("old", "new")	 ||    Renames a file or folder
# Run system command	    ||  os.system("dir")	     ||    Executes a shell command
# Get environment variable	||  os.getenv("PATH")	     ||    Reads system environment variables


import os 

folder_path = r"E:\Jyotsna\Python_Learning\20_Module_in_python\OS_module\Data"

try:
    os.mkdir(folder_path)
    print("Folder created.")
except FileExistsError:
    print("Folder already exists.")


os.makedirs(folder_path, exist_ok=True)

for i in range(5):
    os.mkdir(os.path.join(folder_path, f"Day{i+1}"))




