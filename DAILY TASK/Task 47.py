class A:
    def a(self):
        print("A")
class B(A):
    def b(self):
        print("B")
class C(A):
    def c(self):
        print("C")
class D(B,C):
    def d(self):
        print("D")
o1=D()
o1.d()
o1.c()
o1.b()
o1.a()
