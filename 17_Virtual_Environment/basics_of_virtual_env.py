# A virtual environment in Python is like a personal sandbox—it lets you isolate your project’s dependencies so they don’t interfere with other projects or your system-wide Python setup.

# Why Use a Virtual Environment--->
#  Keeps each project’s packages separate
#  Prevents version conflicts between libraries
#  Lets you test with different Python versions
#  Makes your project easier to share and reproduce

# How to Create and Use One -->
# 1. Create a Virtual Environment
#    run this commnd in terminal -- >python -m venv venv_name
#    This creates a folder (venv_name) with its own Python interpreter and pip.
# 2. Activate It
#    OS	Command
#       Windows -->	jyo\Scripts\activate
#                   jyo\Scripts\activate.bat
#                   .jyo\Scripts\activate\ps1   --->for power shell
#       macOS/Linux	--> source venv_name/bin/activate
#    Once activated, your terminal will show (venv_name or jyo in our case)—you’re now inside the virtual environment.
# 3. Install Packages
#      run this commnd in terminal --> pip install requests
#      Packages go into the virtual environment only—not system-wide.
#      you can instal particular versions also --> pip install pandas==1.4.4
# 4. Deactivate When Done
#      run this commnd in terminal --> deactivate
# 5. To share your environment setup:
#      pip freeze > requirements.txt
# 6. To recreate it later:
#      pip install -r requirements.txt