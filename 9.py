import os
import datetime
directory_path = r"C:\Users\hp\Desktop\python lab"
for path, names, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(path, file)
        print(f"Name : {file} Size : {os.path.getsize(file_path)} Last Modified : {datetime.datetime.fromtimestamp(os.path.getmtime(file_path))}")
