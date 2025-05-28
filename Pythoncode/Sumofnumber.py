#WAP to find sum of first n natural numbers

a = int(input('Enter a number'))

i = 1
b=0

while i<=a:
    b = i + b
    i = i + 1
print(b)