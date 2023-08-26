def natural(x):
    if x<=0:
        return 0
    else:
        return x+natural(x-1)
    
n=int(input("Enter A Number:"))
print("Addition Of Natural Numbers Is:",natural(n))
