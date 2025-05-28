tup = (1,2,3,4,5,6,7)

i = 0

a = int(input('Enter a number to search - '))

while i<len(tup):
    if(a==int(tup[i])):
        print('exists')
        break
    i = i+1
