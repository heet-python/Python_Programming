a=int(input("Maths:"))
b=int(input("Science:"))
c=int(input("English:"))

x=(a+b+c)*100/300
print(x)

if x<=33:
    print("Fail")

elif x<=70:
    print("C Grade")

elif x<=80:
    print("B Grade")

elif x<=90:
    print("A Grade")
    
else :
    print("Pass")
    


