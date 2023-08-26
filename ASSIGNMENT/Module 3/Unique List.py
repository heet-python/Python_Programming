L1=eval(input("Enter A List:"))
unique_list=[]
for i in L1:
    if i not in unique_list:
       unique_list.append(i)
print("Unique List:",unique_list)
