import json
file_path='D:/git/python_lab/Lab_Cycle_2/iris.json'
def read_json(file_path):    
    with open(file_path,'r') as f:
        data=json.load(f)
    for x in data:
        print(x,'\n')
    return data
def list_to_dict(filepath):
    with open(filepath,'r') as f:
        data=json.load(f)
    return data
    