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

def show_setosa(filepath):
    with open(filepath,'r')as f:
        data_list=json.load(f)
    print("\nDetails of all flowers with species name setosa is : \n")
    for x in data_list:
        if x["species"]=='setosa':
            print (x)

def min_max_area(path):
    with open(path,'r') as f:
        datalist=json.load(f)
    species_names=[]
    for x in datalist:
        species_names.append(x["species"])
    species_names=list(set(species_names))
    sepal_area=[]
    petal_area=[]
    for i in species_names:
        for j in datalist:
            if j['species']==i:
                sepal_area.append(j['sepalLength']*j['sepalWidth'])
                petal_area.append(j['petalLength']*j['petalWidth'])
        print("Maximum sepal area in ",i," species is : ",round(max(sepal_area),2))
        print("Minimum petal area in ",i," species is : ",round(min(petal_area)),2)
        sepal_area.clear()
        petal_area.clear()       

def sort_area(path):
    with open(path,'r')as f:
        data = json.load(f)
    for i in data:
        totalArea=(i['sepalLength']*i['sepalWidth'])+(i['petalLength']*i['petalWidth'])
        i.update({'TotalArea':round(totalArea,2)})
    print (data)
       
listdata=read_json(file_path)
dictdata=list_to_dict(file_path)
show_setosa(file_path)
min_max_area(file_path)
sort_area(file_path)
    