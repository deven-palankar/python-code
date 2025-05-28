a = int(input('Enter the number1:'))
b = int(input('Enter the number2:'))
c = int(input('Enter the number3:'))

if((a>b) and (a>c)):
    print('A is greatest:',a)
elif(b>c):
    print('B is greatest:',b)
else:
    print('C is greatest:',c)