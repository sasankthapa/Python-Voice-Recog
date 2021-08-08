import os
import json

#only parse if it is a folder
#this does not check recursively
def get_map_from_path(path):
    to_return_arr=[]
    for name in os.listdir(path):
        if name.find('.')>0:
            continue

        to_return={}
        to_return['name']=name.lower()
        to_return['path']=path+name
        to_return_arr.append(to_return)
    return(to_return_arr)

with open('folder_list.csv','w+') as file1:
    json.dump(get_map_from_path('V:\\'),file1, ensure_ascii=False, indent=4)

