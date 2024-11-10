import os
import hashlib
directory_path =r"C:\Users\hp\Desktop\python lab"
hashes = {}
duplicates = []
for path, _, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(path, file)
        with open(file_path, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in hashes:
                duplicates.append((file_path, hashes[file_hash]))
            else:
                hashes[file_hash] = file_path
if duplicates:
    print("Duplicate files found")
else:
    print("No duplicate files") 
