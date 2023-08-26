#Functions
#function parameter
#*args : arguments

def fun(*x):
    for i in x:
        print(i)
fun(45,65)

# **kwargs : keyword arguments (Arbitary Arguments)

def fun2(**n):
    for i in n.items():
        print(i)
fun2(n1=12,n2=23,n3=34)
