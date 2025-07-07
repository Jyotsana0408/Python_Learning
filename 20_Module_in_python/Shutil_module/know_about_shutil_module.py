# The shutil module --->
# stands for “shell utilities” 
# provides a powerful set of high-level functions for file and directory operations—like copying, moving, deleting, and archiving.

# Key Functions in shutil
# Function	                                        Purpose
# shutil.copy(src, dst)	                            Copies a file to another location (preserves permissions)
# shutil.copy2(src, dst)	                        Like copy(), but also preserves metadata (timestamps)
# shutil.move(src, dst)	                            Moves a file or directory to a new location
# shutil.rmtree(path)	                            Deletes an entire directory tree
# shutil.make_archive(base_name, format, root_dir)	Creates a zip/tar archive
# shutil.unpack_archive(filename, extract_dir)	    Extracts an archive


# Why Use shutil? ---?
# Simplifies file management tasks.
# Cross-platform compatible.
# Great for automation scripts, CLI tools, and backup utilities.


import shutil
import os

# shutil.copy("main.py", "main2.py")

# shutil.move("tutorial/tutorial.txt", " tutorial.txt")

# While shutil is great for directories, it doesn't directly support deleting individual files.
#  For that, Python recommends using the os module.


# shutil.rmtree("my_folder")  # Deletes folder and all contents

# os.remove("my_file.txt")  # Deletes a single file

