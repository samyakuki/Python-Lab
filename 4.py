import os
total_size = 0
directory_path = r"C:\Users\hp\Desktop\python lab"
for path, names, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(path, file)
        print(f"{file} : {os.path.getsize(file_path)}")
        total_size += os.path.getsize(file_path)
print(total_size)
