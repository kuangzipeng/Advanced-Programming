import os
from pathlib import Path
import shutil
import re

def mkdir(path):
    folder=Path(path)
    if(folder.exists()):
        folder.iterdir()
        print("The folder already exists!")
        global exist_num
        exist_num = exist_num + 1
    else:
        folder.mkdir(exist_ok=True, parents=True)
        print("New folder:", path)

def move_folders(folder_mapping,original_path):
    with folder_mapping.open() as file:
        dirs = []
        for line in file:
            link = line.strip()
            link=re.sub('"',"",link)
            links=link.split("\t")
            dirs.append(links)
            file_name=links[0]
            new_path=links[1]
            olddir = original_path + os.sep + file_name
            newdir = new_path + os.sep + file_name
            shutil.copytree(olddir, newdir)
            print(file_name,"is copied into",new_path)
        return dirs

def rename_folders(dirs):
    for links in dirs:
        path=links[1]
        name=links[0]
        old_name=path+os.sep+name
        if "All" in name:
            os.rename(old_name,path+os.sep+"all")
            print(name,"is renamed","all")
        elif "IOS" in name:
            os.rename(old_name,path+os.sep+"ios")
            print(name, "is renamed", "ios")

#main
folder_num = 0
exist_num = 0
folder_list_dir = Path(r"")
folder_mapping = Path(r"")
original_path = ""

with folder_list_dir.open() as fn:
    for path in fn.readlines():
        path = path.strip()
        folder_num = folder_num + 1
        mkdir(path)

if (exist_num == folder_num):
    exit()  #All folders have been created
elif (0 < exist_num < folder_num):
    print("Please delete all folders and rerun the program!")   # If user deletes something by mistake, they need to rerun the script.
    exit()
else:
    dirs = move_folders(folder_mapping, original_path)
    rename_folders(dirs)



