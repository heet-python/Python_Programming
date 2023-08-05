even=0
odd=0
for i in range(1,11):
    Number=int(input(f"Enter Number {i} : "))
    if (Number%2) == 0:
        even += 1
    else:
        odd += 1
print("Even Number Is",even)
print("Odd Number Is",odd)
