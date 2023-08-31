class Parent1:
    def display1(self):
        print("1st Parent")
class Parent2:
    def display2(self):
        print("2nd Parent")
class Parent3:
    def display3(self):
        print("3rd Parent")
class Child(Parent1,Parent2,Parent3):
    def display(self):
        print("Child Here")

o1=Child()
o1.display()
o1.display1()
o1.display2()
o1.display3()
