ascii_number = 65
for i in range(0,5):
    for x in range(0,i+1):
        letter= chr(ascii_number)
        print(letter, end=" ")
        ascii_number +=1
    print()
