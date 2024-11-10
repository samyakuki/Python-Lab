import os
import datetime
directory_path = r"C:\Users\hp\Desktop\python lab"
current_time = datetime.datetime.now()
time_threshold = current_time - datetime.timedelta(days=30)
for path, names, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(path, file)
        file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_mod_time < time_threshold:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except:
                print(f"Failed to delete {file_path}")

