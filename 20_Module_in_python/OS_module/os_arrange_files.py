import os

base_path = r"E:\Jyotsna\Python_Learning"
folders = os.listdir(base_path)

for folder in folders:
    if folder[0].isdigit():
        parts = folder.split("_", 1)
        if parts[0].isdigit():
            new_name = f"{int(parts[0]):02d}_{parts[1]}"
            os.rename(os.path.join(base_path, folder), os.path.join(base_path, new_name))
