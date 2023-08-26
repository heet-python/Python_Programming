n=int(input("Enter A Number:"))
factorial = 1

for i in range(1,n+1):
    if n>=1:
        factorial=factorial*i
print(factorial)
