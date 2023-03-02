import json
file_path='D:/git/python_lab/Lab_Cycle_2/iris.json'
def read_json(file_path):    
    with open(file_path,'r') as f:
        listdata=json.load(f)
    print("The list with each line of the file as a element is : \n")
    for x in listdata:
        print(x,'\n')
    return listdata
def list_to_dict(filepath):
    with open(filepath,'r') as f:
        dictdata=json.load(f)
    print("The file as a list of dictionary objects is : \n")
    print (dictdata)
    return dictdata
def show_setosa(data_list):
    print("\nDetails of all flowers with species name setosa is : \n")
    for x in data_list:
        if x["species"]=='setosa':
            print (x)

listdata=read_json(file_path)
dictdata=list_to_dict(file_path)
show_setosa(listdata)
    