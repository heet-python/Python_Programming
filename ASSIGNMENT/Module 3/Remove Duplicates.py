list=[1,2,3,4,4,3,33]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print("List",list)        
print("New List",list1)
