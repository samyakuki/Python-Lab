import os
import shutil
directory_path = r"C:\Users\hp\Desktop\python lab"
destination_folder = r"C:\Users\hp\Desktop\python lab"
pyfile = "Python"
textfile = "Textfiles"
pdffile = "Pdffiles"
others = "Others"
os.makedirs(os.path.join(destination_folder, pyfile), exist_ok=True)
os.makedirs(os.path.join(destination_folder, textfile), exist_ok=True)
os.makedirs(os.path.join(destination_folder, pdffile), exist_ok=True)
os.makedirs(os.path.join(destination_folder, others), exist_ok=True)
for path, names, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(path, file)
        if file.split('.')[-1] == "py":
            out_path = os.path.join(destination_folder, pyfile, file)
        elif file.split('.')[-1] == "txt":
            out_path = os.path.join(destination_folder, textfile, file)
        elif file.split('.')[-1] == "pdf":
            out_path = os.path.join(destination_folder, pdffile, file)
        else:
            out_path = os.path.join(destination_folder, others, file)
        if os.path.abspath(file_path) != os.path.abspath(out_path):
            shutil.copy(file_path, out_path)

