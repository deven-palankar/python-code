#WAP to check if entered list contains palindrome element

list=[1,2,3,2,3]

list2 = list.copy()

list.reverse()

if(list==list2):
    print('Palindrome')
else:
    print('Not Palindrome')