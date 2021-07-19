import json

tempMap={}
tempMap['index']=0
tempMap['name']="youth"
tempMap['url']="https://www.youtube.com/watch?v=_ZdsmLgCVdU"

tempMap2={}
tempMap2['index']=0
tempMap2['name']="hcv"
tempMap2['path']="V:\\hcv\\"

def create_file_with_dummy():
    with open('website_list.csv','w+') as file1:
        json.dump([tempMap],file1, ensure_ascii=False, indent=4)
    with open('folder_list.csv','w+') as file2:
        json.dump([tempMap2],file2, ensure_ascii=False, indent=4)

create_file_with_dummy()

def readFile(filename):
    with open(filename,'r') as f:
        data=json.loads(f.read())
    return data

url_list=readFile('website_list.csv')
folder_list=readFile('folder_list.csv')

def find_url(name):
    print(name)
    for data in url_list:
        print(data['name']==name)
        if data['name']==name:
            return (True, data['url'])
    return (False,)

def find_folder(name):
    for data in folder_list:
        print(data['name']==name)
        if data['name']==name:
            return (True, data['path'])
    return (False,)
