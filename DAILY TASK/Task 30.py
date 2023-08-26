value=eval(input("Enter A List:"))
list=[]
for i in value:
    if i not in list:
        list.append(i)
print("The New List Is:",list)
