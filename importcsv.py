import json

tempMap={}
tempMap['index']=0
tempMap['name']="youth"
tempMap['url']="https://www.youtube.com/watch?v=_ZdsmLgCVdU"

def create_file_with_dummy():
    with open('website_list.csv','w+') as file1:
        json.dump([tempMap],file1, ensure_ascii=False, indent=4)

def readFile():
    with open('website_list.csv','r') as f:
        data=json.loads(f.read())
    return data

urlList=readFile()

def find_url(name):
    print(name)
    for data in urlList:
        print(data['name']==name)
        if data['name']==name:
            return (True, data['url'])
    return (False,)

