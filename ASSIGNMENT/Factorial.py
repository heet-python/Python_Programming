num=int(input("Enter Number:"))
factorial = 1
if num < 0:
    print("Factorial Cannot Be Calculated For",input)
elif num==0:
    print("Factorial Is !")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial Is :",factorial)
    
    
