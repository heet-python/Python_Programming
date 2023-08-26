l1 = []
n = int(input("Enter Number Of Elements:"))
for i in range(1,n+1):
    elements=int(input(f"Enter The Element {i}:"))
    l1.append(elements)
l1.sort()

print("The Second Smallest Value In The List Is:",l1[1])
