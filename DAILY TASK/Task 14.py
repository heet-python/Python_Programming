status=True
while status:
    num=int(input("Enter Lucky Number:"))
    if num==33:
        print("You Won")
        break
    else:
        print("Wrong Number")

    choice=input("Do You Want To Continue?['Y/N']:")
    if choice=="Y":
        status=True
    else:
        status=False
