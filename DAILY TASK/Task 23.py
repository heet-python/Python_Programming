string=input("Enter Something:")
digit=letter=space=0
for ch in string:
    if ch.isdigit():
        digit=digit+1
    elif ch.isalpha():
        letter=letter+1
    elif ch.isspace():
        space=space+1
    else:
        pass
print("The Number Of Letters is", letter)
print("The Number Of Digits is", digit)
print("The Number Of Spaces is",space)
