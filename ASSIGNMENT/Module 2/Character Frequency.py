string=input("Enter Something:")
frequency = {}
for i in string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("The Frequency Of Each Letter Is:"+str(frequency))
