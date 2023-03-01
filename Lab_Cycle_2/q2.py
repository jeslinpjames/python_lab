def accept_list():
    my_list=list(int(x) for x in input("Enter elements ofn the list seperated by space : ").split())
    print(my_list)
    return my_list

def list_shift(my_list):
    k=int(input("Enter the number of places you want to shift the list by : "))
    my_list=my_list[-k:]+my_list[:-k]
    print("The list after shifting ",k," places is :",my_list)
    return my_list
def listtotuple(my_list):
    my_tuple=tuple([i for i in my_list])
    print("The tuple is : ",my_tuple)
    return my_tuple
def removeduplicates(my_tuple):
    my_tuple=tuple(set(my_tuple))
    new_list=list(my_tuple)
    print("The list after removing duplicates is : ",new_list)
    return new_list
def function(new_list):
    list1=[((x*x)-x) for x in new_list]
    print("The list is : ",list1)
    return list1
def merge(list1,new_list):
    new_list.sort()
    list1.sort()
    list2=new_list+list1
    print("The combined list is : ",list2)
    return list2

my_list=accept_list()
my_list=list_shift(my_list)
my_tuple=listtotuple(my_list)
new_list=removeduplicates(my_tuple)
list1=function(new_list)
list2=merge(list1,new_list)
