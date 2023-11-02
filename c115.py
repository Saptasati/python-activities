import os 
#Source file path
source = "C:/Users/hi/Desktop/Image_Files"
#destination file path
dest = "C:/Users/hi/Desktop/Saptasati_Files"

os.rename(source, dest)
print("Source path renamed to destination path successfully!")