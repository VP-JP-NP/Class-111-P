import os
import shutil

from_dir = '/Users/vedapatel/Downloads'
to_dir = '/Users/vedapatel/Document_files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.pdf', '.doc', '.docx', '.ppt','.jpg','png','mp3']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name

        if os.path.exists(path2):
            shutil.move(path1, path3)
            print("Moving " + file_name + ".....")
        else:
            os.makedirs(path2)
            shutil.move(path1, path3) 
            print("Moving " + file_name + ".....")   
