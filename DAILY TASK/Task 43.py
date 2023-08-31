a=[1,2,3]
b=[3,2,1]

c=zip(a,b)
print(c)
print(list(c))


h,p=zip(*zip(a,b))
print(h)
print(p)
print(list(h))
print(type(h))
print(list(p))
print(type(p))


