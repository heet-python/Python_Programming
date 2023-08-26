d1={'email':'123@gmail.com','pass':'321321'}
user_email=input("Enter Email:")
user_pass=input("Enter Password:")

if user_email == d1['email'] and user_pass == d1['pass']:
    print(True)
else:
    print(False)
    
