str1=input("Enter A Word:")
if len(str1) < 3:
    print(str1)
elif str1[-3:] == "ing":
    print(str1 + "ly")
else:
    print(str1 + "ing")
