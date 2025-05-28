#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

marks.update({input('Enter subject 1'):input('Enter marks 1')})
marks.update({input('Enter subject 2'):input('Enter marks 2')})
marks.update({input('Enter subject 3'):input('Enter marks 3')})

print(marks)