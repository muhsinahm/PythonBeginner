#Find content of directory using os module

import os
path="/Users/muhsin/Documents/projects"
dir_list=os.listdir(path)
print("files and directories in '", path,  "' :")
print(dir_list)
for items in dir_list:
    print(items)