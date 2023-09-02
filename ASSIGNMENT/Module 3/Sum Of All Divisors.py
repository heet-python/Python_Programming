def dict(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
n=int(input("Enter Number1:-"))
n1=int(input("Enter Number2:-"))
print(dict(n))
print(dict(n1))

