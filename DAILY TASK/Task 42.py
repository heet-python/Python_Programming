class calculator:
    def addition(self):
        self.no=int(input("Enter A Number:"))
        self.no1=int(input("Enter A Number:"))
        return self.no+self.no1
    def subraction(self):
        self.no=int(input("Enter A Number:"))
        self.no1=int(input("Enter A Number:"))
        return self.no-self.no1
ob1=calculator()
print(ob1.addition())
print(ob1.subraction())
