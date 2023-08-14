string=input("Enter Something:")
digit,lower,upper,even,odd=0,0,0,0,0
for ch in string:
    if ch.islower():
        lower=lower+1
    elif ch.isupper():
        upper=upper+1
    elif ch.isdigit():
        digit=digit+1
        if int(ch)%2 == 0:
            even +=1
        else:
            odd +=1
    else:
        pass
print("The Number Of Uppercase is", upper)
print("The Number Of Lowercase is", lower)
print("The Number Of Digit is",digit)
print("The Number Of Even Digit is",even)
print("The Number Of Odd Digit is",odd)
