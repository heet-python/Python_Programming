list=[]
n=int(input("Enter A List Of Elements:"))
for i in range(0,n):
    elements=input("Enter Element"+str(i+1) + ":")
    list.append(elements)
max1=len(list[0])
temp=list[0]
for x in list:
    if (len(x)>max1):
        max1=len(x)
        temp=x
print("The Longest Length Word Is",temp)
