# command-line utilities --->
# tools you can run directly from the terminal to automate tasks, process data, or interact with files

# Common Modules for CLI Utilities

# Module	   ||  Purpose
# argparse	   ||  Parse command-line arguments cleanly
# sys	       ||  Access command-line arguments via sys.argv
# click	       ||  Build beautiful CLI apps with decorators
# os	       ||  Interact with the operating system
# subprocess   ||  Run shell commands from Python


# Built-in Python CLI Utilities
# You can run some Python modules directly from the command line using -m:

# Command	                        What It Does
# python -m http.server	            Starts a simple web server
# python -m webbrowser <url>	    Opens a URL in your browser
# python -m json.tool <file.json>	Pretty-prints JSON
# python -m calendar	            Displays a calendar



import argparse

parser = argparse.ArgumentParser(description="Simple File Manager")
parser.add_argument("filename", help="Name of the file to create")
parser.add_argument("--text", help="Text to write into the file", default="Hello!")

args = parser.parse_args()

with open(args.filename, "w") as f:
    f.write(args.text)

print(f"File '{args.filename}' created with content: {args.text}")
