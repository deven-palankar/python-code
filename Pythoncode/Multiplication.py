## WAP to print multiplication of N number

a=input('Please enter number for which you want table to be printed - ')

i=1

print (type(a))
print (type(i))

while i<=10:
    b= int(a) * i
    print(str(i)+'*'+str(a)+'=',b)
    i = i+1

