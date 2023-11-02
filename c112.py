import os
import shutil

from_dir = "C:/Users/hi/Downloads"
to_dir = "C:/Users/hi/Desktop"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
       path1 = from_dir + '/' + file_name
       print(path1)
       path2 = to_dir + '/' + 'image_files'
       print(path2)
       path3 = to_dir + '/' + 'image_files' + '/' + file_name
       print(path3)
       
       if os.path.exists(path2):
           print("Moving the" + file_name + "...")
           shutil.move(path1, path3)

       else:
           os.mkdir(path2) 
           print("Moving the" + file_name + "...")
           shutil.move(path1, path3)
     

