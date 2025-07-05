import greet

# Every Python file has a built-in variable called __name__.

# If you're running the file directly, __name__ becomes "__main__".
# If you're importing the file as a module, __name__ becomes the file name.

# If you don’t use if __name__ == "__main__": in your Python file, then all top-level code will run even 
# when the file is imported as a module into another script. That can lead to unexpected behavior or side effects.

# So, use if __name__ == "__main__": -->
# Keeps your modules clean and reusable
# Prevents accidental execution during import
# Lets you write test/demo code safely

greet.welcome()

print(__name__)
