def addition(num1,num2):
    return num1+num2
def subraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def floordivison(num1,num2):
    return num1//num2
def exponent(num1,num2):
    return num1**num2

n=int(input("Enter Number1:"))
n1=int(input("Enter Number2:"))

print("Add",addition(n,n1))
print("Sub",subraction(n,n1))
print("Mul",multiplication(n,n1))
print("Div",division(n,n1))
print("FD",floordivison(n,n1))
print("Expo",exponent(n,n1))
