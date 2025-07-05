# The os module in Python is like a bridge between your code and the operating system—it lets you interact with files,
# folders, environment variables, and system-level tasks in a portable way

# What You Can Do with os module --->

# Rename file/folder	    ||  os.rename("old", "new")	 ||    Renames a file or folder



import os 

folder_path = r"E:\Jyotsna\Python_Learning\20_Module_in_python\OS_module\Data1"

try:
    os.mkdir(folder_path)
    print("Folder created.")
except FileExistsError:
    print("Folder already exists.")


os.makedirs(folder_path, exist_ok=True)

for i in range(6):
    old_name = os.path.join(folder_path, f"Day{i+1}")
    new_name = os.path.join(folder_path, f"Tutorial{i+1}")
    try:
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} → {new_name}")
    except FileNotFoundError:
        print(f"{old_name} not found.")
    except Exception as e:
        print(f"Error renaming {old_name}: {e}")


