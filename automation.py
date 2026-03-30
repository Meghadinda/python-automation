import os

folder = input("Enter folder path: ")

files = os.listdir(folder)

for i, file in enumerate(files):
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, f"file_{i}.txt")
    
    os.rename(old_path, new_path)

print("All files renamed!")