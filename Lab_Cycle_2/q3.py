import json
file_path='D:/git/python_lab/Lab_Cycle_2/iris.json'
def read_json(file_path):    
    with open(file_path,'r') as f:
        data=json.load(f)
    print("The list with each line of the file as a element is : \n")
    for x in data:
        print(x,'\n')
    return data
def list_to_dict(filepath):
    with open(filepath,'r') as f:
        data=json.load(f)
    print("The file as a list of dictionary objects is : \n")
    print (data)
    return data
data=read_json(file_path)
data=list_to_dict(file_path)
    