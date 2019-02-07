import zipfile
print(dir(zipfile))
import os
print(os.getcwd())

ref = zipfile.ZipFile(r"C:\Users\DBREDDY\Desktop\feb3_file.zip", 'r')
ref.extractall(r"C:\Users\DBREDDY\Desktop")
ref.close()
