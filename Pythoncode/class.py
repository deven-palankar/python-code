class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        i=1
        for i in self.marks:
            sum = sum + i
            i = i+1
        return sum/3



s1 = Student('Deven',[10,15,20])
print(s1.name)
print(s1.marks)
avg = s1.avg()
print(avg)