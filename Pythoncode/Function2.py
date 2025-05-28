#WAP to find factorial of first n natural numbers with function


a = int(input('Enter number to calculate factorial - '))+1

def factorial(int):
    f=1
    for i in range(1,a):
        f = f  * i
    return f

b = factorial(a)

print (b)