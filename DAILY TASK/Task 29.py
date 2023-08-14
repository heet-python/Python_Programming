List=[]
n=int(input("Enter The Size Of List:"))
for i in range(n):
    Elements=int(input("Enter The Elements In List:"))
    List.append(Elements)
    List.sort()
    List.sort(reverse=False)
print("Ascending Order:",List)
print("Descending Order:",List[::-1])

