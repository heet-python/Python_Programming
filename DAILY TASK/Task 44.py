class Welcome:
    def display(self):
        print('''
            1. abd
            2. vadodara
            10....
            ''')
class Registration:    
    def input(self):
        self.a=input("Enter Your Email:")
        self.b=input("Enter Your Password:")
        self.c=input("Confirm Your Password:")

class Login:
    def validate(self):
        self.x=input("Enter Email:")
        self.y=input("Enter Password:")
        
    

#================flow of programe=============

w1=Welcome()
r1=Registration()
l1=Login()

w1.display()
n=input("Want reg ? :[Y/N] : ")
if n=="y" or n=="Y":
    status=True
    while(status):
        r1.input()
        if r1.b!=r1.c:
            print("Password Incorrect")
            status=True
        else:
            print("Now Login Process")
            l1.validate()
            if r1.a==l1.x and r1.b==l1.y:
                print("Login SucessFull")
            else:
                print("Login Denied")
            status=False
else:
    print("Thank You")


    


