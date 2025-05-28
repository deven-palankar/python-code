#WAP to find factorial of first n natural numbers

a = int(input('Enter a number'))

i = 1
b=1

while i<=a:
    b = i * b
    i = i + 1
print(b)