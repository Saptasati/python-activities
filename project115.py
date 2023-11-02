import os
#Source file path
source = "C:/Users/hi/main.txt"
#Destination sfile path
dest = "C:/Users/hi/newfile.txt"
# Renaming the file
os.rename(source, dest)
print("Source path renamed to destination path successfully")