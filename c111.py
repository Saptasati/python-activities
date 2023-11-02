import os
import shutil
os.getcwd()
os.mkdir("Images")

#Splitting the text
path1 = "C:/Users/hi/Downloads/C102_assets-main/C102_assets-main"
root, extension = os.path.splitext(path1)
print("The root element are", root)
print("The extension are", extension)

#Making a copy of file images
source= "C:/Users/hi/Desktop/python-code/class110.py"
destination = "C:/Users/hi/Downloads"
dest = shutil.copy(source, destination)
print("After copying the file")