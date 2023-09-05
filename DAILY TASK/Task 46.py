class GrandParent:
    def grandparent(self):
        print("Grand Parent")
class ParentA(GrandParent):
    def parentA(self):
        print("Parent A")
class ParentB(GrandParent):
    def parentB(self):
        print("Parent B")
class ChildA(ParentA):
    def childA(self):
        print("Child A")
class ChildB(ParentB):
    def childB(self):
        print("Child B")
o1=ChildA()
o2=ChildB()
o1.childA()
o1.parentA()
o1.grandparent()
o2.childB()
o2.parentB()
o2.grandparent()




