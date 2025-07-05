# The seek()  --->
# used to move the file cursor to a specific position, 
# allowing you to read or write from anywhere in the file—not just from the beginning.

# syntax : file.seek(offset, whence)
# offset: Number of bytes to move the cursor.
# whence (optional): Reference point for the offset.
# 0 → Beginning of the file (default)
# 1 → Current cursor position
# 2 → End of the file
# In text mode, only whence=0 is allowed. For 1 or 2, use binary mode ('rb' or 'wb').


# tell() ---->
# The tell() function in Python is used to get the current position of the file cursor—that is, where Python is reading or writing in the file.
# syntax : file.tell()
# Returns an integer representing the number of bytes from the beginning of the file.
# No parameters required.
# Use Cases --->
# -----------------------------------------------------------------
# Scenario	                    ||   Why tell() Helps
# -----------------------------------------------------------------
# Tracking read/write progress	||   Know how far you've processed a file
# Debugging file operations	    ||   Confirm cursor position before/after I/O
# Combining with seek()	        ||   Jump to or return from specific points

# truncate() ---->
# used to resize a file
# syntax : file.truncate(size)
# size (optional): The number of bytes to keep. If omitted, it truncates the file at the current cursor position.



with open("my_file.txt", "r") as f:
    f.seek(10) # Move cursor to 10th byte
    print(f.tell())          
    print(f.read(5))      # Read from there onward


with open("my_file.txt", "rb") as f:
    f.seek(-10, 2)       # Move 10 bytes before end
    print(f.read())      # Read last 10 bytes


with open(r"my_file_2.txt", "w") as f1:
    f1.write('Hello world')
    f1.truncate(3)


with open(r"my_file_2.txt", "r") as f1:         
    print(f1.read()) 


