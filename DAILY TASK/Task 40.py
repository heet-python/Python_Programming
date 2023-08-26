def fun(x):
    if x<=0:
        print(0)
    else:
        print(x)
        fun(x-1)
fun(10)
